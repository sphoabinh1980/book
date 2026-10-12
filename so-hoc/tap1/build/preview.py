#!/usr/bin/env python3
"""Xem trước một (vài) chương: dựng .docx chỉ gồm các chương đó, chuyển sang PDF, ghép ảnh các trang để xem nhanh.
Cách dùng: python3 build/preview.py 2            (chương 2)
           python3 build/preview.py 2 --pages 5-12 --dpi 70
Kết quả: /tmp/claude-0/preview_ch2/ (file .pdf và các ảnh ghép sheet_k.png, mỗi ảnh 8 trang)."""
import glob, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
sys.path.insert(0, glob.glob('/root/.claude/skills/synced/*/docx/scripts')[0])
from office.soffice import run_soffice
args = sys.argv[1:]; ch = args[0]
dpi = int(args[args.index('--dpi') + 1]) if '--dpi' in args else 45
out = f'/tmp/claude-0/preview_ch{ch.replace(",", "_")}'; os.makedirs(out, exist_ok=True)
for f in glob.glob(out + '/*'): os.remove(f)
subprocess.run([sys.executable, os.path.join(HERE, 'run_examples.py')], check=True)
docx = os.path.join(out, 'preview.docx')
subprocess.run(['node', os.path.join(HERE, 'build.js'), docx], check=True, env={**os.environ, 'CHAPTERS': ch})
run_soffice(['--headless', '--convert-to', 'pdf', '--outdir', out, docx], check=True, capture_output=True, timeout=900)
pdf = os.path.join(out, 'preview.pdf')
cmd = ['pdftoppm', '-r', str(dpi), '-png']
if '--pages' in args:
    a, b = args[args.index('--pages') + 1].split('-'); cmd += ['-f', a, '-l', b]
subprocess.run(cmd + [pdf, os.path.join(out, 'p')], check=True)
from PIL import Image
fs = sorted(glob.glob(out + '/p-*.png')); ims = [Image.open(f) for f in fs]
W, H = ims[0].width, ims[0].height
for k in range(0, len(ims), 8):
    c = Image.new('RGB', (W * 4, H * 2), 'white')
    for j, im in enumerate(ims[k:k + 8]): c.paste(im, ((j % 4) * W, (j // 4) * H))
    c.save(os.path.join(out, f'sheet_{k // 8}.png'))
n = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
print(out, [l for l in n.split('\n') if l.startswith('Pages')][0])
