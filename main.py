import glob
import sys
import random

# Rows / Cols
M = 20
N = 20
w = M / 12 * 1000
h = N / 12 * 1000

TPL = f"""<?xml version="1.0" encoding="utf-8"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   height="{h}"
   version="1.1"
   viewBox="0 0 {w} {h}"
   width="{w}"
   id="svg802"
   sodipodi:docname="out.svg"
   inkscape:version="0.92.3 (2405546, 2018-03-11)">
>

  <metadata
     id="metadata808">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
        <dc:creator>
          <cc:Agent>
            <dc:title>Galactic Girlfriends</dc:title>
          </cc:Agent>
        </dc:creator>
        <dc:description>Multiscale Truchet Tiles</dc:description>
      </cc:Work>
    </rdf:RDF>
  </metadata>
"""

sys.stdout.write(TPL)


pieces = []
for file in sorted(glob.glob("*.path")):
    with open(file, "r") as handle:
        pieces.append(handle.read())


def piece(part, offset=None):
    x, y = offset
    transform = f"translate({x}, {y})"
    return f"""<g transform="{transform}">{part}</g>"""


o = 90

for r in range(M):
    for c in range(N):
        p = random.choice(pieces[3:9])
        sys.stdout.write(piece(p, offset=(c * o, r * o)))


sys.stdout.write("</svg>")
