#!/usr/bin/env python3
"""Build, check, or search a source-reviewed illustrated catalog. Python 3.10+."""
import argparse
from datetime import date
import html
import ipaddress
import json
from pathlib import Path
import re
from urllib.parse import urlsplit, unquote, parse_qsl, urlencode

ROOT=Path(__file__).resolve().parents[1]
STATUS={'released':'Available setup','source-build':'Source / DIY build','research':'Research / prototype','archived':'Archived / legacy'}
STATUS_ZH={'released':'已有使用方案','source-build':'源码 / DIY 构建','research':'研究 / 原型','archived':'归档 / 旧版'}
REQUIRED={'id','name','category','url','summary','summary_zh','outcome','outcome_zh','devices','requirements','status','evidence_url','evidence_note','checked_at','limitations','steps'}
OPTIONAL={'source_url','media_url','media_note','spotlight'}
ID_PATTERN=r'[a-z0-9]+(?:-[a-z0-9]+)*'
TEXT_PATTERN=r'^(?![\s\S]*[\r\n<>\[\]|])(?=[\s\S]*\S)[\s\S]+$'
ICONS={'phone','tablet','reader','laptop','mirror','camera','voice','eye','hand','head','breath','object','fold','router','console'}
OUTPUTS={'frame','dashboard','server','music','cursor','command','control','game','gripper'}
CONFIG_TEXT={'title','title_zh','tagline','tagline_zh','description','description_zh'}
CONFIG_FIELDS=CONFIG_TEXT|{'slug','theme','categories','spotlights','sibling'}

class CatalogError(ValueError):pass

def need(value,message):
    if not value:raise CatalogError(message)

def read(path):
    def pairs(items):
        result={}
        for key,value in items:
            need(key not in result,f'Duplicate JSON key: {key}')
            result[key]=value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=pairs)

