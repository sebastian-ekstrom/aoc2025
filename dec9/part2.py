import sys
import math

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

# checks if the ray (x1 + n, y1 + pi*n) intersects the edge
# use an irrational number as a slope to avoid hitting corners
def intersects(x1, y1, edge):
    x2_1, y2_1, x2_2, y2_2 = edge
    printd(f"intersection check: {(x1, y1)}, {(x2_1, y2_1)}, {(x2_2, y2_2)}")
    if x1 > x2_2 or y1 > y2_2:
        printd(f"point SE of edge, no intersection")
        return False
    if x2_1 == x2_2:
        y2_i = y1 + (x2_1 - x1) * math.pi
        printd(f"possible intersection point: {(x2_1, y2_i)}")
        return y2_1 <= y2_i <= y2_2
    elif y2_1 == y2_2:
        x2_i = x1 + (y2_1 - y1) / math.pi
        printd(f"possible intersection point: {(x2_i, y2_1)}")
        return x2_1 <= x2_i <= x2_2

# ray tracing method: if a ray from the point intersects the edges of the
# polygon an even number of times, the point is outside the polygon
def is_outside(x, y):
    intersections = 0
    for edge in edges:
        if intersects(x, y, edge):
            intersections += 1
    printd(f"{(x, y)}: {intersections} intersections")
    return intersections % 2 == 0

def edges_check_outside(edge1, edge2):
    if edge1 == edge2:
        return False
    x1_1, y1_1, x1_2, y1_2 = edge1
    x2_1, y2_1, x2_2, y2_2 = edge2
    # if the first edge intersects the second, part of it is outside
    if x1_1 == x1_2 and y2_1 == y2_2:
        return x2_1 < x1_1 < x2_2 and y1_1 < y2_1 < y1_2
    elif y1_1 == y1_2 and x2_1 == x2_1:
        return x1_1 < x2_1 < x1_2 and y2_1 < y1_1 < y2_1

    # if the first edge overlaps the second, it goes through a corner and might be
    # outside, so check the points just next to the corners
    if x1_1 == x1_2 and x2_1 == x2_2:
        if x1_1 != x2_1:
            return False
        if y1_1 < y2_1 and is_outside(x1_1, y2_1 - 1):
            return True
        if y1_2 > y2_2 and is_outside(x1_1, y2_2 + 1):
            return True
        return False
    if y1_1 == y1_2 and y2_1 == y2_2:
        if y1_1 != y2_1:
            return False
        if x1_1 < x2_1 and is_outside(x2_1 - 1, y1_1):
            return True
        if x1_2 > x2_2 and is_outside(x2_2 + 1, y1_1):
            return True
        return False




filename = sys.argv[1]
with open(filename) as file:
    tiles = [tuple(int(i) for i in line.strip().split(",")) for line in file]

edges = []
for n in range(len(tiles) + 1):
    if n < len(tiles) - 1:
        x1, y1 = tiles[n]
        x2, y2 = tiles[n + 1]
    else:
        x1, y1 = tiles[-1]
        x2, y2 = tiles[0]
    if (x1, y1) < (x2, y2):
        edges.append((x1, y1, x2, y2))
    else:
        edges.append((x2, y2, x1, y1))

max_area = 0
for m in range(len(tiles) - 1):
    x1, y1 = tiles[m]
    for n in range(m + 1, len(tiles)):
        x2, y2 = tiles[n]
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        if area <= max_area:
            continue

        area_edges = []
        for x in x1, x2:
            if y1 < y2:
                area_edges.append((x, y1, x, y2))
            else:
                area_edges.append((x, y2, x, y1))
        for y in y1, y2:
            if x1 < x2:
                area_edges.append((x1, y, x2, y))
            else:
                area_edges.append((x2, y, x1, y))

        outside = False
        for edge1 in area_edges:
            for edge2 in edges:
                if edges_check_outside(edge1, edge2):
                    outside = True
                    break
            if outside:
                break
        if not outside:
            max_area = area

print(max_area)
