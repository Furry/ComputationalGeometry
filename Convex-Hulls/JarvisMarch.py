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

# Get the orientation using the cross product
def get_orientation(p1, p2, p3):
    cross = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    if cross == 0:
        return "collinear"
    elif cross > 0:
        return "clockwise"
    else:
        return "counterclockwise"
#END

def hull(points):
    # Get the left most point
    left = points.index(min(points))

    # Start with the left most point.
    hull = [points[left]]

    while True:
        # Get the next point
        right = (left + 1) % len(points)
        for i in range(len(points)):
            # Test it's orientation, if it's counter clockwise, it's the next point if not continue.
            if get_orientation(hull[-1], points[right], points[i]) == "counterclockwise":
                right = i
        if points[right] == hull[0]: # This means we've looped around the list to the start point.
            break

        # Add the next point to the hull,
        hull.append(points[right])

        # Set the left point to the current (next right angled) point
        left = right
    return hull
#END

print("Convex Hull")
points = generate_points(8)
plot_points(points)
hull = hull(points)
x = [p[0] for p in hull]
y = [p[1] for p in hull]
plt.plot(x, y, 'r')
# graph from last to first
x.append(x[0])
y.append(y[0])
plt.plot(x, y, 'r')
plt.show()