def public_url(value):
    need(isinstance(value,str) and not re.search(r'[\s<>"\\()]',value),f'Unsafe URL: {value!r}')
    try:
        p=urlsplit(value);host=(p.hostname or '').rstrip('.');port=p.port
    except ValueError as error:
        raise CatalogError(f'Invalid URL: {value}') from error
    need(value.startswith('https://') and host and p.username is None and p.password is None and port in (None,443),f'Expected HTTPS URL: {value}')
    need('.' in host and not host.endswith(('.local','.internal','.localhost')),f'Non-public hostname: {value}')
    try:address=ipaddress.ip_address(host)
    except ValueError:address=None
    if address:need(address.is_global,f'Non-public IP: {value}')
    else:
        labels=host.split('.')
        need(all(re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?',x,re.I) for x in labels) and re.search(r'[a-z]',labels[-1],re.I),f'Invalid hostname: {value}')
    return p

def identity(value):
    p=public_url(value);host=p.hostname.lower().rstrip('.').removeprefix('www.')
    app=re.search(r'/id(\d+)(?:/|$)',p.path)
    if host=='apps.apple.com' and app:return 'appstore:'+app[1]
    query=parse_qsl(p.query,keep_blank_values=True)
    if host=='play.google.com' and p.path.rstrip('/')=='/store/apps/details':
        package=[v for k,v in query if k=='id']
        if len(package)==1 and package[0]:return 'googleplay:'+package[0]
    path=unquote(p.path).rstrip('/')
    if host=='github.com':
        path=path.lower().removesuffix('.git')
        if len(path.strip('/').split('/'))==2:return host+path
    # Tracking parameters do not identify a project; other query values may.
    query=[(k,v) for k,v in query if not k.lower().startswith('utm_') and k.lower() not in {'fbclid','gclid'}]
    return host+path+('?' + urlencode(sorted(query)) if query else '')

def safe_text(value):
    return isinstance(value,str) and re.fullmatch(TEXT_PATTERN,value) is not None

def markdown(value):
    """Render plain data as text, never as authored Markdown."""
    return re.sub(r'([\\`*_{}\[\]()#+.!|>~\-])',r'\\\1',value.replace('&','&amp;'))

def rendered_project(project):
    result=dict(project)
    for key in ('name','summary','summary_zh','outcome','outcome_zh','evidence_note','media_note'):
        if key in result:result[key]=markdown(result[key])
    for key in ('devices','requirements','limitations','steps'):
        result[key]=[markdown(value) for value in result[key]]
    return result

def validate_config(config):
    need(isinstance(config,dict),'Config must be an object')
    need(config.keys()==CONFIG_FIELDS,'Invalid config fields')
    for key in CONFIG_TEXT:need(safe_text(config[key]),f'Invalid config text: {key}')
    need(isinstance(config['slug'],str) and re.fullmatch(ID_PATTERN,config['slug']),'Invalid repository slug')
    need(isinstance(config['theme'],str) and config['theme'] in {'afterlife','inputs'},'Invalid theme')
    # The sibling cross-link is intentionally authored Markdown, unlike data prose.
    need(isinstance(config['sibling'],str) and config['sibling'].strip(),'Invalid sibling Markdown')
    need(isinstance(config['categories'],list) and config['categories'],'Invalid categories')
    names=set();ids=set()
    for category in config['categories']:
        need(isinstance(category,dict) and category.keys()=={'id','name','name_zh','description','description_zh'},'Invalid category fields')
        need(all(safe_text(value) for value in category.values()),'Invalid category text')
        need(re.fullmatch(ID_PATTERN,category['id']),'Invalid category ID')
        need(category['id'] not in ids and category['name'].casefold() not in names,'Duplicate category')
        ids.add(category['id']);names.add(category['name'].casefold())
    selected=config['spotlights']
    need(isinstance(selected,list) and len(selected)==6,'Exactly six illustrated spotlights required')
    for spec in selected:
        need(isinstance(spec,dict) and spec.keys()=={'id','from','to','icon','output'},'Invalid spotlight fields')
        need(all(safe_text(value) for value in spec.values()),'Invalid spotlight text')
        need(re.fullmatch(ID_PATTERN,spec['id']),'Invalid spotlight ID')
        need(spec['icon'] in ICONS and spec['output'] in OUTPUTS,'Unknown diagram icon/output')
    need(len({x['id'] for x in selected})==6,'Duplicate spotlight')

def validate(projects,config,today=None):
    today=today or date.today()
    validate_config(config)
    need(isinstance(projects,list) and projects,'Empty or invalid catalog')
    categories=[x['name'] for x in config['categories']]
    need(len(categories)==len(set(categories)),'Duplicate category')
    seen={k:set() for k in ('id','name','url')}
    for p in projects:
        need(isinstance(p,dict),'Project must be an object')
        need(REQUIRED<=p.keys(),f'Missing fields: {REQUIRED-p.keys()}')
        need(p.keys()<=REQUIRED|OPTIONAL,f'Unknown fields: {p.keys()-(REQUIRED|OPTIONAL)}')
        for k in REQUIRED-{'devices','requirements','limitations','steps','url','evidence_url'}:
            need(safe_text(p[k]),f'{p.get("id")}: invalid {k}')
        need(re.fullmatch(ID_PATTERN,p['id']),f'Invalid ID: {p["id"]}')
        need(p['status'] in STATUS,f'{p["id"]}: unknown status')
        need(p['category'] in categories,f'{p["id"]}: unknown category')
        need(re.fullmatch(r'\d{4}-\d{2}-\d{2}',p['checked_at']) and date.fromisoformat(p['checked_at'])<=today,f'{p["id"]}: invalid/future date')
        for k in ['devices','requirements','limitations','steps']:
            need(isinstance(p[k],list) and p[k] and all(safe_text(x) for x in p[k]),f'{p["id"]}: invalid {k}')
        for k in ['url','evidence_url','source_url','media_url']:
            if k in p:public_url(p[k])
        if 'media_url' in p:need(safe_text(p.get('media_note')),f'{p["id"]}: media attribution required')
        if 'media_note' in p:need(safe_text(p['media_note']),f'{p["id"]}: invalid media note')
        if 'spotlight' in p:need(type(p['spotlight']) is bool,'spotlight must be boolean')
        for k in seen:
            v=identity(p[k]) if k=='url' else p[k].casefold()
            need(v not in seen[k],f'Duplicate {k}: {p[k]}');seen[k].add(v)
    ids={p['id'] for p in projects}
    selected=config['spotlights']
    need(len(selected)==6 and len({x['id'] for x in selected})==6,'Exactly six distinct illustrated spotlights required')
    need(all(x['id'] in ids for x in selected),'Unknown spotlight project')
    need(all(any(p['category']==c for p in projects) for c in categories),'Empty category')
    order={c:i for i,c in enumerate(categories)}
    need(projects==sorted(projects,key=lambda p:(order[p['category']],p['name'].casefold())),'Catalog is not sorted by category and name')

def load(root=ROOT):
    projects=read(root/'data/projects.json');config=read(root/'data/config.json')
    validate(projects,config)
    return projects,config

def find(projects,query='',status=None,category=None):
    words=query.casefold().split()
    return [p for p in projects if (status is None or p['status']==status) and (category is None or p['category']==category) and all(w in ' '.join([p['name'],p['summary'],p['summary_zh'],p['outcome'],p['outcome_zh'],*p['devices'],*p['requirements']]).casefold() for w in words)]

def slug(text):
    text=re.sub(r'!?\[([^\]]+)\]\([^)]*\)',r'\1',text)
    text=html.unescape(re.sub(r'<[^>]*>','',text))
    return re.sub(r'[^\w\- ]','',text.lower()).replace(' ','-')

def card(p,spec,index,theme):
    dark=theme=='inputs';bg='#101d33' if dark else '#f6f1e7';ink='#fff5e4' if dark else '#173e30';accent='#f58a70' if dark else '#c45b20';soft='#263a58' if dark else '#e3e8da'
    def esc(v):return html.escape(v,quote=True)
    left=esc(spec['from']);right=esc(spec['to'])
    # Original conceptual diagrams: labels map a documented input/device to an outcome.
    symbols={
      'phone':'<rect x="67" y="76" width="64" height="112" rx="12"/><path d="M85 88h28M90 176h18"/>',
      'tablet':'<rect x="42" y="84" width="120" height="88" rx="9"/><circle cx="150" cy="128" r="2"/>',
      'reader':'<rect x="51" y="76" width="102" height="112" rx="8"/><path d="M68 99h66M68 113h50M68 127h66M68 141h38M89 175h26"/>',
      'laptop':'<rect x="48" y="83" width="108" height="74" rx="6"/><path d="M38 174h128l-10-17H48z"/>',
      'mirror':'<rect x="61" y="65" width="82" height="132" rx="32"/><path d="m76 105 45-23m-45 54 49-24m-39 58h29"/>',
      'camera':'<rect x="40" y="97" width="120" height="67" rx="12"/><circle cx="100" cy="130" r="23"/><path d="M64 97v-13h47v13"/>',
      'voice':'<path d="M38 128h13m9-20v40m16-62v84m17-102v120m17-80v40m17-60v80m17-54v28m14-14h13"/>',
      'eye':'<path d="M31 128q69-74 138 0-69 74-138 0Z"/><circle cx="100" cy="128" r="25"/><circle cx="100" cy="128" r="8"/>',
      'hand':'<path d="M65 183V92q0-16 12-16t12 16v35-60q0-15 12-15t12 15v60-49q0-14 12-14t12 14v56-32q0-13 12-13t12 13v52q0 43-47 43H91q-18-1-26-14l-24-38q-6-12 5-18t19 8l11 14"/>',
      'head':'<path d="M69 185v-28q-30-14-29-52 2-47 48-48 42-1 50 37l18 28h-20v35h-28v28"/><path d="m161 72 14 13-14 13M180 86h-24"/>',
      'breath':'<path d="M35 103q45-18 77 0m-77 25q53-20 119 0m-119 25q42-15 77 0"/><circle cx="166" cy="128" r="13"/>',
      'object':'<rect x="55" y="84" width="90" height="90" rx="9"/><path d="M71 100h23v23H71zM108 100h21v23h-21zM71 138h23v21H71zM108 138h10v10h11v11h-21z"/>',
      'fold':'<path d="m44 166 57-92 57 92Z M101 74v92M44 166h114"/><path d="M81 77q20-28 42 0"/>',
      'router':'<rect x="43" y="122" width="116" height="49" rx="7"/><path d="M60 122V74m82 48V74M60 151h15m16 0h15m16 0h15"/>',
      'console':'<path d="M65 98h72q16 0 22 22l14 43q5 23-17 15l-25-22H70l-25 22q-20 8-15-15l13-43q6-22 22-22Z"/><path d="M57 116v27m-14-14h28"/><circle cx="135" cy="121" r="5"/><circle cx="151" cy="137" r="5"/>'}
    icon=symbols.get(spec['icon'],symbols['tablet'])
    output={'frame':'<path d="m307 155 28-29 22 17 19-34 34 46"/><circle cx="328" cy="105" r="8"/>','dashboard':'<path d="M309 96h42v29h-42zM366 96h38v29h-38zM309 140h95m-95 14h59"/>','server':'<path d="M309 98h94v23h-94zM309 138h94v23h-94zM320 109h8m-8 40h8"/>','music':'<path d="M341 145V98l40-10v48"/><ellipse cx="330" cy="148" rx="12" ry="9"/><ellipse cx="370" cy="139" rx="12" ry="9"/>','cursor':'<path d="m333 91 45 42-24 2-11 23Z"/>','command':'<path d="m310 105 17 15-17 15m30 7h43"/>','control':'<path d="M315 103h82m-82 25h82m-82 25h82"/><circle cx="337" cy="103" r="7"/><circle cx="378" cy="128" r="7"/><circle cx="351" cy="153" r="7"/>','game':'<path d="M317 112h27m-14-13v27"/><circle cx="379" cy="108" r="6"/><circle cx="393" cy="128" r="6"/>','gripper':'<path d="M352 97v28l-28 28m28-28 27 28m-55 0 13 12m42-12-13 12"/>'}.get(spec['output'],'<path d="m310 128 26 25 60-59"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 274" role="img" aria-labelledby="title desc"><title id="title">{esc(p['name'])}: {left} to {right}</title><desc id="desc">Original conceptual workflow illustration, not a screenshot or test result.</desc><rect width="480" height="274" rx="18" fill="{bg}"/><text x="25" y="30" fill="{accent}" font-family="Arial,sans-serif" font-size="11" font-weight="700" letter-spacing="2">{index:02d} / EXPLORE A POSSIBILITY</text><g fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{icon}<rect x="290" y="75" width="130" height="110" rx="10" fill="{soft}"/>{output}</g><path d="M190 129h65m-12-10 12 10-12 10" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><text x="100" y="215" text-anchor="middle" fill="{ink}" font-family="Arial,sans-serif" font-size="15" font-weight="700">{left}</text><text x="355" y="215" text-anchor="middle" fill="{ink}" font-family="Arial,sans-serif" font-size="15" font-weight="700">{right}</text><text x="25" y="251" fill="{accent}" font-family="Arial,sans-serif" font-size="12">{esc(p['name'])}</text></svg>\n'''

def render_readme(projects,c,zh=False):
    projects=[rendered_project(p) for p in projects]
    c={**c,**{key:markdown(c[key]) for key in CONFIG_TEXT}}
    lang='_zh' if zh else '';repo='https://github.com/KeWang0622/'+c['slug'];readme='README.zh-CN.md' if zh else 'README.md'
    out=[f'![{c["title"]} — {c["tagline"]}](assets/cover.png)',f'# {c["title"+lang]}',f'[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Catalog checks]({repo}/actions/workflows/check.yml/badge.svg)]({repo}/actions/workflows/check.yml) [![CC0](https://img.shields.io/badge/catalog-CC0-173e30.svg)](LICENSE)', '[English](README.md) · **简体中文**' if zh else '**English** · [简体中文](README.zh-CN.md)',f'**{c["tagline"+lang]}**\n\n{c["description"+lang]}']
    counts={s:sum(p['status']==s for p in projects) for s in STATUS}
    numbers=' · '.join(f'{n} {(STATUS_ZH if zh else STATUS)[s]}' for s,n in counts.items() if n)
    out.append((f'**{len(projects)} 个项目 · {len(c["categories"])} 个类别** — {numbers}。' if zh else f'**{len(projects)} projects · {len(c["categories"])} categories** — {numbers}.'))
    out.append('[完整步骤与限制](docs/catalog.md) · [如何选择](docs/choose.md) · [竞品与选题依据](docs/landscape.md) · [离线搜索](docs/tooling.md) · [参与贡献](CONTRIBUTING.md)' if zh else '[Setup notes](docs/catalog.md) · [Choose a starting point](docs/choose.md) · [Research & related work](docs/landscape.md) · [Offline search](docs/tooling.md) · [Contribute](CONTRIBUTING.md)')
    out.append('封面和卡片是原创概念插画，不是实拍或测试证据。本项目核查了公开资料，尚未实测这些设备或操作。每条项目均链接原始来源；具体型号、系统版本和上游限制以详情为准。' if zh else 'Cover and cards are original conceptual illustrations, not screenshots or test evidence. This catalog reviews published sources; we have not independently tested the listed setups. Every entry links its primary evidence and setup limits.')
    out.append('## 六个值得先看的玩法' if zh else '## Six places to start')
    lookup={p['id']:p for p in projects};cells=[]
    for spec in c['spotlights']:
        p=lookup[spec['id']];target='docs/catalog.md#'+p['id']
        cells.append(f'[![{p["name"]}: {p["outcome"]}](assets/{p["id"]}.svg)]({target})<br>**[{p["name"]}]({target})**<br>{p["outcome"+lang]}<br>*{(STATUS_ZH if zh else STATUS)[p["status"]]}*<br>{"需要" if zh else "Needs"}: {p["requirements"][0]}')
    # GitHub's automatic Markdown table sizing otherwise gives long captions
    # wider columns and makes identically sized illustrations appear unequal.
    rows=[]
    for i in range(0,6,2):
        row='\n'.join('<td width="50%" valign="top">\n\n'+cell+'\n\n</td>' for cell in cells[i:i+2])
        rows.append('<tr>\n'+row+'\n</tr>')
    out.append('<table width="100%">\n'+'\n'.join(rows)+'\n</table>')
    out.append('## 目录' if zh else '## Explore the collection')
    out.append(' · '.join(f'[{markdown(x["name_zh" if zh else "name"])}](#{x["id"]})' for x in c['categories']))
    for cat in c['categories']:
        out.append(f'<a id="{cat["id"]}"></a>\n\n## {markdown(cat["name_zh" if zh else "name"])}\n\n{markdown(cat["description_zh" if zh else "description"])}')
        lines=[]
        for p in projects:
            if p['category']!=cat['name']:continue
            links=f'[{"来源" if zh else "Evidence"}]({p["evidence_url"]}) · [{"配置与限制" if zh else "Setup & limits"}](docs/catalog.md#{p["id"]})'
            lines.append(f'- **[{p["name"]}]({p["url"]})** — {p["summary"+lang]} *{(STATUS_ZH if zh else STATUS)[p["status"]]}* · {links}.')
        out.append('\n'.join(lines))
    out.append('## 收录标准' if zh else '## Curation, not a compatibility promise')
    out.append('我们收录有明确用途、原始证据和可解释条件的项目。研究演示、归档项目和可安装软件分别标注；源码公开不等于具备开源许可证。日期表示资料核查时间，不代表实测通过。欢迎通过 [Issue](https://github.com/KeWang0622/'+c['slug']+'/issues/new/choose) 补充兼容性结果。\n\n目录正文与原创示意图采用 [CC0](LICENSE)，脚本采用 [MIT](LICENSE-CODE)。外部项目保留各自许可证。详见 [研究方法](docs/methodology.md)、[图片来源](assets/README.md) 和 [测试记录](docs/testing.md)。' if zh else 'Entries need a concrete outcome, primary evidence and explicit requirements. Research demonstrations, archived projects and installable software are labeled separately. Public source does not automatically mean an open-source license. Review dates record source inspection, not successful device tests.\n\nOriginal catalog prose and diagrams: [CC0](LICENSE). Scripts: [MIT](LICENSE-CODE). Linked projects keep their licenses. Read the [method](docs/methodology.md), [visual credits](assets/README.md), [testing protocol](docs/testing.md), and [contribution guide](CONTRIBUTING.md).')
    out.append(f'**Source review / 资料核查：{max(p["checked_at"] for p in projects)}** · [Machine-readable catalog](data/projects.json) · [Changelog](CHANGELOG.md)')
    out.append(c['sibling'])
    return '\n\n'.join(out)+'\n'

def render_details(projects,c):
    projects=[rendered_project(p) for p in projects]
    out=[f'# {markdown(c["title"])}: setup notes','[Back to the illustrated collection](../README.md) · [中文入口](../README.zh-CN.md)', 'These are brief, source-derived routes into each project, not substitute installation manuals or executed test reports. Follow the linked upstream instructions for the exact version and device.']
    for cat in c['categories']:
        out.append('## '+markdown(cat['name']))
        for p in projects:
            if p['category']!=cat['name']:continue
            out.append(f'<a id="{p["id"]}"></a>\n\n### {p["name"]}\n\n**{p["outcome"]}** · {STATUS[p["status"]]} · Source reviewed {p["checked_at"]}')
            if p['id'] in {x['id'] for x in c['spotlights']}:out.append(f'![Conceptual workflow for {p["name"]}](../assets/{p["id"]}.svg)')
            out.append('**Device / input:** '+ '; '.join(p['devices'])+'\n\n**You need:** '+ '; '.join(p['requirements']))
            out.append('\n'.join(f'{i}. {s}' for i,s in enumerate(p['steps'],1)))
            out.append('**Limits:** '+' '.join(p['limitations']))
            links=f'[Project]({p["url"]}) · [Primary evidence]({p["evidence_url"]})'
            if p.get('source_url'):links+=f' · [Source code]({p["source_url"]})'
            if p.get('media_url'):links+=f' · [Upstream visual / demo]({p["media_url"]})'
            out.append(links)
            out.append('**Evidence:** '+p['evidence_note'])
            if p.get('media_url'):out.append('**Visual credit / context:** '+p['media_note'])
    return '\n\n'.join(out)+'\n'

def project_schema(config):
    """Structural schema; cross-record and environmental checks stay in validate."""
    validate_config(config)
    text={'type':'string','minLength':1,'pattern':TEXT_PATTERN}
    url={'type':'string','format':'uri','pattern':r'^https://[^\s<>"\\()]+$'}
    properties={key:dict(text) for key in REQUIRED|OPTIONAL}
    for key in ('devices','requirements','limitations','steps'):
        properties[key]={'type':'array','minItems':1,'items':dict(text)}
    for key in ('url','evidence_url','source_url','media_url'):properties[key]=dict(url)
    properties['id']={'type':'string','pattern':'^'+ID_PATTERN+'$'}
    properties['status']={'type':'string','enum':list(STATUS)}
    properties['category']={'type':'string','enum':[x['name'] for x in config['categories']]}
    properties['checked_at']={'type':'string','format':'date','pattern':r'^\d{4}-\d{2}-\d{2}$'}
    properties['spotlight']={'type':'boolean'}
    return {
        '$schema':'https://json-schema.org/draft/2020-12/schema',
        'title':config['title']+' project catalog',
        '$comment':'Runtime validation additionally checks calendar validity and future dates, URL hostname/IP/port rules, canonical duplicate IDs/names/URLs, configured spotlight references, nonempty categories, and category/name order. JSON Schema format assertions depend on the consumer. Config is validated separately by catalog.py.',
        'type':'array','minItems':1,
        'items':{'type':'object','required':sorted(REQUIRED),'additionalProperties':False,
                 'properties':dict(sorted(properties.items())),
                 'dependentRequired':{'media_url':['media_note']}}
    }

def outputs(projects,c):
    result={'README.md':render_readme(projects,c),'README.zh-CN.md':render_readme(projects,c,True),'docs/catalog.md':render_details(projects,c)}
    lookup={p['id']:p for p in projects}
    for i,spec in enumerate(c['spotlights'],1):result[f'assets/{spec["id"]}.svg']=card(lookup[spec['id']],spec,i,c['theme'])
    result['data/summary.json']=json.dumps({'projects':len(projects),'categories':len(c['categories']),'status':{s:sum(p['status']==s for p in projects) for s in STATUS},'latest_source_review':max(p['checked_at'] for p in projects),'independently_tested_setups':0},indent=2)+'\n'
    result['data/schema.json']=json.dumps(project_schema(c),ensure_ascii=False,indent=2)+'\n'
    return result

def strip_fences(text):
    out=[];fence=None
    for line in text.splitlines():
        m=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',line)
        if fence:
            if m and m[1][0]==fence[0] and len(m[1])>=len(fence) and not m[2].strip():fence=None
        elif m:fence=m[1]
        else:out.append(line)
    return '\n'.join(out)

def anchors(text):
    text=strip_fences(text);out=set(re.findall(r'<a id="([^"]+)"',text));seen={}
    for title in re.findall(r'^#{1,6} (.+)$',text,re.M):
        key=slug(title);n=seen.get(key,0);out.add(key if not n else f'{key}-{n}');seen[key]=n+1
    return out

def local_links(root):
    # Supported Markdown destinations include optional titles and angle brackets.
    inline=re.compile(r'''\]\(\s*(?:<([^<>\n]+)>|((?:\\.|[^\s()\\]|\([^()\n]*\))+))(?:\s+(?:"[^"\n]*"|'[^'\n]*'|\([^()\n]*\)))?\s*\)''')
    definition=re.compile(r'^ {0,3}\[([^\]]+)\]:\s*(?:<([^<>\n]+)>|(\S+))',re.M)
    def ref_key(value):return ' '.join(value.split()).casefold()
    for file in root.rglob('*.md'):
        if '.git' in file.parts:continue
        text=strip_fences(file.read_text(encoding='utf-8'))
        text=re.sub(r'(`+)(.*?)\1','',text,flags=re.S)
        refs={ref_key(k):(angle or bare) for k,angle,bare in definition.findall(text)}
        for label,key in re.findall(r'\[([^\]]+)\]\[([^\]]*)\]',text):need(ref_key(key or label) in refs,f'Undefined reference: {file}:{key}')
        destinations=[angle or bare for angle,bare in inline.findall(text)]+list(refs.values())
        for dest in destinations:
            dest=re.sub(r'\\([!"#$%&\'()*+,\-./:;<=>?@\[\]\\^_`{|}~])',r'\1',dest)
            parsed=urlsplit(dest)
            if parsed.scheme or parsed.netloc:continue
            path,frag=unquote(parsed.path),unquote(parsed.fragment)
            target=(file.parent/path).resolve() if path else file.resolve()
            need(target.is_relative_to(root.resolve()),f'Local link escapes repository: {dest}')
            need(target.exists(),f'Broken local link: {file}:{dest}')
            if frag and target.suffix=='.md':need(frag in anchors(target.read_text(encoding='utf-8')),f'Broken anchor: {file}:{dest}')

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',choices=['build','check','search']);parser.add_argument('query',nargs='?',default='');parser.add_argument('--status',choices=STATUS);parser.add_argument('--category');parser.add_argument('--json',action='store_true');args=parser.parse_args()
    try:
        projects,c=load()
        if args.command=='search':
            if args.category:need(args.category in {x['name'] for x in c['categories']},'Unknown category')
            matches=find(projects,args.query,args.status,args.category)
            if args.json:print(json.dumps(matches,ensure_ascii=False,indent=2))
            else:
                print(f'{len(matches)} matches')
                for p in matches:print(f'\n{p["name"]} [{STATUS[p["status"]]}]\n  {p["summary"]}\n  Needs: {"; ".join(p["requirements"])}\n  {p["url"]}')
        elif args.command=='build':
            for name,body in outputs(projects,c).items():
                path=ROOT/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body,encoding='utf-8')
            print(f'Built {len(projects)} projects, two READMEs and six illustrated cards')
        else:
            for name,body in outputs(projects,c).items():need((ROOT/name).read_text(encoding='utf-8')==body,f'Stale generated file: {name}')
            local_links(ROOT)
            import xml.etree.ElementTree as ET
            for path in (ROOT/'assets').glob('*.svg'):
                tree=ET.parse(path);need(not any(el.tag.rsplit('}',1)[-1] in ('script','foreignObject') for el in tree.iter()),f'Unexpected SVG content: {path}')
            print(f'OK: {len(projects)} projects; evidence fields, URL syntax, identities, status, dates, generated docs/schema, SVGs and local links (no remote availability or device tests)')
    except (CatalogError,ValueError,OSError,KeyError) as error:raise SystemExit(str(error)) from error

if __name__=='__main__':main()
