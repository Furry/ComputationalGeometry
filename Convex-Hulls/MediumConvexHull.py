import random
import matplotlib.pyplot as plt
import numpy as np

# Generate a random set of points
def generate_points(n):
    points = []
    for _ in range(n):
        points.append((random.randint(0, 100), random.randint(0, 100)))
    return points
#END

# Plot the points
def plot_points(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.scatter(x, y)
#END

def hull(points):
    # Unlike the Jarvis March, this algorithem will operate by rotating a line around the points,
    # finding the first point that would intersect the line, and then rotating the line around that point and so on.

    # Get the left most point
    left = points.index(min(points))

    # Start with the left most point.
    hull = [points[left]]
#END