"""Canonical draft wiki formatting and checks for Sowmya's governing schema.
No model calls, source edits, compliance decisions or automatic review approval.
"""
import copy,json,re
from pathlib import PurePosixPath
import yaml

ALLOWED_RELATIONS={'defines','cites','modifies','deletes','replaces','supersedes','superseded_by','clarifies','requires','evidenced_by','governs','related_to','belongs_to'}
RELATION_ALIASES={'relates_to':'related_to','references':'cites','amends':'modifies'}
TYPE_ALIASES={'wiki_hub':'hub','wiki_index':'catalog','wiki_log':'log','wiki_qa':'qa','wiki_schema':'schema'}
PARAMETER_HEADER='| Parameter | Value | Citation | Status |'

def wrap(meta,body):
    return '---\n'+yaml.safe_dump(meta,sort_keys=False,allow_unicode=True,width=1000000)+'---\n\n'+body.strip()+'\n'

def expected_type(path):
    path=path.removeprefix('wiki/')
    if path=='SCHEMA.md':return 'schema'
    if path=='index.md':return 'catalog'
    if path=='log.md':return 'log'
    if path.startswith('concepts/'):return 'concept'
    if path.startswith('qa/'):return 'qa'
    return 'hub'

def record(e):
    try:return json.loads(e.get('quote',''))
    except (ValueError,TypeError):return {}

def short_label(e):
    path=e['okf_path'];h=e['heading'];r=record(e)
    parent=e.get('parent_record_context',{})
    cid=r.get('clause_id') or parent.get('clause_id') or ''
    if not cid:
        m=re.search(r'Clause\s+([0-9]+(?:\.[0-9]+)*)',h,re.I)
        if m:cid=m[1]
    for suffix,prefix in [('/secB.md','ITT'),('/secC.md','EQC'),('/secE.md','GCC'),('/secF.md','SCC')]:
        if path.endswith(suffix):
            if '/contract_data' in e.get('json_path','') and r.get('item_number') is not None:return 'Contract Data Item '+str(r['item_number'])
            if r.get('scc_clause_id'):return 'SCC '+str(r['scc_clause_id'])
            return prefix+(' '+str(cid) if cid else '')
    if path.endswith('/secA.md'):
        m=re.search(r'(Key Detail|Instruction)\s+(\d+)',h)
        return 'NIT '+m[0] if m else 'NIT'
    if '/addendum_and_corrigendum/' in path:
        n=r.get('corrigendum_number') or re.search(r'C(\d+)',path)[1]
        ref=r.get('affected_reference') or r.get('printed_amendment_serial') or ''
        return 'Corrigendum '+str(n)+(' '+str(ref) if ref else '')
    if '/Vol3/' in path:return 'SHE'+(' '+str(cid) if cid else ' '+PurePosixPath(path).stem)
    if '/Vol2/' in path:
        m=re.search(r'part(\w+)\.md',path)
        return 'Vol 2 Part '+(m[1] if m else '')+(' Clause '+str(cid) if cid else '')
    if path.endswith('/secG.md'):return 'Contract Forms'+(' '+str(r.get('form_number')) if r.get('form_number') else '')
    return 'Financial Section J' if '/Financial/' in path else h[:70]

def link(e):return '[['+e['okf_path'].removesuffix('.md')+'#'+e['heading']+'|'+short_label(e)+']]'
def location(e):
    if e.get('sheet_cells'):return '`'+e['source_document']+'`, workbook '+str(e['sheet_cells'])
    ps=e.get('pdf_pages',[])
    return '`'+e['source_document']+'`, '+('PDF p. '+str(ps[0]) if len(ps)==1 else 'PDF pp. '+', '.join(map(str,ps)))
def citation(e):return link(e)+', '+location(e)+(' (`'+e['json_path']+'#'+e.get('json_pointer','')+'`)' if e.get('json_path') else '')
def cell(s):return str(s).replace('|','\\|').replace('\r',' ').replace('\n',' ')
def wiki_link(path,title):return '[[wiki/'+path.removesuffix('.md')+'|'+title+']]'

