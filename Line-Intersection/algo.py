import heapq
import random
import numpy as np

class Point:
    def __init__(self, x, y, segment):
        self.x = x
        self.y = y
        self.segment = segment
    #END

    def __gt__(self, other):
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

    def points(self):
        return (self.p1, self.p2)
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

segments = generate_lines(10)
points = np.array([p.points() for p in segments]).flatten().tolist()
heapq._heapify_max(points)

print(points)

def find_intersections(s):
    Q = []
    heapq._heapify_max(Q)
