import sys
import random

from multiscaletruchet import TILES
import multiscaletruchet.svg as svg

# Rows / Cols
M = 20
N = 20
w = M / 12 * 1000
h = N / 12 * 1000


print(svg.header(author="Helena", title="Singlescale Truchet", width=w, height=h))


def piece(part, offset=None):
    x, y = offset
    transform = f"translate({x}, {y})"
    return f"""<g transform="{transform}">{part}</g>"""


o = 90

for r in range(M):
    for c in range(N):
        p = random.choice(TILES)
        sys.stdout.write(piece(p, offset=(c * o, r * o)))


print(svg.footer())