def source_paths(meta):
    out=[]
    for s in meta.get('sources',[]):
        if isinstance(s,str):out.append(s)
        elif isinstance(s,dict):
            for k in ['okf_path','json_path']:
                if s.get(k):out.append(s[k])
    for c in meta.get('claims',[]):
        for e in c.get('citations',[]):
            out.append(e['okf_path'])
            if e.get('json_path'):out.append(e['json_path'])
    for e in meta.get('answer_citations',[]):
        out.append(e['okf_path'])
        if e.get('json_path'):out.append(e['json_path'])
    return sorted(set(out))

def amendment_rows(claim,catalogue):
    rows=[]
    for a in claim.get('amendment_annotations',[]):
        ids=a['evidence_ids'];records=[record(catalogue[i]) for i in ids]
        c1=next((r for r in records if r.get('corrigendum_number')==1),None)
        c3=next((r for r in records if r.get('corrigendum_number')==3),None)
        deletion=next((r for r in records if r.get('target_gcc_subclauses')),None)
        if c3:
            old=c3['existing_selected_text'];new=c3['replacement_selected_text']
            value='~~'+old+'~~ → '+new
            if a['scope'].startswith('Baseline') and c1:value='~~'+c1['existing_selected_text']+'~~ → ~~'+c1['replacement_selected_text']+'~~ → '+new
            status='Superseded historical date/time fields by Corrigendum 3; latest among supplied notices; Pending review'
        elif deletion:
            target=', '.join(deletion['target_gcc_subclauses'])
            value='~~Historical GCC '+target+' provision~~ → '+deletion['replacement_selected_text']
            status='Deleted by Corrigendum 2 ('+deletion['affected_reference']+'); Pending review'
        else:
            value=a['text'];status=a['state'].capitalize()+' — '+a['scope']+'; Pending review'
        rows.append((a['scope'],value,ids,status))
    return rows

def review_inventory(pages,previous=None):
    old={x['claim_id']:x for x in (previous or [])}
    rows=[]
    for path,p in sorted(pages.items()):
        meta=p.get('meta',p.get('metadata',{}))
        for c in meta.get('claims',[]):
            if c.get('status')=='reviewed':continue
            records=[]
            for e in c.get('citations',[]):
                status=e.get('source_review_status','not_recorded')
                records.append({k:e[k] for k in ['id','okf_path','json_path','json_pointer','source_document','pdf_pages','sheet_cells'] if k in e}|{'review_status':status})
            checks=['Compare exact wording, values, units, conditions and exceptions with the original PDF; confirm the cited physical PDF page.']
            if any('visual' in r['review_status'] for r in records):checks.append('Inspect table columns, merged cells and layout against the source PDF.')
            if c.get('amendment_annotations'):checks.append('Verify the exact amendment/deletion scope and original-to-replacement sequence; do not infer broader precedence.')
            if c.get('kind')=='relation':checks.append('Confirm source and target, relation type and explicit versus inferred classification.')
            row={'claim_id':c['id'],'page':path if path.startswith('wiki/') else 'wiki/'+path,'claim':c['text'],'source_records':records,'checks':checks,'status':'pending_manual_review'}
            prior=old.get(c['id'])
            if prior and prior.get('claim')==row['claim'] and prior.get('source_records')==records:
                for k in ['status','reviewer','reviewed_at','resolution']:
                    if k in prior:row[k]=prior[k]
            rows.append(row)
    return rows

