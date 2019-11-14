import glob
import sys
import random
import svg
import quadtree


print(svg.header(author="Helena", title="Multiscale Truchet", width=800, height=800))


pieces = []
for file in sorted(glob.glob("svgs/*.path")):
    with open(file, "r") as handle:
        pieces.append(handle.read())


def piece(part, scale=None, offset=None):
    x, y = offset
    transform = f"translate({x}, {y}) scale({scale})"
    return f"""<g transform="{transform}">{part}</g>"""


q = quadtree.init(size=900)
# q.random_divide(kids=0)
q.divide_min_depth(min_depth=3, min_kids=100)


def invert(piece):
    return piece.replace("#ffffff", "black").replace("#000000", "white")


for i, child in enumerate(sorted(q.all_children(), key=lambda x: x.depth)):
    p = random.choice(pieces)
    x = child.x0 * 0.9
    y = child.y0 * 0.9

    if child.depth % 2 == 0:
        pi = invert(p)
    else:
        pi = p

    sys.stderr.write(f"{i} - {x} {y} {child.width} {child.depth}\n")
    sys.stdout.write(piece(pi, offset=(x, y), scale=9 * 2 ** (1 + -child.depth)))


print(svg.footer())
