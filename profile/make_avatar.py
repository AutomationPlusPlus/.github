#!/usr/bin/env python3
"""Generate the AutomationPlusPlus org avatar: shrug kaomoji on a dark rounded card."""
from PIL import Image, ImageDraw, ImageFont

SIZE = 512
BG = (15, 23, 42)        # slate-900
FG = (241, 245, 249)     # slate-100
ACCENT = (129, 140, 248) # indigo-400

DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CJK = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"

# segments: (text, font_path, ttc_index)
def segments(font_size):
    dv = ImageFont.truetype(DEJAVU, font_size)
    cjk = ImageFont.truetype(CJK, int(font_size * 1.25), index=2)  # JP face, upsized for balance
    return [("¯\\_(", dv), ("ツ", cjk), (")_/¯", dv)]

img = Image.new("RGB", (SIZE, SIZE), BG)
d = ImageDraw.Draw(img)

# subtle accent ring
d.rounded_rectangle([14, 14, SIZE - 14, SIZE - 14], radius=72, outline=ACCENT, width=6)

# find the font size that makes the shrug fit ~82% of width
target = int(SIZE * 0.82)
font_size = 100
for _ in range(20):
    segs = segments(font_size)
    w = sum(d.textlength(t, font=f) for t, f in segs)
    if abs(w - target) < 4:
        break
    font_size = int(font_size * target / w)
segs = segments(font_size)
total_w = sum(d.textlength(t, font=f) for t, f in segs)

# vertical metrics: use combined bbox of all segments for centering
tops, bottoms = [], []
x = 0
for t, f in segs:
    bbox = d.textbbox((0, 0), t, font=f)
    tops.append(bbox[1])
    bottoms.append(bbox[3])
top, bottom = min(tops), max(bottoms)
text_h = bottom - top

x = (SIZE - total_w) / 2
y = (SIZE - text_h) / 2 - top
for t, f in segs:
    d.text((x, y), t, font=f, fill=FG)
    x += d.textlength(t, font=f)

# small "++" accent, bottom right inside the ring
pp_font = ImageFont.truetype(DEJAVU, 56)
d.text((SIZE - 118, SIZE - 108), "++", font=pp_font, fill=ACCENT)

out = "/tmp/claude-1000/-code/d6f7ba8f-76ca-4134-84ac-eabb06e70e57/scratchpad/avatar.png"
img.save(out)
print("saved", out, "font_size", font_size)
