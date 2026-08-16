#!/usr/bin/env python3
"""Regenerate og.png, the social preview card for the Nova Helix showcase.

The card mirrors the palette and typography of index.html so the link preview
and the landing page look like the same product.

    pip install pillow
    python3 tools/make-og-image.py

Writes og.png (1200x630) next to the repository root.
"""

from math import hypot
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (11, 13, 22)
ACCENT = (124, 92, 255)
ACCENT2 = (78, 163, 255)
MUTED = (154, 163, 192)
LINE = (38, 45, 74)

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path("/usr/share/fonts/truetype/dejavu")
BOLD = FONTS / "DejaVuSans-Bold.ttf"
REGULAR = FONTS / "DejaVuSans.ttf"

TITLE = "Nova Helix"
TAGLINE = "An AI companion that lives on your computer"
PILL = "100% local  ·  Private by design  ·  Windows"


def glow() -> Image.Image:
    """The header's radial purple wash, matching the CSS in index.html."""
    sw, sh = 150, 79  # rendered small, then scaled up — cheap and smooth
    layer = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    px = layer.load()
    cx, cy = sw / 2, -0.10 * sh
    rx, ry = 0.80 * sw, 0.60 * sh
    for y in range(sh):
        for x in range(sw):
            d = hypot((x - cx) / rx, (y - cy) / ry)
            if d < 1:
                falloff = (1 - d) ** 2
                px[x, y] = (*ACCENT, int(255 * 0.28 * falloff))
    return layer.resize((W, H), Image.BICUBIC)


def gradient_text(text: str, font: ImageFont.FreeTypeFont) -> Image.Image:
    """Left-to-right accent gradient clipped to the glyphs."""
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).text((W / 2, 250), text, font=font, fill=255, anchor="mm")

    ramp = Image.new("RGB", (W, 1))
    ramp_px = ramp.load()
    for x in range(W):
        t = x / (W - 1)
        ramp_px[x, 0] = tuple(round(a + (b - a) * t) for a, b in zip(ACCENT, ACCENT2))

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    layer.paste(ramp.resize((W, H)), (0, 0), mask)
    return layer


def main() -> None:
    card = Image.new("RGBA", (W, H), (*BG, 255))
    card.alpha_composite(glow())

    card.alpha_composite(gradient_text(TITLE, ImageFont.truetype(str(BOLD), 118)))

    draw = ImageDraw.Draw(card)
    draw.text((W / 2, 352), TAGLINE, font=ImageFont.truetype(str(REGULAR), 38),
              fill=MUTED, anchor="mm")

    pill_font = ImageFont.truetype(str(REGULAR), 26)
    tw = draw.textlength(PILL, font=pill_font)
    pad_x, pad_y, cy = 34, 19, 470
    draw.rounded_rectangle(
        [(W / 2 - tw / 2 - pad_x, cy - pad_y - 12), (W / 2 + tw / 2 + pad_x, cy + pad_y + 12)],
        radius=999, outline=LINE, width=2,
    )
    draw.text((W / 2, cy), PILL, font=pill_font, fill=ACCENT2, anchor="mm")

    draw.text((W / 2, 566), "ndeveloperh.github.io/Nova-Helix-V5",
              font=ImageFont.truetype(str(REGULAR), 24), fill=MUTED, anchor="mm")

    out = ROOT / "og.png"
    card.convert("RGB").save(out, optimize=True)
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