def format_page(path,metadata,catalogue,now):
    path=path.removeprefix('wiki/');m=copy.deepcopy(metadata);m['type']=expected_type(path)
    if m['type'] not in ['hub','concept']:raise ValueError('format_page expects a hub or concept')
    claims=m.get('claims',[]);m['sources']=source_paths(m)
    foot={};passages={}
    def cite(ids):
        refs=[]
        for i in ids:
            if i not in catalogue:raise ValueError('Missing formatter evidence '+i)
            passages[i]=catalogue[i]
            if i not in foot:foot[i]='e'+str(len(foot)+1)
            refs.append('[^'+foot[i]+']')
        return ' '.join(refs)
    b=['# '+m['title'],'','> Draft source synthesis. Pending PDF and human review; no compliance or applicability decision.','','## Summary','']
    summaries=[c for c in claims if c['kind']=='summary'];chosen=summaries[:2]
    if chosen:
        for c in chosen:b += [c['text']+' '+cite(c['evidence_ids']),'']
        if len(chosen)==1:b+=['The cited source statements remain provisional pending recorded review.','']
    else:b+=['This page organizes the cited source statements and relationships below. The page remains draft pending recorded source verification.','']
    b+=['## Key parameters','',PARAMETER_HEADER,'|---|---|---|---|']
    for c in claims:
        if c['kind']!='parameter':continue
        first=c['citations'][0];label=short_label(first)+' — '+c['id']
        status='Pending review'
        if c.get('amendment_annotations'):status+='; historical fields/provisions have scoped supersession below'
        b.append('| '+cell(label)+' | '+cell(c['text'])+' | '+cite(c['evidence_ids'])+' | '+cell(status)+' |')
    b+=['','## Where it appears','']
    all_ids=list(dict.fromkeys(i for c in claims for i in c['evidence_ids']))
    for c in claims:
        for a in c.get('amendment_annotations',[]):all_ids+=a['evidence_ids']
    for i in dict.fromkeys(all_ids):
        e=catalogue[i];passages[i]=e;b.append('- '+citation(e))
    b+=['','## Relations','','| Source | Relation | Target | Classification | Citation | Status |','|---|---|---|---|---|---|']
    for c in claims:
        if c['kind']!='relation':continue
        if c['relation_type'] not in ALLOWED_RELATIONS:raise ValueError('Unsupported relation '+c['relation_type'])
        b.append('| '+cell(short_label(catalogue[c['from_id']]))+' | '+c['relation_type']+' | '+cell(short_label(catalogue[c['to_id']]))+' | '+c['explicitness']+' | '+cite(c['evidence_ids'])+' | Pending review |')
        b += []
    b+=['']
    for c in claims:
        if c['kind']=='relation':b+=['- '+c['text']+' '+cite(c['evidence_ids'])]
    for rel in m.get('entity_relations',[]):
        if rel['relation_type'] not in ALLOWED_RELATIONS:raise ValueError('Unsupported entity relation')
        b.append('- **'+rel['relation_type']+' (inferred editorial navigation):** '+wiki_link(rel['target'],rel['title'])+'. '+cite(rel['evidence_ids']))
    b+=['','## Open questions and contradictions','']
    questions=[c for c in claims if c['kind'] in ['review_question','source_quirk']]
    if questions:
        for c in questions:b+=['- '+c['text']+' '+cite(c['evidence_ids'])+' See '+wiki_link('review_queue.md','review queue')+' and '+wiki_link('source_quirks.md','source quirks')+'.']
    else:b+=['No additional conflict is recorded on this page. Verification remains open in '+wiki_link('review_queue.md','the review queue')+'; absence of a recorded contradiction is not approval.']
    for x in m.get('scope_exclusions',[]):b+=['','- '+x['text']+' ('+x['citation']+').']
    b+=['','## Amendment states','','Historical source quotations are retained. A superseded field or deleted subclause does not make the entire page superseded.','','| Parameter | Value | Citation | Status |','|---|---|---|---|']
    for c in claims:
        for label,value,ids,status in amendment_rows(c,catalogue):b.append('| '+cell(label)+' | '+cell(value)+' | '+cite(ids)+' | '+cell(status)+' |')
    # Show explicit C2 deletion instructions on every page citing those records or referenced historical GCC text.
    page_records=[catalogue[i] for i in all_ids if i in catalogue]
    shown=set()
    for e in catalogue.values():
        r=record(e)
        if not r.get('target_gcc_subclauses'):continue
        targets=r['target_gcc_subclauses']
        relevant=e['id'] in all_ids or any(pe.get('okf_path','').endswith('/secE.md') and any(re.search(r'(?<!\d)'+re.escape(t)+r'(?!\d)',pe['quote']) for t in targets) for pe in page_records)
        if relevant and e['id'] not in shown:
            shown.add(e['id']);label='GCC '+', '.join(targets)
            b.append('| '+cell(label)+' | ~~'+cell(label+' historical provision')+'~~ → '+cell(r['replacement_selected_text'])+' | '+cite([e['id']])+' | '+cell('Deleted by Corrigendum 2 ('+r['affected_reference']+'); Pending review')+' |')
    b+=['','## Additional source statements','']
    for c in summaries[len(chosen):]:b+=['- '+c['text']+' '+cite(c['evidence_ids'])]
    b+=['','## Claim register','']
    # Explicit IDs are stable source-review references; no claim is removed by presentation changes.
    for c in claims:
        if c['kind']=='parameter':continue
        if c['kind'] not in ['summary','relation','review_question','source_quirk']:b+=['- '+c['text']+' '+cite(c['evidence_ids'])]
    b+=['Claim IDs and evidence records are retained in frontmatter. Every draft claim has an entry in '+wiki_link('review_queue.md','the claim-level review queue')+'.']
    for c in claims:
        for note in c.get('editorial_notes',[]):b+=['','- **Draft review note:** '+note['text']+' Supporting finding: `'+note['related_claim_id']+'`.']
    if m.get('review_items') is not None:
        b+=['','## Claim-level verification inventory','','One row per active draft claim; no item is marked reviewed by this formatter.','','| Page / Claim | Claim | Source records and pages | Required checks | Status |','|---|---|---|---|---|']
        for item in m['review_items']:
            ids=[r['id'] for r in item['source_records']]
            source_text=cite(ids)+' '+'; '.join((r.get('json_path','OKF')+'#'+r.get('json_pointer','')+' — '+r['review_status']) for r in item['source_records'])
            target=item['page'].removeprefix('wiki/')
            b.append('| '+cell(item['claim_id'])+' '+cell(wiki_link(target,'page'))+' | '+cell(item['claim'])+' | '+cell(source_text)+' | '+cell(' '.join(item['checks']))+' | '+cell(item['status'])+' |')
    for ext in m.get('hub_extensions',[]):b+=['','## '+ext['title'],'',ext['body']]
    b+=['','## Citation notes','']
    for eid,label in foot.items():b+=['[^'+label+']: '+citation(catalogue[eid])]
    # Obsidian pipes inside Markdown tables become footnotes, preserving live targets.
    table_refs=[]
    def table_link(match):
        table_refs.append(match[0].replace('\\|','|'))
        return '[^p'+str(len(table_refs))+']'
    b=[re.sub(r'\[\[[^\]]+\]\]',table_link,line) if line.startswith('|') else line for line in b]
    if table_refs:b+=['']+['[^p'+str(n)+']: '+value for n,value in enumerate(table_refs,1)]
    b+=['','<details>','<summary>Supporting source passages</summary>','']
    for eid,e in passages.items():b+=['### '+eid,'',citation(e),'',*['> '+line for line in e['quote'].splitlines()],'']
    b+=['</details>']
    # Include every source actually displayed, including review inventory and amendment rows.
    all_sources=set(m['sources'])
    for e in passages.values():
        all_sources.add(e['okf_path'])
        if e.get('json_path'):all_sources.add(e['json_path'])
    if m.get('scope_exclusions'):all_sources.add('wiki/SCHEMA.md')
    m['sources']=sorted(all_sources)
    return wrap(m,'\n'.join(b))

