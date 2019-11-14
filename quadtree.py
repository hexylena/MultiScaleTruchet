from dataclasses import dataclass
from dataclasses import field
import random
import svg

# quadtree
@dataclass
class Point:
    x: float
    y: float

@dataclass
class Node:
    x0: float
    y0: float
    width: float
    height: float
    children: list  = field(default_factory=list)
    enabled: bool = True
    depth: int = 1

    def subdivide(self):
        w_ = float(self.width/2)
        h_ = float(self.height/2)

        x1 = Node(self.x0, self.y0, w_, h_, depth=self.depth + 1)
        x2 = Node(self.x0, self.y0+h_, w_, h_, depth=self.depth + 1)
        x3 = Node(self.x0 + w_, self.y0, w_, h_, depth=self.depth + 1)
        x4 = Node(self.x0+w_, self.y0+h_, w_, h_, depth=self.depth + 1)

        self.children = [x1, x2, x3, x4]
        self.enabled = False

    def all_children(self):
        for child in self.children:
            yield from child.all_children()
        else:
            yield self

@dataclass
class QTree:
    root: Node

    def all_children(self, really_all=False):
        if really_all:
            yield from self.root.all_children()
        else:
            for child in self.root.all_children():
                if child.enabled:
                    yield child


def divided_tree(kids=25):
    root = Node(0, 0, 100, 100)
    q = QTree(root)

    while True:
        if len(list(q.all_children())) > kids:
            break

        kid = random.choice(list(q.all_children()))
        kid.subdivide()
    return q


if __name__ == '__main__':
    q = divided_tree()


    print(svg.header(author="GalPals", title="Multiscale Truchet"))

    for x in q.all_children():
        if x.enabled:
            colour = svg.random_color()
            # colour = ''.join(map(str, [x.depth * 2, colour[0], x.depth * 2, colour[1], x.depth * 2, colour[2]]))

            print(f"""
            <rect
            style="opacity:1;fill:#{colour};fill-opacity:1;stroke:none;stroke-width:0.1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke fill markers"
            width="{x.width}"
            height="{x.height}"
            x="{x.x0}"
            y="{x.y0}" />
                """)


    print(svg.footer())
