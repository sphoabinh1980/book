# -*- coding: utf-8 -*-
"""XEPDEU / CODEPLUS - Manim Community, 9:16.

Math renderer uses separate baseline/superscript/subscript Text objects.
No MathTex, XeLaTeX, Emoji or unescaped raw ^/_ in displayed formulas.
Expected Manim Community >= 0.18.
"""
from manim import *
from pathlib import Path
from contextlib import contextmanager
import json
import os
import re

PREVIEW = os.getenv("NP_PREVIEW", "0") == "1"
config.pixel_width = 540 if PREVIEW else 1080
config.pixel_height = 960 if PREVIEW else 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.background_color = "#FFFFFF"

C = -0.48
LEFT_EDGE = -3.95
RIGHT_EDGE = 2.99
SAFE_TOP = 6.90
SAFE_BOTTOM = -3.80
STAGE_TOP = 6.10
STAGE_BOTTOM = -1.32
NOTE_Y = -2.05

INK = "#111827"
SUB = "#475569"
BLUE = "#2563EB"
GREEN = "#15803D"
RED = "#DC2626"
ORANGE = "#EA580C"
PURPLE = "#7C3AED"
TEAL = "#0E7490"
GOLD = "#B45309"
PALE_BLUE = "#EFF6FF"
PALE_GREEN = "#F0FDF4"
PALE_RED = "#FEF2F2"
PALE_ORANGE = "#FFF7ED"
PALE_PURPLE = "#F5F3FF"
GRAY_BG = "#F8FAFC"
BORDER = "#CBD5E1"
WHITE = "#FFFFFF"
# Prefer the same Vietnamese font as the HINHVUONG reference where available.
# Never bundle third-party font files: use installed font families on the PC.
try:
    from manimpango import list_fonts
    _fonts = set(list_fonts())
except Exception:
    _fonts = set()

def choose_font(candidates, fallback):
    return next((font for font in candidates if font in _fonts), fallback)

FONT = choose_font(["Be Vietnam Pro", "Inter", "Noto Sans", "Arial", "DejaVu Sans"], "DejaVu Sans")
MONO = choose_font(["JetBrains Mono", "Consolas", "DejaVu Sans Mono", "Courier New"], "DejaVu Sans Mono")
FALLBACK = choose_font(["DejaVu Sans", "Cambria Math", "Segoe UI Symbol", "Arial"], "DejaVu Sans")

# Superscripts and subscripts have to be explicit, not glyph substitutions.
# This prevents 10^9, a_i, g_j, k^n from being displayed on the baseline.
SCRIPT = re.compile(r"([_^])\{([^{}]+)\}")


def t(s, size=27, color=INK, bold=False, font=FONT):
    s = str(s)
    # t2f is per-character; Vietnamese stays in Inter, operators use DejaVu.
    fallback = {ch: FALLBACK for ch in "≤≥≠⇒→←×÷∑√∞✓✗" if ch in s}
    return Text(s, font=font, font_size=size, color=color,
                weight=BOLD if bold else NORMAL, disable_ligatures=True,
                t2f=fallback)


def m(s, size=30, color=INK, bold=False):
    """Build mathematical labels with real positioned super- and subscripts.
    Example: m('n = 20, k = 3: 3^{20} = 3 486 784 401').
    """
    parts = VGroup()
    x = 0.0
    last_base = None
    p = 0
    for match in SCRIPT.finditer(s):
        normal = s[p:match.start()]
        if normal:
            q = t(normal, size, color, bold)
            q.move_to([x + q.width / 2, 0, 0])
            parts.add(q)
            x = q.get_right()[0] + 0.015
            last_base = q
        kind, contents = match.group(1), match.group(2)
        if last_base is None:
            raise ValueError("Missing base before superscript/subscript: " + s)
        small = t(contents, int(size * .69), color, bold)
        # Anchor glyph rather than mathematical Unicode superscript.
        dy = last_base.height * (0.45 if kind == "^" else -0.38)
        small.move_to([x + small.width / 2, dy, 0])
        parts.add(small)
        x = small.get_right()[0] + 0.045
        p = match.end()
    if p < len(s):
        tail = t(s[p:], size, color, bold)
        tail.move_to([x + tail.width / 2, 0, 0])
        parts.add(tail)
    if not len(parts):
        return t(s, size, color, bold)
    parts.move_to(ORIGIN)
    return parts


def fitted(obj, width=6.72, height=None):
    if obj.width > width:
        obj.scale_to_fit_width(width)
    if height and obj.height > height:
        obj.scale_to_fit_height(height)
    return obj


