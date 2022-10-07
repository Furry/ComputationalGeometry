import heapq
import random
import numpy as np
import matplotlib.pyplot as plt

from structs import Node, BalancedSearchTree

# from binarytree import Node
# from binarytree import tree
# from binarytree import build

class Point:
    def __init__(self, x, y, segment):
        self.x = x
        self.y = y
        self.segment = segment
    #END

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        else:
            return self.y > other.y
        #END
    #END

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    #END
#END

class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1, self)
        self.p2 = Point(x2, y2, self)
    #END

    def __repr__(self):
        return str(self.p1) + " -> " + str(self.p2)
    #END

    def __lt__(self, other):
        # Cross product between s1 and s2
        s1p1 = self.p1
        s1p2 = self.p2
        s2p1 = other.p1
        s2p2 = other.p2

        cross = (s1p2.y - s1p1.y) * (s2p2.x - s2p1.x) - (s1p2.x - s1p1.x) * (s2p2.y - s2p1.y)

        if cross == 0:
            return False
        elif cross > 0:
            return True
        else:
            return False
        #END
    #END

    def points(self):
        return (self.p1, self.p2)
    #END
#END

class Queue:
    def __init__(self):
        self.queue = []
    #END

    def push(self, point):
        self.queue.append(point)
        self.queue = sorted(self.queue, key=lambda k: [k.y, k.x], reverse=True)
    #END

    def pop(self):
        x = self.queue.pop()
        self.queue = sorted(self.queue, key=lambda k: [k.y, k.x], reverse=True)
        return x
    #END

    def __repr__(self):
        return str(self.queue)
    #END
#END

def generate_lines(n):
    points = []
    for _ in range(n):
        points.append(
            Segment(
                random.randint(-100, 100),
                random.randint(-100, 100),
                random.randint(-100, 100),
                random.randint(-100, 100)
            )
        )
    return points
#END

# segments = generate_lines(10)

def find_intersections(s):
    ""
#END

q = Queue()
tree = BalancedSearchTree()
for s in generate_lines(10):
    tree.insert(s)
#END

for s in tree.traverse():
    # Plot with matplotlib
    x = [s.p1.x, s.p2.x]
    y = [s.p1.y, s.p2.y]
    plt.plot(x, y, label=s)
#END

plt.legend()

plt.show()