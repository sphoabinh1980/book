#!/bin/bash
# render.sh in.docx outdir  -> PDF + ảnh trang
set -e
OUT=$2; mkdir -p $OUT; rm -f $OUT/*.jpg
cd $OUT && timeout 900 python /root/.claude/skills/synced/ab1e3a82-3639-402f-9bd8-ae47514e93b9_d3ad1bb1-93c0-40c8-942c-aa5bd6863b3a/docx/scripts/office/soffice.py --headless --convert-to pdf $1 >/dev/null 2>&1
B=$(basename $1 .docx); pdfinfo $B.pdf | grep Pages
pdftoppm -jpeg -r ${3:-60} $B.pdf p
python3 - <<'PY'
from PIL import Image
import glob
fs=sorted(glob.glob('p-*.jpg')); ims=[Image.open(f) for f in fs]; w,h=ims[0].size
for k in range(0,len(ims),6):
    g=Image.new('RGB',(w*3,h*2),'white')
    for i,im in enumerate(ims[k:k+6]): g.paste(im,((i%3)*w,(i//3)*h))
    g.save(f'sheet{k//6:02d}.jpg')
PY
