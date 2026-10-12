#!/usr/bin/env python3
"""Dựng sách hai lượt: lượt 1 dựng thử và đo số trang từng mục, lượt 2 điền số trang vào mục lục.
Cách dùng: python3 paginate.py <thư mục đầu ra>"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(sys.argv[1])
NAME = 'SH_2_BaiTap'
SOFFICE = '/root/.claude/skills/synced/ab1e3a82-3639-402f-9bd8-ae47514e93b9_d3ad1bb1-93c0-40c8-942c-aa5bd6863b3a/docx/scripts/office/soffice.py'
os.makedirs(OUT, exist_ok=True)
docx = os.path.join(OUT, NAME + '.docx'); pdf = os.path.join(OUT, NAME + '.pdf')

def build_and_render():
    subprocess.run(['node', os.path.join(HERE, 'build.js'), docx], check=True)
    if os.path.exists(pdf): os.remove(pdf)
    subprocess.run(['python3', SOFFICE, '--headless', '--convert-to', 'pdf', '--outdir', OUT, docx], check=True, capture_output=True, timeout=1200)
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    pages = [subprocess.run(['pdftotext', '-layout', '-f', str(i), '-l', str(i), pdf, '-'], capture_output=True, text=True).stdout for i in range(1, n + 1)]
    return pages

targets = json.loads(subprocess.run(['node', os.path.join(HERE, 'targets.js')], capture_output=True, text=True, check=True).stdout)
pj = os.path.join(HERE, 'pages.json')
prev = None
for it in range(4):
    pages = build_and_render()
    found = {}
    for t in targets:
        for i, txt in enumerate(pages, 1):
            flat = re.sub(r'\s+', ' ', txt)
            if re.search(t['re'], flat) and (not t.get('also') or re.search(t['also'], flat)):
                found[t['key']] = i; break
        else:
            print('KHÔNG TÌM THẤY', t)
    print(f'lượt {it + 1}: {len(pages)} trang')
    if found == prev: break
    json.dump(found, open(pj, 'w'), ensure_ascii=False, indent=0)
    prev = found
print('xong', docx)
