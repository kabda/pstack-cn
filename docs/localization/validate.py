#!/usr/bin/env python3
"""离线核验固定基线；不安装依赖、不执行插件、不更新测试预期。"""
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
import argparse
import hashlib
import json
import os
import re
import subprocess
import unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
RECORDS = ROOT / 'docs/localization'
MANIFEST = json.loads((RECORDS / 'MANIFEST.json').read_text())
SOURCE = Path('/Users/zxj/Developer/open-source/pstack')
SHA = MANIFEST['source_commit']
TICK = chr(96)


def git(*args):
    return subprocess.check_output(['git', '-C', str(SOURCE), *args])


def blob(row):
    return git('cat-file', 'blob', row['source_object'])


def unfenced(text):
    out, fence = [], None
    for line in text.splitlines():
        match = re.match(r'^\s*(' + TICK + r'{3,}|~{3,})', line)
        if match:
            mark = match[1]
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            out.append('')
        else:
            out.append('' if fence else line)
    return '\n'.join(out), fence


def slug(text):
    text = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'\[([^\]]*)\]\[[^\]]*\]', r'\1', text)
    text = re.sub(r'<[^>]+>', '', text).replace(TICK, '').strip().lower()
    text = ''.join(c for c in text if c.isalnum() or c in '_- ' or unicodedata.category(c).startswith('M'))
    return text.replace(' ', '-')


def anchors(text):
    text, _ = unfenced(text)
    result = set(re.findall(r'\b(?:id|name)=[\"\']([^\"\']+)', text))
    counts = Counter()
    for line in text.splitlines():
        m = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if m:
            key = slug(m[1]); n = counts[key]; counts[key] += 1
            result.add(key + ('-' + str(n) if n else ''))
    return result