def sync_review_queue(planned,existing,catalogue,now,model):
    # Called by ingestion before its final preflight. It makes no API calls or approval decisions.
    combined={}
    for path,p in existing.items():combined[path]=p
    for path,text in planned.items():
        if not path.endswith('.md'):continue
        parts=re.split(r'^---\s*$',text.replace('\r\n','\n'),maxsplit=2,flags=re.M)
        if len(parts)==3:combined[path]={'meta':yaml.safe_load(parts[1]) or {},'body':parts[2],'text':text}
    queue=combined.get('review_queue.md')
    if not queue:return
    meta=copy.deepcopy(queue['meta']);meta['review_items']=review_inventory(combined,meta.get('review_items'));meta['last_review_inventory_updated']=now
    planned['review_queue.md']=format_page('review_queue.md',meta,catalogue,now)
    if 'log.md' in planned:planned['log.md']+='\n- Claim-level review inventory synchronized for all active draft claims; no human approval inferred.\n'

def schema_issues(pages,catalogue):
    issues=[];all_claims={};queue=None
    def issue(k,p,d):issues.append((k,p,d))
    for path,page in pages.items():
        m=page.get('metadata',page.get('meta',{}));body=page.get('body','');rel=path.removeprefix('wiki/');expected=expected_type(rel)
        if m.get('type')!=expected:issue('schema_type',path,'Expected '+expected+', got '+str(m.get('type')))
        if expected in ['hub','concept']:
            for key in ['sources','last_ingested']:
                if key not in m:issue('schema_frontmatter',path,'Missing '+key)
            for heading in ['Summary','Key parameters','Where it appears','Relations','Open questions and contradictions']:
                if not re.search(r'^## '+re.escape(heading)+r'\s*$',body,re.M):issue('schema_section',path,'Missing '+heading)
            if PARAMETER_HEADER not in body:issue('schema_parameter_table',path,'Missing required table columns')
            for c in m.get('claims',[]):
                all_claims[c['id']]=(path,c)
                if c['kind']=='relation' and c.get('relation_type') not in ALLOWED_RELATIONS:issue('schema_relation',path,c.get('relation_type'))
                for a in c.get('amendment_annotations',[]):
                    if a.get('state')=='superseded' and ('~~' not in body or 'Superseded' not in body and 'Deleted by' not in body):issue('schema_supersession',path,'Missing scoped supersession display')
            for r in m.get('entity_relations',[]):
                if r.get('relation_type') not in ALLOWED_RELATIONS:issue('schema_entity_relation',path,r.get('relation_type'))
        if expected=='qa':
            for key in ['question','asked','sources']:
                if not m.get(key):issue('schema_qa_field',path,'Missing '+key)
            for heading in ['Question','Answer','Citations','Wiki pages used','Caveats']:
                if not re.search(r'^## '+heading+r'\s*$',body,re.M):issue('schema_qa_section',path,'Missing '+heading)
            for e in m.get('answer_citations',[]):
                if catalogue.get(e.get('id'))!=e:issue('schema_qa_provenance',path,e.get('id'))
        if rel=='review_queue.md':queue=m
        if m.get('status')=='reviewed' and not m.get('human_review_event'):issue('schema_review_approval',path,'Reviewed page has no recorded human review event')
    items={x['claim_id']:x for x in (queue or {}).get('review_items',[])}
    for cid,(path,c) in all_claims.items():
        if c.get('status')=='reviewed':continue
        row=items.get(cid)
        if not row:issue('schema_review_inventory',path,'Missing claim '+cid);continue
        if row.get('claim')!=c['text'] or {r['id'] for r in row.get('source_records',[])}!=set(c['evidence_ids']):issue('schema_review_inventory',path,'Stale claim/source inventory '+cid)
        if not row.get('checks'):issue('schema_review_inventory',path,'Missing verification task '+cid)
    quirks=pages.get('wiki/source_quirks.md',pages.get('source_quirks.md',{}))
    body=quirks.get('body','')
    if 'Pre-bid replies have not been ingested' not in body:issue('schema_scope_notice','wiki/source_quirks.md','Missing pre-bid reply ingestion limitation')
    return issues

def format_qa(meta,answer_body):
    m=copy.deepcopy(meta);m['type']='qa';m['sources']=source_paths(m)
    used=m.get('wiki_pages_used',[])
    answer_body=re.sub(r'^# [^\n]+\n*','',answer_body,count=1)
    answer_body=re.sub(r'^(#{1,4}) ',lambda match:'#'*(len(match[1])+2)+' ',answer_body,flags=re.MULTILINE)
    b=['# '+m['title'],'','## Question','',m['question'],'','## Answer','',answer_body.strip(),'','## Citations','']
    if m.get('answer_citations'):
        for e in m['answer_citations']:b.append('- '+citation(e))
    else:
        for path in m['sources']:
            if path.endswith('.md'):b.append('- [['+path.removesuffix('.md')+'|'+PurePosixPath(path).name+']]')
            else:b.append('- `'+path+'`')
    b+=['','## Wiki pages used','']
    for path in used:b.append('- [['+path.removesuffix('.md')+'|'+PurePosixPath(path).name+']]')
    b+=['','## Caveats','','Draft only. Existing audit snapshots and historical counts in the answer retain their original context. PDF verification, source completeness, amendment interpretation and human approval are not established by formatting or a structural audit.']
    return wrap(m,'\n'.join(b))
