#!/usr/bin/env bash
# Crop figures/tables from ../ho2026declarative_attention.pdf into images/ (200 dpi).
# Needs pdftoppm (poppler) and Python with Pillow.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
pdf="$here/../ho2026declarative_attention.pdf"
[ -f "$pdf" ] || (cd "$here/../.." && ./scripts/ensure-extract.sh ho2026declarative_attention)
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
mkdir -p "$here/images"
for p in 1 3 8 9 10 11 12 39; do
  pdftoppm -f $p -l $p -r 200 -png -singlefile "$pdf" "$tmp/p$p" 2>/dev/null
done
python3 -I - "$tmp" "$here/images" <<'PY'
import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
# name: (page, (left, top, right, bottom)) in 200-dpi pixels
boxes = {
    "example-acme":           (3,  (160, 860, 1490, 1345)),
    "fig1-protocol":          (1,  (190, 990, 1470, 1815)),
    "table2-main-results":    (8,  (133, 220, 1570, 1060)),
    "fig2-masking-vs-length": (9,  (110, 210, 1570, 660)),
    "fig3-model-scale":       (9,  (180, 920, 1470, 1320)),
    "fig4-context-length":    (10, (250, 280, 1400, 825)),
    "table3-wall-time":       (11, (350, 225, 1410, 505)),
    "fig5-mode-share":        (12, (250, 210, 1470, 725)),
    "fig6-focus-adherence":   (12, (180, 925, 1470, 1360)),
    "prompt-soft-requirements": (39, (178, 560, 1512, 945)),
}
for name, (p, box) in boxes.items():
    Image.open(f"{src}/p{p}.png").crop(box).save(f"{out}/{name}.png")
    print(f"images/{name}.png")
PY
