# Implement the two TSP heuristics of Section 1.1 (page 5). Which of them gives better-quality solutions in practice?
# Can you devise a heuristic that works better than both of them

import random


class Point:
    """
    Point class represents a point in 2D space
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, point):
        # Pythagorean theorem
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def nearestNeighbour(self, points):
        # Find the nearest neighbour to the current point
        # nearest = None
        nearestKey = None
        nearestDistance = float('inf')
        for key, point in points.items():
            distance = self.distanceTo(point)
            if distance < nearestDistance:
                # nearest = point
                nearestDistance = distance
                nearestKey = key
        return nearestKey


def tour(points):
    remaining_points = points.copy()
    tour_path = []
    # Start at a random point
    current_key = random.choice(list(remaining_points.keys()))
    while remaining_points:
        current_point = remaining_points[current_key]
        tour_path.append(current_key)
        # Remove the current point from the remaining
        del remaining_points[current_key]
        current_key = current_point.nearestNeighbour(remaining_points)
    return tour_path


# Generate 10 random points
points = {}

for i in range(10):
    points[i] = Point(random.randint(0, 100),
                      random.randint(0, 100))

print("{")
for key in points:
    cur = points[key]
    print(str(key) + ":", cur.x, str(cur.y) + ",")
print("}")

# print(points)
print(tour(points))
