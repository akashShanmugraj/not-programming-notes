
The QuickHull algorithm is used to find the convex hull of a set of points in a plane. The convex hull is the smallest convex polygon that encloses all the given points. QuickHull is a divide-and-conquer algorithm that works similarly to QuickSort.

### Pseudocode

1. **Input**:
    - `points[]`: Array of points where each point is represented as a tuple `(x, y)`.

2. **Output**:
    - Convex hull points in counter-clockwise order.

### Pseudocode

```python
procedure quickHull(points):
    if length(points) < 3:
        return points
    
    def findSide(p1, p2, p):
        val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
        if val > 0:
            return 1
        elif val < 0:
            return -1
        return 0

    def distance(p1, p2, p):
        return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

    def hull(p1, p2, points, side):
        ind = -1
        max_dist = 0
        for i in range(len(points)):
            temp = distance(p1, p2, points[i])
            if findSide(p1, p2, points[i]) == side and temp > max_dist:
                ind = i
                max_dist = temp

        if ind == -1:
            hull_points.add(p1)
            hull_points.add(p2)
            return

        hull(points[ind], p1, [points[i] for i in range(len(points)) if findSide(points[ind], p1, points[i]) == -side], -findSide(points[ind], p1, p2))
        hull(points[ind], p2, [points[i] for i in range(len(points)) if findSide(points[ind], p2, points[i]) == -side], -findSide(points[ind], p2, p1))

    min_x = min(points, key=lambda p: p[0])
    max_x = max(points, key=lambda p: p[0])

    hull_points = set()

    hull(min_x, max_x, points, 1)
    hull(min_x, max_x, points, -1)

    return list(hull_points)

# Example usage
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
print(quickHull(points))  # Output: convex hull points
```

### Explanation

1. **Initialization**:
    - If there are fewer than three points, return the points themselves as the convex hull.
    - Find the points with the minimum and maximum x-coordinates, `min_x` and `max_x`. These points are guaranteed to be part of the convex hull.

2. **Helper Functions**:
    - `findSide(p1, p2, p)`: Determines the side of point `p` relative to the line formed by `p1` and `p2`. Returns 1 if `p` is on one side, -1 if on the other, and 0 if collinear.
    - `distance(p1, p2, p)`: Computes the perpendicular distance of point `p` from the line formed by `p1` and `p2`.

3. **Hull Function**:
    - Given two points `p1` and `p2` and a set of points, find the point with the maximum distance from the line `p1` to `p2` that is on the specified side.
    - If no such point exists, add `p1` and `p2` to the set of hull points.
    - Recursively find the hull points on either side of the line formed by the newly found point and `p1` and `p2`.

4. **Recursive Division**:
    - Recursively apply the `hull` function to divide the problem into smaller subproblems.
    - Start with the line segment between `min_x` and `max_x`, and find hull points on both sides of this line.

5. **Result**:
    - Collect all points identified as part of the convex hull and return them.

### Example Trace

Consider the example:

- Points: `[(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]`

1. **Initialization**:
    - `min_x = (0, 0)`
    - `max_x = (3, 3)`

2. **Recursive Hull Calculation**:
    - Divide the points into those on the left and right of the line `min_x` to `max_x`.
    - Recursively find the farthest points and build the convex hull.

By following the pseudocode and explanation, the QuickHull algorithm efficiently finds the convex hull of a set of points using a divide-and-conquer strategy.