def links(text):
    text, _ = unfenced(text)
    # 行内代码中的示例链接不属于文档链接；链接标签内的代码则只去包装内容。
    text = re.sub(r'(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)', '', text, flags=re.S)
    found = []
    for m in re.finditer(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+[\"\'][^\n]*?[\"\'])?\)', text):
        found.append(m[1].strip('<>'))
    found += re.findall(r'^\s*\[[^\]]+\]:\s*<?([^\s>]+)', text, re.M)
    found += re.findall(r'\b(?:href|src)=[\"\']([^\"\']+)', text)
    for srcset in re.findall(r'\bsrcset=[\"\']([^\"\']+)', text):
        found += [part.strip().split()[0] for part in srcset.split(',') if part.strip()]
    return found


def link_problems(contents):
    from urllib.parse import unquote
    issues = set()
    for path, text in contents.items():
        if not path.endswith(('.md', '.html', '.svg')):
            continue
        for link in links(text):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('//'):
                continue
            base, _, fragment = unquote(link).partition('#')
            base = base.split('?')[0]
            target = os.path.normpath(str(Path(path).parent / base)) if base else path
            if target.startswith('/') or target.startswith('../'):
                issues.add((path, link, '超出镜像范围'))
            elif target not in contents and not any(p.startswith(target.rstrip('/') + '/') for p in contents):
                issues.add((path, link, '文件缺失'))
            elif fragment and target in contents and target.endswith(('.md', '.html', '.svg')):
                if fragment not in anchors(contents[target]):
                    issues.add((path, link, '锚点缺失'))
    return issues


class HTMLCheck(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.errors.append('闭合标签不匹配: ' + tag)


def svg_structure(node, parent_human=False):
    tag = node.tag.rsplit('}', 1)[-1]
    human = tag in {'text', 'tspan', 'title', 'desc'}
    attributes = tuple(sorted((k, '<已审校自然语言>' if k in {'aria-label', 'title'} else v) for k, v in node.attrib.items()))
    return (node.tag, attributes, '<已审校自然语言>' if human else node.text,
            tuple(svg_structure(child, human) for child in node),
            '<已审校自然语言>' if parent_human else node.tail)


def angle_tokens(text):
    html_tags = {'a', 'abbr', 'b', 'blockquote', 'br', 'code', 'details', 'div', 'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img', 'li', 'ol', 'p', 'picture', 'pre', 'section', 'source', 'span', 'strong', 'style', 'summary', 'table', 'tbody', 'td', 'th', 'thead', 'tr', 'ul'}
    # 在代码围栏和行内代码里，即使名字与 HTML 标签相同也是精确字面量。
    result = []
    for block in code_fences(text):
        result.extend(re.findall(r'<[^<>\n]+>', block['body']))
    text, _ = unfenced(text)
    span = TICK + r'([^' + TICK + r'\n]+)' + TICK
    for literal in re.findall(span, text):
        result.extend(re.findall(r'<[^<>\n]+>', literal))
    text = re.sub(span, '', text)
    for match in re.finditer(r'<([^<>\n]+)>', text):
        body = match[1].strip()
        first = body.lstrip('/').split()[0].lower() if body else ''
        if first in html_tags or body.startswith(('!--', 'http:', 'https:')):
            continue
        result.append(match[0])
    return Counter(result)


def code_fences(text):
    result, opening, body = [], None, []
    for line in text.splitlines():
        if opening:
            close = re.match(r'^ {0,3}(' + re.escape(opening[0]) + r'+)[ \t]*$', line)
            if close and len(close[1]) >= opening[1]:
                result.append({'language': opening[2], 'body': '\n'.join(body)})
                opening, body = None, []
            else:
                body.append(line)
        else:
            match = re.match(r'^ {0,3}(' + TICK + r'{3,}|~{3,})(.*)$', line)
            if match and not (match[1][0] == TICK and TICK in match[2]):
                opening = (match[1][0], len(match[1]), match[2].strip())
    return result


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def without_js_comments(text):
    """针对已审阅的 TS 示例，保护字符串和类型，仅移除说明注释。"""
    out, i, quote = [], 0, None
    while i < len(text):
        char = text[i]
        if quote:
            out.append(char)
            if char == '\\' and i + 1 < len(text):
                out.append(text[i + 1]); i += 2; continue
            if char == quote:
                quote = None
            i += 1; continue
        if char in {'"', "'", TICK}:
            quote = char; out.append(char); i += 1; continue
        if text.startswith('//', i):
            end = text.find('\n', i); i = len(text) if end < 0 else end; continue
        if text.startswith('/*', i):
            end = text.find('*/', i + 2)
            if end < 0:
                raise ValueError('未闭合块注释')
            i = end + 2; continue
        out.append(char); i += 1
    return ''.join(out)


def compare_literal(path, language, a, b):
    """重算混合示例中的机器部分，不依赖历史 passed 标记。"""
    if path == 'skills/typescript-best-practices/references/patterns.md':
        return 'TS 示例去注释后完整文本相同', without_js_comments(a) == without_js_comments(b)
    if language == 'mermaid':
        def graph(text):
            text = re.sub(r'\[[^\]\n]*\]', '[]', text)
            text = re.sub(r'\{[^}\n]*\}', '{}', text)
            text = re.sub(r'\|[^|\n]*\|', '||', text)
            return re.sub(r'\s+', '', text)
        return 'Mermaid 去展示标签后节点/边/语法相同', graph(a) == graph(b)
    if path == 'skills/why/references/sources/code-archaeology.md':
        clean = lambda text: '\n'.join(line for line in text.splitlines() if not line.lstrip().startswith('#'))
        return 'Bash 示例非注释文本相同', clean(a) == clean(b)
    if path == 'skills/setup-pstack/SKILL.md':
        clean = lambda text: '\n'.join(line for line in text.splitlines() if not line.startswith('description:') and (not line.startswith('#') or line.startswith('# budget:')))
        return '模型规则模板保护字段及身份行相同', clean(a) == clean(b)
    if path == 'skills/show-me-your-work/SKILL.md':
        aa = [line.split('\t') for line in a.splitlines()]; bb = [line.split('\t') for line in b.splitlines()]
        passed = len(aa) == len(bb) and aa[0] == bb[0]
        passed = passed and all(len(x) == len(y) == 6 and [x[j] for j in [0, 1, 4]] == [y[j] for j in [0, 1, 4]] for x, y in zip(aa[1:], bb[1:]))
        return 'TSV 示例六列结构和机器列相同', passed
    if path.startswith(('skills/why/references/sources/datadog', 'skills/why/references/sources/sentry')):
        names = lambda text: re.findall(r'^\s*([a-z][a-z0-9_]+)', text, re.M)
        return '工具用法示例 API 名和次序相同', names(a) == names(b)
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--final', action='store_true', help='要求所有文件完成且独立审校通过')
    args = parser.parse_args()
    errors, warnings, english, candidates, fenced, numeric, literal_proofs = [], [], [], [], [], [], []
    source, target = {}, {}
    rows = MANIFEST['files']
    tree = {}
    for item in git('ls-tree', '-rz', SHA).split(b'\0'):
        if item:
            meta, path = item.split(b'\t'); mode, kind, obj = meta.decode().split()
            tree[path.decode()] = (mode, kind, obj)
    if set(tree) != {r['path'] for r in rows}:
        errors.append('MANIFEST 与固定基线的路径集合不同')
    comment_file = RECORDS / 'COMMENT-CHANGES.json'
    comments = json.loads(comment_file.read_text()) if comment_file.exists() else []
    config_file = RECORDS / 'CONFIG-CHANGES.json'
    config_changes = json.loads(config_file.read_text()) if config_file.exists() else []
    yaml_documents = []
    for row in rows:
        path = row['path']; dst = ROOT / path
        if tree.get(path) != (row['source_mode'], row['source_type'], row['source_object']):
            errors.append(path + ': Git 树信息不符')
        data = blob(row)
        if hashlib.sha256(data).hexdigest() != row['source_sha256']:
            errors.append(path + ': 固定源哈希不符')
        if not dst.exists() and not dst.is_symlink():
            errors.append(path + ': 目标缺失'); continue
        if row['source_mode'] == '120000':
            actual = os.readlink(dst).encode() if dst.is_symlink() else b''
        else:
            if not dst.is_file() or dst.is_symlink():
                errors.append(path + ': 文件类型不同'); continue
            actual = dst.read_bytes()
            if bool(dst.stat().st_mode & 0o111) != (row['source_mode'] == '100755'):
                errors.append(path + ': 可执行位不同')
        category = row['category']
        if category in {'原样机器内容', '原样许可证', '原样图像'} and actual != data:
            errors.append(path + ': 受保护内容字节变化')
        relevant = [c for c in comments + config_changes if c['path'] == path]
        if relevant:
            expected = data.decode()
            for change in relevant:
                if expected.count(change['source']) != 1:
                    errors.append(path + ': 注释白名单源匹配不唯一')
                expected = expected.replace(change['source'], change['target'], 1)
            if expected.encode() != actual:
                errors.append(path + ': 存在白名单之外的代码变化')
        if args.final:
            required_review = '原样核验通过' if category in {'原样机器内容', '原样许可证', '原样图像'} else '独立审校通过'
            if row['status'] not in {'已翻译', '已保留'} or row['review_status'] != required_review:
                errors.append(path + ': 翻译或审校未完成')
        try:
            s, t = data.decode('utf-8'), actual.decode('utf-8')
        except UnicodeDecodeError:
            source[path] = ''; target[path] = ''; continue
        source[path], target[path] = s, t
        if path.endswith('.json'):
            try:
                sj, tj = json.loads(s), json.loads(t)
                if path in {'plugin.json', '.cursor-plugin/plugin.json'}:
                    sj.pop('description'); desc = tj.pop('description')
                    if sj != tj or not re.search('[\u4e00-\u9fff]', desc):
                        errors.append(path + ': 插件身份字段或 description 异常')
            except Exception as exc:
                errors.append(path + ': JSON 解析失败 ' + str(exc))
        if path.endswith('.svg'):
            try:
                if svg_structure(ET.fromstring(s)) != svg_structure(ET.fromstring(t)):
                    errors.append(path + ': SVG 图形/属性/ID/关系变化')
            except Exception as exc:
                errors.append(path + ': SVG 解析失败 ' + str(exc))
        if path.endswith(('.yaml', '.yml')):
            expected_yaml = s
            for change in config_changes:
                if change['path'] == path:
                    expected_yaml = expected_yaml.replace(change['source'], change['target'], 1)
            yaml_documents.append({'path': path, 'source': expected_yaml, 'target': t, 'whole': True})
        if not path.endswith('.md') or '/scripts/' in path:
            continue
        sf, tf = code_fences(s), code_fences(t)
        if len(sf) != len(tf):
            errors.append(path + ': 代码围栏数量变化，需要人工裁定')
        for number, (a, b) in enumerate(zip(sf, tf), 1):
            if a['language'] != b['language']:
                errors.append(path + ': 代码围栏语言标记变化')
            if a['body'] != b['body']:
                fenced.append({'path': path, 'index': number, 'language': a['language'], 'source_sha256': digest(a['body']), 'target_sha256': digest(b['body']), 'source_preview': a['body'][:160], 'target_preview': b['body'][:160]})
                proof = compare_literal(path, a['language'], a['body'], b['body'])
                if proof:
                    name, passed = proof
                    literal_proofs.append({'path': path, 'index': number, 'check': name, 'passed': passed, 'source_sha256': digest(a['body']), 'target_sha256': digest(b['body'])})
                    if not passed:
                        errors.append(path + ': 混合示例机器部分变化 ' + name)
        numbers = r'\d+(?:[.,]\d+)*'
        missing_numbers = Counter(re.findall(numbers, s)) - Counter(re.findall(numbers, t))
        for value, count in missing_numbers.items():
            numeric.append({'path': path, 'source_number': value, 'count': count})
        if path == 'README.md':
            markers = r'<!-- mirror:(?:start|end).*?-->'
            if re.findall(markers, s, re.S) != re.findall(markers, t, re.S):
                errors.append(path + ': 镜像同步标记变化')
        if s.startswith('---\n'):
            sm, tm = re.match(r'^---\n(.*?)\n---(?:\n|$)', s, re.S), re.match(r'^---\n(.*?)\n---(?:\n|$)', t, re.S)
            if not tm:
                errors.append(path + ': frontmatter 不完整')
            else:
                yaml_documents.append({'path': path, 'source': sm[1], 'target': tm[1], 'whole': False})
        _, fence = unfenced(t)
        if fence:
            errors.append(path + ': 代码围栏未闭合')
        # 精确占位符只从源中提取；HTML 标签不是占位符。
        patterns = [r'\$\{[^\n}]+\}', r'\{\{[^\n}]+\}\}', r'\[benny:[a-z]+\]', r'(?<!\{)\{[A-Z][A-Z0-9_]*\}(?!\})', r'\$[A-Z_][A-Z0-9_]+']
        for pattern in patterns:
            missing = Counter(re.findall(pattern, s)) - Counter(re.findall(pattern, t))
            if missing:
                errors.append(path + ': 精确占位符或协议标记缺失 ' + repr(dict(missing)))
        missing_angles = angle_tokens(s) - angle_tokens(t)
        if missing_angles:
            errors.append(path + ': 尖括号占位符或代码类型缺失 ' + repr(dict(missing_angles)))
        # 缺失的行内片段进入人工裁定队列，不能自动认定为已保留或已翻译。
        span = TICK + r'([^' + TICK + r'\n]+)' + TICK
        missing = Counter(re.findall(span, s)) - Counter(re.findall(span, t))
        for value, count in missing.items():
            candidates.append({'path': path, 'source_span': value, 'count': count})
        clean, _ = unfenced(t)
        clean = re.sub(span, '', clean)
        clean = re.sub(r'<[^>]*>', '', clean)
        for number, line in enumerate(clean.splitlines(), 1):
            if re.search('[\u4e00-\u9fff]', line) or re.match(r'^(?:name|model|color|tools|skills|disable-model-invocation):', line):
                continue
            line = re.sub(r'https?://\S+', '', line)
            if len(re.findall(r'[A-Za-z]{2,}', line)) >= 4:
                english.append({'path': path, 'line': number, 'text': line.strip()})
    # 使用宿主已有 Ruby/Psych 解析 YAML，不安装依赖。
    ruby = '''require 'json'; require 'yaml'; input=JSON.parse(STDIN.read); errors=[]; input.each do |d|; begin; a=YAML.safe_load(d['source'], aliases: true); b=YAML.safe_load(d['target'], aliases: true); if d['whole']; errors << d['path']+': YAML 数据变化' unless a==b; else; a.delete('description'); v=b.delete('description'); errors << d['path']+': frontmatter 机器字段变化' unless a==b; errors << d['path']+': description 缺少中文' unless v.is_a?(String) && v.match?(/[一-鿿]/); end; rescue => e; errors << d['path']+': '+e.message; end; end; puts JSON.generate(errors)'''
    proc = subprocess.run(['ruby', '-e', ruby], input=json.dumps(yaml_documents), capture_output=True, text=True)
    if proc.returncode:
        errors.append('YAML 解析器失败: ' + proc.stderr)
    else:
        errors.extend(json.loads(proc.stdout))
    known = set(tree)
    for dst in ROOT.rglob('*'):
        path = str(dst.relative_to(ROOT))
        if path == '.git' or path.startswith('.git/') or not dst.is_file():
            continue
        if path not in known and not path.startswith(('docs/localization/', 'wiki/')):
            errors.append(path + ': 新增路径越界')
        if path.endswith('.html'):
            text = dst.read_text(); check = HTMLCheck(); check.feed(text)
            errors.extend(path + ': ' + e for e in check.errors)
            if check.stack:
                errors.append(path + ': HTML 标签未闭合 ' + repr(check.stack))
            target[path] = text
        elif path.endswith('.md') and path not in known:
            target[path] = dst.read_text()
        elif path.endswith('.json') and path not in known:
            try:
                json.loads(dst.read_text())
            except Exception as exc:
                errors.append(path + ': 新增 JSON 解析失败 ' + str(exc))
    # 使用已安装 Bun 的 Markdown 解析器核验全文；不安装依赖。
    markdown = [{'path': p, 'text': t} for p, t in target.items() if p.endswith('.md')]
    js = '''const rows = await Bun.stdin.json(); const errors = []; for (const row of rows) { try { const html = Bun.markdown.html(row.text); if (typeof html !== 'string') throw new Error('没有生成 HTML'); } catch (e) { errors.push(row.path + ': ' + e.message); } } console.log(JSON.stringify({count: rows.length, errors}));'''
    parsed = subprocess.run(['bun', '-e', js], input=json.dumps(markdown), capture_output=True, text=True)
    markdown_count = 0
    if parsed.returncode:
        errors.append('Markdown 解析器失败: ' + parsed.stderr)
    else:
        result = json.loads(parsed.stdout); markdown_count = result['count']; errors.extend(result['errors'])
    baseline_links = link_problems(source)
    current_links = link_problems(target)
    introduced = current_links - baseline_links
    errors.extend(path + ': 新增失效引用 ' + link + ' (' + reason + ')' for path, link, reason in sorted(introduced))
    if args.final:
        review_index = {}
        for review_file in RECORDS.glob('REVIEW-*.json'):
            review = json.loads(review_file.read_text())
            if not isinstance(review, dict):
                continue
            if review.get('open_issues') or review.get('unresolved_issues'):
                errors.append(review_file.name + ': 仍有未决审校项')
            if review.get('source_commit') != SHA:
                errors.append(review_file.name + ': 审校基线不同')
            for item in review.get('files', review.get('reviewed_files', [])):
                if not isinstance(item, dict) or 'path' not in item:
                    continue
                if item.get('open_issues') or item.get('unresolved_issues'):
                    errors.append(item['path'] + ': 仍有未决审校项')
                    continue
                independent = item.get('independent', review.get('independent', False))
                reviewer = item.get('reviewer', review.get('reviewer'))
                translator = item.get('initial_translator', review.get('initial_translator'))
                status = item.get('review_status', item.get('result', item.get('status', review.get('review_status', review.get('status')))))
                approved = status in {'通过', '逐段源译对照通过', '独立全文源译对照通过', '原样保留，中文解读通过'}
                if independent and reviewer and translator and reviewer != translator and approved:
                    review_index[item['path']] = item
        for row in rows:
            path = row['path']; dst = ROOT / path
            if dst.is_file() and row['category'] not in {'原样机器内容', '原样许可证', '原样图像'}:
                review = review_index.get(path)
                if not review or review.get('target_sha256') != hashlib.sha256(dst.read_bytes()).hexdigest():
                    errors.append(path + ': 缺少当前哈希的独立审校证明')
            if dst.is_file() and row.get('target_sha256') != hashlib.sha256(dst.read_bytes()).hexdigest():
                errors.append(path + ': 清单目标哈希未锁定或发生漂移')
        wiki = ROOT / 'wiki/index.html'
        if not wiki.exists() or review_index.get('wiki/index.html', {}).get('target_sha256') != hashlib.sha256(wiki.read_bytes()).hexdigest():
            errors.append('wiki/index.html: 缺少当前哈希的独立审校证明')
        decisions_file = RECORDS / 'LITERAL-REVIEW.json'
        if not decisions_file.exists():
            errors.append('缺少英文和混合片段逐项裁定记录')
        else:
            decisions = json.loads(decisions_file.read_text())
            if decisions.get('source_commit') != SHA:
                errors.append('LITERAL-REVIEW.json: 裁定基线不同')
            groups = {'english': english, 'inline': candidates, 'fences': fenced, 'numbers': numeric}
            for kind, items in groups.items():
                expected = decisions.get(kind, [])
                for item in items:
                    key = {k: v for k, v in item.items() if k not in {'line', 'source_preview', 'target_preview'}}
                    match = next((x for x in expected if x.get('candidate') == key and x.get('reason') and x.get('status') == '已裁定'), None)
                    if not match:
                        errors.append(item['path'] + ': 存在未裁定或已漂移的 ' + kind + ' 片段')
    report = {'source_commit': SHA, 'final_mode': args.final, 'baseline_files': len(rows), 'markdown_parsed': markdown_count, 'errors': errors, 'warnings': warnings, 'baseline_link_problems': sorted(baseline_links), 'new_link_problems': sorted(introduced), 'english_candidates': english, 'inline_span_candidates': candidates, 'changed_fence_candidates': fenced, 'numeric_candidates': numeric}
    (RECORDS / 'CHECK-RESULTS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (RECORDS / 'LITERAL-PROOFS.json').write_text(json.dumps({'source_commit': SHA, 'checks': literal_proofs, 'scope': '每次运行均从固定源对象和目标重新比较；不是完整语言编译或真实工作流执行。'}, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'基线文件': len(rows), '错误': len(errors), '基线引用问题': len(baseline_links), '英文待裁定行': len(english), '行内片段待裁定': len(candidates)}, ensure_ascii=False))
    for err in errors[:30]:
        print(err)
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
