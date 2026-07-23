#!/usr/bin/env python3
"""Generate the AutomationPlusPlus org avatar (profile/avatar.png).

Arms use DejaVu Sans Bold unstroked — a uniform stroke fuses the tightly
packed ¯ \\ _ ( glyphs into blobs. Only the thin serif ツ gets a mild stroke.
"""
from PIL import Image, ImageDraw, ImageFont

SIZE, SS = 512, 4  # supersample 4x for crisp downscale
W = SIZE * SS
BG, FG, ACCENT = (15, 23, 42), (241, 245, 249), (129, 140, 248)
DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CJK = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"

def build(font_size):
    dv = ImageFont.truetype(DEJAVU, font_size)
    face_size = int(font_size * 1.4)
    cjk = ImageFont.truetype(CJK, face_size, index=2)  # index 2 = JP
    face_stroke = int(face_size * 0.03)
    return [("¯\\_(", dv, 0), ("ツ", cjk, face_stroke), (")_/¯", dv, 0)]

img = Image.new("RGB", (W, W), BG)
d = ImageDraw.Draw(img)

# size the shrug to ~90% of the canvas width
target = int(W * 0.90)
fs = 400
for _ in range(20):
    segs = build(fs)
    w = sum(d.textlength(t, font=f) for t, f, _ in segs)
    if abs(w - target) < 8:
        break
    fs = int(fs * target / w)
segs = build(fs)
total_w = sum(d.textlength(t, font=f) for t, f, _ in segs)

# center vertically on the combined ink bbox
tops, bottoms = [], []
for t, f, st in segs:
    b = d.textbbox((0, 0), t, font=f, stroke_width=st)
    tops.append(b[1])
    bottoms.append(b[3])
top, bottom = min(tops), max(bottoms)

x = (W - total_w) / 2
y = (W - (bottom - top)) / 2 - top
for t, f, st in segs:
    d.text((x, y), t, font=f, fill=FG, stroke_width=st, stroke_fill=FG)
    x += d.textlength(t, font=f)

# "++" accent, bottom right
pp = ImageFont.truetype(DEJAVU, int(W * 0.14))
pb = d.textbbox((0, 0), "++", font=pp)
d.text((W - (pb[2] - pb[0]) - int(W * 0.06), W - (pb[3] - pb[1]) - pb[1] - int(W * 0.05)),
       "++", font=pp, fill=ACCENT)

img = img.resize((SIZE, SIZE), Image.LANCZOS)
img.save("avatar.png")
print("saved avatar.png, font", fs)