def fraction(top, bottom, color=INK, size=28):
    up=m(str(top),size,color,True)
    down=m(str(bottom),size,color,True)
    w=max(up.width,down.width)+.30
    bar=Line(LEFT*w/2,RIGHT*w/2,color=color,stroke_width=3)
    return VGroup(up,bar,down).arrange(DOWN,buff=.08)


def vertical(*items, gap=0.27, align=ORIGIN):
    return VGroup(*items).arrange(DOWN, buff=gap)


def label_lines(ss, size=27, color=INK, bold=False, gap=.3, width=6.6):
    result = VGroup(*[fitted(t(s, size, color, bold), width) for s in ss])
    result.arrange(DOWN, buff=gap, aligned_edge=LEFT)
    return result


def rounded(width, height, fill=WHITE, border=BORDER, radius=.16, weight=2):
    return RoundedRectangle(width=width, height=height, corner_radius=radius,
                            stroke_color=border, stroke_width=weight,
                            fill_color=fill, fill_opacity=1)


def badge(s, color, size=19, fill=None):
    text = t(s, size, WHITE if fill is None else color, True)
    bg = rounded(max(1.0, text.width + .38), .52, color if fill is None else fill,
                 color, radius=.13, weight=0 if fill is None else 2)
    return VGroup(bg, text.move_to(bg))


def check_icon(ok=True, size=.27, color=None):
    col = color or (GREEN if ok else RED)
    if ok:
        a = Line([-size * .62, -.01, 0], [-size * .15, -size * .38, 0], color=col, stroke_width=7)
        b = Line([-size * .15, -size * .38, 0], [size * .68, size * .47, 0], color=col, stroke_width=7)
    else:
        a = Line([-size*.48, -size*.48, 0], [size*.48,size*.48,0], color=col, stroke_width=7)
        b = Line([-size*.48,size*.48,0], [size*.48,-size*.48,0], color=col, stroke_width=7)
    return VGroup(a,b)


PALETTE = [BLUE, ORANGE, GREEN, PURPLE, TEAL, GOLD]


def gift(identity, value, color=BLUE, w=.88, h=1.02):
    frame = rounded(w, h, WHITE, color, radius=.15, weight=2.8)
    bar = Rectangle(width=w-.18, height=.06, fill_color=color, fill_opacity=1,
                    stroke_width=0).move_to(frame.get_top()+DOWN*.10)
    name = t(str(identity), 20, color, True)
    number = t(str(value), 30, INK, True)
    ink = VGroup(name, number).arrange(DOWN,buff=.03).move_to(frame)
    return VGroup(frame,bar,ink)


def group_box(name, contents, goal, color=BLUE, width=3.0, height=2.0):
    """contents: sequence (identity, value, color); show identities, not only values."""
    bg = rounded(width,height,GRAY_BG,color,radius=.18,weight=2.5)
    heading=t(name or "TỔ",20 if height<1.85 else 22,color,True).move_to(bg.get_top()+DOWN*.25)
    gh=.68 if height<1.85 else .82
    row=VGroup(*[gift(i,v,c,w=.66 if height<1.85 else .72,h=gh) for i,v,c in contents])
    if len(row):
        row.arrange(RIGHT,buff=.07)
        fitted(row,width-.25,.95)
    else:
        row.add(t("chưa có quà",18,SUB))
    row.move_to(bg.get_center()+UP*.03)
    total=sum(v for _,v,_ in contents)
    info=m(f"{total} / {goal}",21, GREEN if total==goal else SUB,True)
    info.move_to(bg.get_bottom()+UP*.23)
    return VGroup(bg,heading,row,info)


def summary_card(heading, desc, color=BLUE, pale=PALE_BLUE, width=6.65, height=1.22):
    bg=rounded(width,height,pale,color,radius=.16,weight=1.6)
    h=fitted(m(heading,25,color,True) if SCRIPT.search(heading) else t(heading,25,color,True),width-.38)
    d=fitted(t(desc,21,INK),width-.38)
    both=VGroup(h,d).arrange(DOWN,buff=.14,aligned_edge=LEFT)
    fitted(both,width-.38,height-.2)
    both.move_to(bg).align_to(bg,LEFT).shift(RIGHT*.18)
    return VGroup(bg,both)


def code_line(s,size=17):
    s = s.expandtabs(4)
    obj = t("█" + (s if s else " "),size,INK,font=MONO)
    if len(obj):obj[0].set_opacity(0)
    # Give whole line a semantic color where appropriate; no malformed markup.
    if "if (" in s or "if(" in s:
        obj.set_color(PURPLE)
    elif "return" in s or "continue" in s:
        obj.set_color(RED)
    elif "Try(" in s or "try(" in s:
        obj.set_color(BLUE)
    return obj


