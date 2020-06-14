import distance as distance

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]
non_quadrant = []
quadrant_1 = ("Quadrant 1")
quadrant_2 = ("Quadrant 2")
quadrant_3 = ("Quadrant 3")
quadrant_4 = ("Quadrant 4")
total_quadrant_1 = 0
total_quadrant_2 = 0
total_quadrant_3 = 0
total_quadrant_4 = 0
closest_distance_to_the_center = []

from scipy.spatial import distance
for point in points:
    print("Euclidean distance: ", distance.euclidean(point[0], point[1]))
    if point[0] + point[1] == 0:
        non_quadrant.append(point)
    elif point[0] == 0 or point[1] == 0:
        non_quadrant.append(point)
    # print(point)

    if point[0] == 0 or point[1] == 0:
        print("Out of quandrant")
    if point[0] > 0 and point[1] > 0:
        total_quadrant_1 += 1
        print("The arrow hits the ", quadrant_1)
    if point[0] < 0 and point[1] > 0:
        total_quadrant_2 += 1
        print("The arrow hits the ", quadrant_2)
    if point[0] < 0 and point[1] < 0:
        total_quadrant_3 += 1
        print("The arrow hits the ", quadrant_3)
    if point[0] > 0 and point[1] < 0:
        total_quadrant_4 += 1
        print("The arrow hits the ", quadrant_4)
print("\n")
print("Quadrant 1: ", total_quadrant_1, " hits.")
print("Quadrant 2: ", total_quadrant_2, " hits.")
print("Quadrant 3: ", total_quadrant_3, " hits.")
print("Quadrant 4: ", total_quadrant_4, " hits.")
print("Arrow out of quadrant!", non_quadrant)

import collections
print("The replicated strikes are:", [item for item, count in collections.Counter(points).items() if count > 1])