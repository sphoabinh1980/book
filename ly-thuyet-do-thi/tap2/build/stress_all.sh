#!/bin/bash
# Đối chiếu mọi lời giải mẫu với chương trình trâu / chương trình chấm trên test ngẫu nhiên nhỏ
set -e
cd "$(dirname "$0")/../verify"
N=${1:-300}
for c in BATTAY NOITIENG TAMGIAC CHUYENDOI BANCHUNG BANDO DEMDAO CAYKHONG DUPHONG MADITUAN CHAYTRON CHIADOI; do python3 run.py ch1 $c $N; done
for c in DUONGTRUONG NUTGIAO XEBUYT DOITIEN BAYRE LICHTHIDAU THUDO XEPHANG XETAI DENGIAOTHONG PHATUONG ROBOTXOAY; do python3 run.py ch2 $c $N; done
for c in MANGBANBE PHACAU HAIPHE NOIMANG ITDOC GIENGONG HOHANG CAPQUANG CAPK; do python3 run.py ch3 $c $N; done
for c in XHGIAIDAU XAYNHA DEMLOTRINH HUYETMACH BIENAP CAPDUPHONG TINDON KHOBAU TUYENCHON NETVE DOMINO KETSAT; do python3 run.py ch4 $c $N; done
for c in XEPPHONG DATDOMINO CAMERA DUONGONG ROINHAU TRUCNHAT; do python3 run.py ch5 $c $N; done