class XepDeuVideo(Scene):
    def setup(self):
        self.heading=None
        self.content=None
        self.notebox=None
        self.cues=[]
        self.sections=[]
        self.flags=[]
        self.section=""
        self.brand=None

    @contextmanager
    def say(self, script, min_time=3.0):
        begin = self.renderer.time
        yield
        # Reading time estimate: Vietnamese short syllable/word, intentional pauses.
        syllables = len(script.split())
        need = max(min_time, syllables/4.15+.8)
        used = self.renderer.time-begin
        if used < need:
            self.wait(need-used)
        self.cues.append([round(begin,3),round(self.renderer.time,3),script])
        self.sections.append((self.section,script))
        self.layout_check()

    def layout_check(self):
        for name,group in [("heading",self.heading),("stage",self.content),("note",self.notebox)]:
            if group is None:continue
            l,r=group.get_left()[0],group.get_right()[0]
            b,u=group.get_bottom()[1],group.get_top()[1]
            if l<LEFT_EDGE-.03 or r>RIGHT_EDGE+.03 or b<SAFE_BOTTOM-.03 or u>SAFE_TOP+.03:
                self.flags.append(f"[{self.section} / {name}] SAFE l={l:.3f},r={r:.3f},b={b:.3f},t={u:.3f}")
            if name=="stage" and (u>STAGE_TOP+.02 or b<STAGE_BOTTOM-.02):
                self.flags.append(f"[{self.section} / stage] OVERLAP b={b:.3f},t={u:.3f}")

    def setup_brand(self):
        mark=VGroup(
            rounded(.40,.39,PALE_BLUE,BLUE,radius=.09,weight=1.2),
            Circle(radius=.055,color=BLUE,fill_color=BLUE,fill_opacity=1).shift(LEFT*.085+UP*.025),
            Circle(radius=.055,color=BLUE,fill_color=BLUE,fill_opacity=1).shift(RIGHT*.085+UP*.025),
            Line(LEFT*.08+DOWN*.095,RIGHT*.08+DOWN*.095,color=BLUE,stroke_width=2.3)
        )
        mark.move_to([LEFT_EDGE+.23,-3.57,0])
        brand=t("CODEPLUS",18,BLUE,True).next_to(mark,RIGHT,buff=.13)
        self.brand=VGroup(mark,brand)
        self.add(self.brand)

    def section_title(self, tag, title, color=BLUE):
        self.section=tag
        left=badge(tag,color,17)
        heading=fitted(t(title,30,INK,True),6.85-left.width-.25,.8)
        title_row=VGroup(left,heading).arrange(RIGHT,buff=.18)
        title_row.move_to([LEFT_EDGE+title_row.width/2,6.55,0])
        divider=Line([LEFT_EDGE,6.16,0],[RIGHT_EDGE,6.16,0],color=color,stroke_width=3)
        new=VGroup(title_row,divider)
        fading=[]
        for item in (self.heading,self.content,self.notebox):
            if item is not None: fading.append(FadeOut(item,shift=DOWN*.08))
        fading.append(FadeIn(new,shift=DOWN*.13))
        self.play(*fading,run_time=.48)
        self.heading=new; self.content=None; self.notebox=None

    def stage(self, obj, cy=2.18, animate=True, max_height=6.75):
        obj=fitted(obj,6.78,max_height)
        if obj.height/2 + cy > STAGE_TOP:cy=STAGE_TOP-obj.height/2-.08
        if cy-obj.height/2 < STAGE_BOTTOM:cy=STAGE_BOTTOM+obj.height/2+.08
        obj.move_to([C,cy,0])
        if animate:
            transition=[]
            if self.content is not None: transition.append(FadeOut(self.content,shift=DOWN*.13))
            transition.append(FadeIn(obj,shift=UP*.13))
            self.play(*transition,run_time=.58)
        else:
            if self.content is not None:self.remove(self.content)
            self.add(obj)
        self.content=obj
        return obj

    def note(self, obj, color=BLUE, fill=GRAY_BG):
        if isinstance(obj,str):obj=m(obj,23,color,True) if SCRIPT.search(obj) else t(obj,23,color,True)
        fitted(obj,6.30,.73)
        bg=rounded(6.76,max(.80,obj.height+.30),fill,color,radius=.14,weight=1.6)
        obj.move_to(bg)
        new=VGroup(bg,obj).move_to([C,NOTE_Y,0])
        moves=[]
        if self.notebox is not None:moves.append(FadeOut(self.notebox))
        moves.append(FadeIn(new,shift=UP*.08))
        self.play(*moves,run_time=.34)
        self.notebox=new
        return new

    def multi_gift(self, items, width=6.6):
        group=VGroup(*[gift(*p) for p in items]).arrange(RIGHT,buff=.12)
        return fitted(group,width)

    def construct(self):
        self.setup_brand()
        self.hook()
        self.problem()
        self.naive()
        self.false_pruning()
        self.canonical_groups()
        self.valid_pruning()
        self.trace()
        self.proof()
        self.code()
        self.end()
        self.export()

    def hook(self):
        self.section_title("BẪY ĐẾM","XẾP ĐỀU: 1 HAY 3 CÁCH?",RED)
        items=[('a',1,BLUE),('b',1,ORANGE),('c',1,GREEN),('d',1,PURPLE)]
        row=self.multi_gift(items)
        mid=vertical(t("4 MÓN QUÀ RIÊNG BIỆT",28,INK,True),row,
                     t("Chia vào 2 tổ · tổng mỗi tổ bằng 2",23,SUB),gap=.51)
        with self.say("Bốn phần quà a, b, c, d đều có giá trị một. Chia vào hai tổ sao cho tổng của hai tổ bằng nhau. Có bao nhiêu cách chia?"):
            self.stage(mid,2.70)
            self.note("Đếm số cách chia, không phân biệt tên tổ",RED,PALE_RED)
        wrong=VGroup(check_icon(False,.35),m("1 cách?",31,RED,True)).arrange(RIGHT,buff=.25)
        right=VGroup(check_icon(True,.35),m("3 cách!",31,GREEN,True)).arrange(RIGHT,buff=.25)
        compare=VGroup(wrong,right).arrange(DOWN,buff=.49)
        with self.say("Nếu áp dụng một nhát cắt nhánh quen thuộc, em có thể đếm ra một. Nhưng kết quả chính xác là ba! Vì sao?",3.5):
            self.stage(vertical(row.copy(),compare,gap=.62),2.45)
            self.note("CÓ / KHÔNG khác hoàn toàn ĐẾM SỐ CÁCH",PURPLE,PALE_PURPLE)

    def problem(self):
        self.section_title("01","HIỂU ĐÚNG ĐỀ BÀI",BLUE)
        statements=vertical(summary_card("n phần quà có giá trị a_{i}","Phần quà là các đối tượng riêng biệt",BLUE),
                            summary_card("Chia hết thành k tổ KHÔNG có tên","Tổng giá trị của mọi tổ bằng nhau",GREEN,PALE_GREEN),gap=.25)
        with self.say("Cô giáo có n phần quà, phần thứ i có giá trị a i. Cần chia toàn bộ vào k tổ, sao cho mỗi tổ có cùng tổng giá trị. Các tổ không phân biệt tên."):
            self.stage(statements,2.50)
            self.note("Hai món bằng giá trị vẫn là hai MÓN KHÁC NHAU",ORANGE,PALE_ORANGE)
        items=[('a',4,BLUE),('b',3,ORANGE),('c',2,GREEN),('d',2,PURPLE),('e',1,TEAL),('f',3,GOLD)]
        top=self.multi_gift(items)
        eq=VGroup(m("T =",29,BLUE,True),fraction("15","3",BLUE,27),m("= 5",29,GREEN,True)).arrange(RIGHT,buff=.19)
        info=vertical(m("n = 6,  k = 3",27,INK,True),eq,gap=.38)
        with self.say("Ví dụ sáu phần quà có giá trị bốn, ba, hai, hai, một, ba. Tổng bằng mười lăm. Chia cho ba tổ thì mỗi tổ phải có tổng bằng năm."):
            self.stage(vertical(top,info,gap=.62),2.60)
            self.note("T = tổng giá trị / k = 5",GREEN,PALE_GREEN)
        a=group_box("Tổ 0",[items[0],items[4]],5,BLUE,width=2.05,height=1.72)
        b=group_box("Tổ 1",[items[1],items[2]],5,GREEN,width=2.05,height=1.72)
        c=group_box("Tổ 2",[items[3],items[5]],5,PURPLE,width=2.05,height=1.72)
        groups=VGroup(a,b,c).arrange(RIGHT,buff=.18)
        ways=t("Đổi ghép b,c và d,f: được 2 cách chia",23,SUB)
        with self.say("Một cách chia là a với e, b với c, d với f. Đổi cặp ghép của hai món giá trị ba và hai, ta có thêm một cách khác."):
            self.stage(vertical(groups,ways,gap=.45),2.57)
            self.note("Ví dụ chính thức này có đúng 2 cách",GREEN,PALE_GREEN)

    def naive(self):
        self.section_title("02","VÌ SAO VÉT CẠN THẤT BẠI?",ORANGE)
        formulas=vertical(
            m("k^{n}  cách gán vào k tổ có tên",30,INK,True),
            m("Mỗi cách chia bị đếm k! lần",29,PURPLE),
            m("Đáp án = số gán hợp lệ / k!",29,BLUE,True),gap=.57)
        with self.say("Cách đầu tiên là gán mỗi món vào một trong k tổ có tên. Có k mũ n cách gán. Mỗi cách chia đúng bị đếm k giai thừa lần do đổi tên tổ, nên phải chia cho k giai thừa."):
            self.stage(formulas,2.38)
            self.note("Vét cạn: tốn thời gian theo cấp số mũ",ORANGE,PALE_ORANGE)
        huge=vertical(m("n = 20,  k = 3",29,SUB),
                      m("3^{20} = 3 486 784 401",36,RED,True),
                      t("Gần 3,5 TỈ trạng thái gán!",30,RED,True),gap=.55)
        with self.say("Với n bằng hai mươi và k bằng ba, số gán là ba mũ hai mươi, tức ba tỉ bốn trăm tám mươi sáu triệu bảy trăm tám mươi bốn nghìn bốn trăm linh một. Quá lớn."):
            self.stage(huge,2.40)
            self.note("Phải cắt nhánh, nhưng KHÔNG được cắt sai",RED,PALE_RED)

    def false_pruning(self):
        self.section_title("03","BẪY: CẮT NHÁNH TRÙNG TỔNG",RED)
        first=vertical(t("Nếu hai tổ có cùng tổng hiện tại...",27,INK,True),
                       VGroup(check_icon(False),t("Chỉ thử một tổ?",28,RED,True)).arrange(RIGHT,buff=.2),gap=.54)
        with self.say("Có một nhát cắt rất quen thuộc. Nếu hai tổ đang có tổng bằng nhau, ta chỉ thử đặt phần quà vào một tổ. Nhát cắt này có được dùng không?"):
            self.stage(first,2.40)
            self.note("ĐÚNG để kiểm tra tồn tại; SAI khi đếm",RED,PALE_RED)
        cards=VGroup(group_box("Tổ 0",[('a',1,BLUE)],2,BLUE,2.78,1.9),
                     group_box("Tổ 1",[('b',1,ORANGE)],2,ORANGE,2.78,1.9)).arrange(RIGHT,buff=.38)
        branch=vertical(cards,m("g_{0} = g_{1} = 1",31,PURPLE,True),
                        t("Nhưng tập phần quà trong hai tổ KHÁC nhau",23,RED,True),gap=.4)
        with self.say("Hai tổ đều có tổng một, nhưng tổ không chứa món a, còn tổ một chứa món b. Thử đặt món c vào mỗi tổ sẽ tạo ra những cách chia khác nhau."):
            self.stage(branch,2.37)
            self.note("Không được đồng nhất hai nhóm chỉ vì cùng tổng",RED,PALE_RED)
        triples=[([('a',1,BLUE),('b',1,ORANGE)],[('c',1,GREEN),('d',1,PURPLE)]),
                 ([('a',1,BLUE),('c',1,GREEN)],[('b',1,ORANGE),('d',1,PURPLE)]),
                 ([('a',1,BLUE),('d',1,PURPLE)],[('b',1,ORANGE),('c',1,GREEN)])]
        listing=VGroup()
        for ix,(left,right) in enumerate(triples,1):
            tag=badge(f"CÁCH {ix}",BLUE if ix==1 else GREEN,16)
            # Compact visual: colored identities, no unnecessary totals.
            p=VGroup(*[gift(*item,w=.68,h=.77) for item in left]).arrange(RIGHT,buff=.06)
            q=VGroup(*[gift(*item,w=.68,h=.77) for item in right]).arrange(RIGHT,buff=.06)
            middle=t("/",28,SUB,True)
            pair=VGroup(p,middle,q).arrange(RIGHT,buff=.18)
            pairbg=rounded(4.16,1.05,GRAY_BG,BORDER,radius=.14,weight=1)
            pair.move_to(pairbg)
            line=VGroup(tag,VGroup(pairbg,pair)).arrange(RIGHT,buff=.25)
            listing.add(line)
        listing.arrange(DOWN,buff=.20)
        with self.say("Ba cách chia phân biệt là: a b với c d; a c với b d; và a d với b c. Bỏ các tổ trùng tổng sẽ đánh mất nghiệm. Đây là lỗi nguy hiểm nhất của bài toán này.",min_time=5.0):
            self.stage(listing,2.40)
            self.note("3 phân hoạch khác nhau, tuyệt đối không bỏ bớt",GREEN,PALE_GREEN)

    def canonical_groups(self):
        self.section_title("04","PHÁ ĐÚNG ĐỐI XỨNG",GREEN)
        steps=vertical(summary_card("Mở tổ 0 trước", "Món đầu tiên buộc phải mở tổ đầu tiên", BLUE),
                       summary_card("Món tiếp theo", "Vào tổ đã mở HOẶC mở đúng một tổ mới", GREEN,PALE_GREEN),
                       summary_card("Không đặt tên tổ tùy ý", "Tổ được đánh số theo THỨ TỰ MỞ", PURPLE,PALE_PURPLE),gap=.28)
        with self.say("Ta chỉ phá đối xứng do tên tổ. Mỗi tổ được đánh số theo thứ tự xuất hiện: không, một, hai. Mỗi món được xếp vào tổ đã mở, hoặc mở đúng một tổ mới. Không bao giờ được mở trực tiếp tổ hai khi tổ một chưa mở."):
            self.stage(steps,2.43)
            self.note("Mỗi phân hoạch xuất hiện CHÍNH XÁC 1 lần",GREEN,PALE_GREEN)
        math=vertical(m("Try(i, used)",37,BLUE,True),
                      m("i:  số món đã xếp",27,SUB),
                      m("used:  số tổ đã mở",27,SUB),
                      m("j = 0, 1, ..., used - 1",29,PURPLE,True),
                      t("hoặc mở tổ mới mang số used",27,GREEN,True),gap=.35)
        with self.say("Trạng thái quay lui là Try của i và used: i món đầu đã được xếp, và used tổ đã mở. Chọn một trong các tổ từ không đến used trừ một, hoặc mở nhóm mới có số used."):
            self.stage(math,2.52)
            self.note("Không cần chia kết quả cho k!",GREEN,PALE_GREEN)

    def valid_pruning(self):
        self.section_title("05","HAI NHÁT CẮT AN TOÀN",ORANGE)
        over=vertical(m("T = 5",29,SUB),
                      VGroup(group_box("Tổ 0",[('a',4,BLUE)],5,BLUE,3.1,2.00),
                             gift('c',2,GREEN,w=.87,h=1.0)).arrange(RIGHT,buff=.55),
                      m("g_{0} + a_{i} = 4 + 2 = 6 > 5",29,RED,True),gap=.55)
        with self.say("Nhát cắt thứ nhất: nếu tổng một tổ sau khi thêm món mới vượt T, nhánh này chắc chắn sai, vì tất cả giá trị đều dương. Bốn cộng hai bằng sáu lớn hơn năm."):
            self.stage(over,2.42)
            self.note("g_{j} + a_{i} > T  ⇒  KHÔNG THỬ",RED,PALE_RED)
        less=vertical(m("n - i = 1",32,INK,True),
                      m("k - used = 2",32,INK,True),
                      VGroup(check_icon(False),t("1 món không thể mở đủ 2 tổ",26,RED,True)).arrange(RIGHT,buff=.20),gap=.58)
        with self.say("Nhát cắt thứ hai: nếu số món quà chưa xếp ít hơn số tổ còn phải mở, nhánh này không thể hoàn thành. Ví dụ còn một món nhưng phải mở tới hai tổ."):
            self.stage(less,2.42)
            self.note("n - i < k - used  ⇒  CẮT",RED,PALE_RED)
        sort=vertical(m("a_{0} ≥ a_{1} ≥ ... ≥ a_{n-1}",30,BLUE,True),
                      t("Xếp món lớn trước",29,INK,True),
                      t("Nhánh vượt T bị phát hiện sớm hơn",24,SUB),gap=.56)
        with self.say("Sắp các món theo giá trị giảm dần, món lớn đứng trước. Cách này giúp phát hiện nhánh vượt T sớm hơn. Tuy nhiên, từng món quà vẫn giữ danh tính riêng."):
            self.stage(sort,2.47)
            self.note("Sắp xếp giá trị, không gộp các món bằng nhau",GREEN,PALE_GREEN)

    def trace(self):
        self.section_title("06","CHẠY TAY TỪNG NHÁNH",BLUE)
        names={'a':('a',1,BLUE),'b':('b',1,ORANGE),'c':('c',1,GREEN),'d':('d',1,PURPLE)}
        top=self.multi_gift(list(names.values()))
        start=vertical(top,m("n = 4,  k = 2,  T = 2",31,BLUE,True),
                       t("a buộc mở tổ 0",28,INK,True),gap=.55)
        with self.say("Giờ chạy tay bốn món quà a, b, c, d, giá trị mỗi món là một. Chia hai tổ, mỗi tổ tổng hai. Món a chỉ có một lựa chọn là mở tổ không."):
            self.stage(start,2.55)
            self.note("Thứ tự món cố định: a → b → c → d",BLUE,PALE_BLUE)
        scenarios=[
            ("NHÁNH 1",['a','b'],['c','d'],"Cho b vào tổ không. Hai món còn lại tạo tổ một."),
            ("NHÁNH 2",['a','c'],['b','d'],"Cho b mở tổ một, rồi cho c vào tổ không."),
            ("NHÁNH 3",['a','d'],['b','c'],"Vẫn cho b mở tổ một, nhưng cho c vào tổ một.")]
        for ix,(tag,aa,bb,narr) in enumerate(scenarios,1):
            a=group_box("Tổ 0",[names[x] for x in aa],2,BLUE,3.0,2.10)
            b=group_box("Tổ 1",[names[x] for x in bb],2,GREEN,3.0,2.10)
            pair=VGroup(a,b).arrange(RIGHT,buff=.27)
            center=vertical(t(tag,30,PURPLE,True),pair,
                            VGroup(check_icon(True),t("Mỗi tổ tổng 2: HỢP LỆ",25,GREEN,True)).arrange(RIGHT,buff=.2),gap=.46)
            with self.say(narr+" Cách chia thứ "+str(ix)+" hợp lệ.",min_time=3.2):
                self.stage(center,2.40)
                self.note(f"Cách {ix} / 3 · Danh tính từng món được giữ nguyên",GREEN,PALE_GREEN)
        with self.say("Vậy có đúng ba cách chia. Khi hai tổ đang có cùng tổng một, ta vẫn phải thử cả hai cách đặt món tiếp theo, vì thành viên của hai tổ khác nhau.",min_time=4.5):
            self.note("ĐÁP ÁN = 3 · Không đếm trùng, không bỏ sót",GREEN,PALE_GREEN)

    def proof(self):
        self.section_title("07","LẬP LUẬN TÍNH ĐÚNG",GREEN)
        cards=vertical(summary_card("1 · Không đếm trùng", "Thứ tự mở nhóm được xác định duy nhất", GREEN,PALE_GREEN),
                       summary_card("2 · Không bỏ sót", "Mọi phân hoạch có một chuỗi thao tác hợp lệ", BLUE,PALE_BLUE),
                       summary_card("3 · Chỉ cắt nhánh vô nghiệm", "Vượt T hoặc thiếu món để mở đủ nhóm", PURPLE,PALE_PURPLE),gap=.22)
        with self.say("Tại sao đúng? Một: mỗi cách chia có thứ tự mở nhóm duy nhất, nên không đếm trùng. Hai: mọi phân hoạch đều có một chuỗi thao tác mở nhóm và đặt món, nên không bỏ sót. Ba: các nhát cắt chỉ bỏ những nhánh không thể hoàn thành."):
            self.stage(cards,2.45)
            self.note("Chỉ khi đủ k tổ và xếp hết n món mới tăng đáp án",GREEN,PALE_GREEN)
        math=vertical(m("0 ≤ g_{j} ≤ T",31,PURPLE,True),
                      m("g_{0} + ... + g_{k-1} = kT",30,BLUE,True),
                      m("⇒  g_{j} = T   (mọi j)",31,GREEN,True),gap=.58)
        with self.say("Một chi tiết tinh tế: ở lá của cây tìm kiếm, tất cả nhóm có tổng không vượt T, trong khi tổng tất cả các nhóm bằng k nhân T. Vì vậy mỗi nhóm bắt buộc có tổng đúng T."):
            self.stage(math,2.45)
            self.note("Không cần quét lại từng tổ ở trạng thái kết thúc",GREEN,PALE_GREEN)

    def code(self):
        self.section_title("08","C++: QUAY LUI ĐÚNG CÁCH",PURPLE)
        chunks=[
            (["void Try(int i, int used) {",
              "    if (i == n) {",
              "        if (used == k) cnt++;",
              "        return;",
              "    }",
              "    if (n - i < k - used) return;"],
             "Cơ sở đệ quy: xếp đủ n món và đã mở đủ k nhóm thì tăng biến đếm. Nếu các món còn lại không đủ để mở tất cả nhóm thiếu, quay lui ngay."),
            (["    for (int j = 0; j < used; j++) {",
              "        if (g[j] + a[i] > T) continue;",
              "        g[j] += a[i];",
              "        Try(i + 1, used);",
              "        g[j] -= a[i];",
              "    }"],
             "Thử đưa món thứ i vào từng nhóm đã mở. Nếu vượt T thì bỏ qua. Sau lời gọi đệ quy, phải trừ lại giá trị để hoàn tác trạng thái."),
            (["    if (used < k) {",
              "        g[used] = a[i];",
              "        Try(i + 1, used + 1);",
              "        g[used] = 0;",
              "    }",
              "}"],
             "Cuối cùng, nếu số tổ đã mở còn nhỏ hơn k, chỉ được mở đúng một tổ mới mang số used. Hoàn tác sau khi xét xong nhánh.")]
        for ix,(lines,voice) in enumerate(chunks,1):
            shell=rounded(6.7,3.68,"#F8FAFC",BORDER,radius=.16,weight=1.3)
            code=VGroup(*[code_line(s,18) for s in lines]).arrange(DOWN,buff=.22,aligned_edge=LEFT)
            fitted(code,6.25,3.10)
            code.move_to(shell).align_to(shell,LEFT).shift(RIGHT*.25)
            block=VGroup(shell,code)
            decorated=vertical(badge(f"KHỐI {ix} / 3",PURPLE,20),block,gap=.4)
            with self.say(voice,min_time=4.5):
                self.stage(decorated,2.50)
                self.note("File XEPDEU.cpp chứa chương trình đầy đủ",PURPLE,PALE_PURPLE)
        with self.say("Trước khi quay lui cần tính T bằng tổng chia k. Nếu tổng không chia hết, hoặc có món lớn hơn T, đáp án bằng không. Sắp xếp giảm dần và bắt đầu Try của không, không."):
            frac=VGroup(m("T =",28,BLUE,True),fraction("tổng","k",BLUE,26)).arrange(RIGHT,buff=.18)
            summary=vertical(frac,
                             m("tổng % k ≠ 0  ⇒  đáp án 0",29,RED,True),
                             m("max(a_{i}) > T  ⇒  đáp án 0",29,RED,True),
                             m("Try(0, 0)",32,GREEN,True),gap=.5)
            self.stage(summary,2.50)
            self.note("Độ phức tạp phụ thuộc trạng thái, xấu nhất vẫn hàm mũ",PURPLE,PALE_PURPLE)

    def end(self):
        self.section_title("GHI NHỚ","SỰ KHÁC BIỆT NẰM Ở ĐẾM!",GREEN)
        all=vertical(summary_card("CÙNG TỔNG không phải CÙNG TRẠNG THÁI", "Nếu thành viên khác nhau, không được gộp khi đếm", RED,PALE_RED),
                     summary_card("Chỉ phá đối xứng đặt tên tổ", "Mở tổ lần lượt: 0, 1, 2, ...", GREEN,PALE_GREEN),
                     summary_card("Cắt nhánh có chứng minh", "Vượt T · Thiếu món mở đủ k tổ", BLUE,PALE_BLUE),gap=.30)
        with self.say("Bài học quan trọng nhất: một nhát cắt hợp lệ để kiểm tra có nghiệm chưa chắc đúng khi đếm số nghiệm. Hãy giữ nguyên danh tính từng phần quà, chỉ phá đối xứng đặt tên các tổ, và chứng minh mỗi nhát cắt.",min_time=5.0):
            self.stage(all,2.39)
            self.note("CODEPLUS · XẾP ĐỀU · NHÁNH CẬN",GREEN,PALE_GREEN)

    def export(self):
        # File written at the end of a real Manim render; timestamps are real scene times.
        if os.environ.get("NP_NO_OUTPUT") == "1": return
        output=Path(os.getenv("NP_OUT",str(Path(__file__).resolve().parent)))
        output.mkdir(parents=True,exist_ok=True)
        def ts(sec):
            ms=int(round(sec*1000))
            return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"
        def chunks(text,limit=46):
            words=text.split();out=[];cur=[]
            for word in words:
                trial=" ".join(cur+[word])
                if len(trial)>limit and cur:
                    out.append(" ".join(cur));cur=[word]
                else:cur.append(word)
            if cur:out.append(" ".join(cur))
            # Break into at most two lines per subtitle interval.
            return ["\n".join(out[i:i+2]) for i in range(0,len(out),2)]
        sub=[];index=0
        for begin,end,message in self.cues:
            pieces=chunks(message)
            weights=[max(1,len(p.replace("\n"," ").split())) for p in pieces]
            total=sum(weights)
            time=begin
            for piece,weight in zip(pieces,weights):
                nxt=time+(end-begin)*weight/total
                index+=1
                sub.append(f"{index}\n{ts(time)} --> {ts(max(time+.10,nxt-.02))}\n{piece}\n")
                time=nxt
        (output/"XEPDEU.srt").write_text("\n".join(sub),encoding="utf-8")
        voices=[];last=None
        for sec,script in self.sections:
            if sec!=last:voices.append("\n=== "+sec+" ===\n");last=sec
            voices.append(script)
        (output/"XEPDEU_thuyetminh.txt").write_text("\n\n".join(voices),encoding="utf-8")
        (output/"XEPDEU_cues.json").write_text(json.dumps(self.cues,ensure_ascii=False,indent=2),encoding="utf-8")
        (output/"XEPDEU_layout_check.txt").write_text("\n".join(dict.fromkeys(self.flags)) if self.flags else "OK: Không phát hiện nội dung vượt vùng an toàn.\n",encoding="utf-8")


# Compatibility with old script's class name / render command.
Video=XepDeuVideo