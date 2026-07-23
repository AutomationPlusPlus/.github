#!/usr/bin/env python3
"""Generate the AutomationPlusPlus org avatar: shrug kaomoji on a dark card."""
from PIL import Image, ImageDraw, ImageFont

SIZE = 512
SS = 4  # supersample for crisp downscale
W = SIZE * SS
BG = (15, 23, 42)        # slate-900
FG = (241, 245, 249)     # slate-100
ACCENT = (129, 140, 248) # indigo-400

DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CJK = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"

STROKE_FRAC = 0.045  # extra stroke as fraction of font size, to fatten thin glyphs

def segments(font_size):
    dv = ImageFont.truetype(DEJAVU, font_size)
    cjk = ImageFont.truetype(CJK, int(font_size * 1.35), index=2)  # JP face, upsized
    return [("¯\\_(", dv), ("ツ", cjk), (")_/¯", dv)]

img = Image.new("RGB", (W, W), BG)
d = ImageDraw.Draw(img)

# find the font size that makes the shrug fit ~88% of width (incl. stroke)
target = int(W * 0.88)
font_size = 400
for _ in range(20):
    segs = segments(font_size)
    stroke = int(font_size * STROKE_FRAC)
    w = sum(d.textlength(t, font=f) for t, f in segs) + 2 * stroke
    if abs(w - target) < 8:
        break
    font_size = int(font_size * target / w)
segs = segments(font_size)
stroke = int(font_size * STROKE_FRAC)
total_w = sum(d.textlength(t, font=f) for t, f in segs)

# vertical centering from the combined ink bbox of the whole composite
tops, bottoms = [], []
for t, f in segs:
    bbox = d.textbbox((0, 0), t, font=f, stroke_width=stroke)
    tops.append(bbox[1])
    bottoms.append(bbox[3])
top, bottom = min(tops), max(bottoms)

x = (W - total_w) / 2
y = (W - (bottom - top)) / 2 - top
for t, f in segs:
    d.text((x, y), t, font=f, fill=FG, stroke_width=stroke, stroke_fill=FG)
    x += d.textlength(t, font=f)

# "++" accent, bottom right — bigger and bolder than before
pp_font = ImageFont.truetype(DEJAVU, int(W * 0.16))
pp_bbox = d.textbbox((0, 0), "++", font=pp_font)
d.text((W - (pp_bbox[2] - pp_bbox[0]) - int(W * 0.06), W - (pp_bbox[3] - pp_bbox[1]) - pp_bbox[1] - int(W * 0.05)),
       "++", font=pp_font, fill=ACCENT)

img = img.resize((SIZE, SIZE), Image.LANCZOS)
out = "/tmp/claude-1000/-code/d6f7ba8f-76ca-4134-84ac-eabb06e70e57/scratchpad/avatar.png"
img.save(out)

# small-size legibility proof sheet: 48px and 96px pasted on a canvas
sheet = Image.new("RGB", (400, 160), (40, 40, 48))
sheet.paste(img.resize((96, 96), Image.LANCZOS), (24, 32))
sheet.paste(img.resize((48, 48), Image.LANCZOS), (160, 56))
sheet.paste(img.resize((32, 32), Image.LANCZOS), (248, 64))
sheet.save("/tmp/claude-1000/-code/d6f7ba8f-76ca-4134-84ac-eabb06e70e57/scratchpad/avatar_small_preview.png")
print("saved", out, "font_size", font_size, "stroke", stroke)
