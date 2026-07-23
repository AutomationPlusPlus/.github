#!/usr/bin/env python3
"""Generate the AutomationPlusPlus org avatar (profile/avatar.png).

Arms use DejaVu Sans Bold unstroked — a uniform stroke fuses the tightly
packed ¯ \\ _ ( glyphs into blobs. The serif ツ gets a mild stroke and is
sized/positioned by ink bbox so it sits centered between the parentheses
instead of hanging below their baseline.
"""
from PIL import Image, ImageDraw, ImageFont

SIZE, SS = 512, 4  # supersample 4x for crisp downscale
W = SIZE * SS
BG, FG, ACCENT = (15, 23, 42), (241, 245, 249), (129, 140, 248)
DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CJK = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"

img = Image.new("RGB", (W, W), BG)
d = ImageDraw.Draw(img)

def face_font_for(paren_ink_h, guess):
    # scale the face font so its ink height is ~88% of the paren ink height
    for _ in range(10):
        f = ImageFont.truetype(CJK, guess, index=2)  # index 2 = JP
        st = int(guess * 0.03)
        b = d.textbbox((0, 0), "ツ", font=f, stroke_width=st)
        ink = b[3] - b[1]
        target = paren_ink_h * 0.88
        if abs(ink - target) < 4:
            break
        guess = int(guess * target / ink)
    return f, st

def layout(fs):
    dv = ImageFont.truetype(DEJAVU, fs)
    pb = d.textbbox((0, 0), "(", font=dv)
    cjk, st = face_font_for(pb[3] - pb[1], int(fs * 1.1))
    return dv, cjk, st, pb

# fit total width to ~90% of the canvas
fs = 400
for _ in range(20):
    dv, cjk, st, pb = layout(fs)
    total = (d.textlength("¯\\_(", font=dv) + d.textlength("ツ", font=cjk)
             + d.textlength(")_/¯", font=dv))
    target_w = W * 0.90
    if abs(total - target_w) < 8:
        break
    fs = int(fs * target_w / total)

dv, cjk, st, pb = layout(fs)
w_left = d.textlength("¯\\_(", font=dv)
w_face = d.textlength("ツ", font=cjk)
total = w_left + w_face + d.textlength(")_/¯", font=dv)

# arms: center the full-arm ink bbox on the canvas
ab = d.textbbox((0, 0), "¯\\_()_/¯", font=dv)
x = (W - total) / 2
y_arms = (W - (ab[3] - ab[1])) / 2 - ab[1]

# face: center its ink on the paren ink center
paren_center = y_arms + (pb[1] + pb[3]) / 2
fb = d.textbbox((0, 0), "ツ", font=cjk, stroke_width=st)
y_face = paren_center - (fb[1] + fb[3]) / 2

d.text((x, y_arms), "¯\\_(", font=dv, fill=FG)
d.text((x + w_left, y_face), "ツ", font=cjk, fill=FG, stroke_width=st, stroke_fill=FG)
d.text((x + w_left + w_face, y_arms), ")_/¯", font=dv, fill=FG)

# "++" accent, bottom right
pp = ImageFont.truetype(DEJAVU, int(W * 0.14))
ppb = d.textbbox((0, 0), "++", font=pp)
d.text((W - (ppb[2] - ppb[0]) - int(W * 0.06), W - (ppb[3] - ppb[1]) - ppb[1] - int(W * 0.05)),
       "++", font=pp, fill=ACCENT)

img = img.resize((SIZE, SIZE), Image.LANCZOS)
img.save("avatar.png")
print("saved avatar.png, arm font", fs)
