# author = Jasper_Jiao@ele.me
# -*- coding: utf-8 -*-


import Geohash

def is_point_in_path(point, poly):
    # x is latitude, y is longitude
    x, y = point
    # Number of vertices in polygon
    num = len(poly) - 1
    i, j, c = 0, num - 1, 0
    for i in range(num):
        # Pick adjacent vertices
        a, b = poly[i], poly[j]
        # Define the slope
        d = (b[0] - a[0]) / (b[1] - a[1] + 0.000000001)
        # In the triangle && under the line || In the rectangle formed by a&b
        # Count how many times point falls in the rectangle
        c += (a[1] > y) != (b[1] > y) and ((x - a[0]) < d * (y - a[1]))
        # Move to next vertices pair
        j = i
    # If c is an odd number, then it falls in polygon
    return c % 2 == 1

def get_geohash_list(poly, precision):
    data = [[-90.0, 90.0, 1],
            [-180.0, 180.0, 1]]
    # Define loop times
    for x in range(precision):
        data[0][2] += 2
        data[1][2] += 2
        data[x % 2][2] += 1

    border_rect = [[90.0, -90.0], [180.0, -180.0]]

    # Define the largest rectangle contains all vertices
    # Stored like [[min_lat, max_lat],
    #              [min_lng, max_lng]]
    for x in poly:
        border_rect[0][0] = min(border_rect[0][0], x[0])
        border_rect[0][1] = max(border_rect[0][1], x[0])
        border_rect[1][0] = min(border_rect[1][0], x[1])
        border_rect[1][1] = max(border_rect[1][1], x[1])

    # Divide and conquer to find latitude and longitude
    for k in (0, 1):
        a, b = border_rect[k]
        while True:
            mid = (data[k][0] + data[k][1]) / 2
            if mid < a:
                data[k][0] = mid
            elif mid > b:
                data[k][1] = mid
            else:
                break
            data[k][2] -= 1

    result = []
    a, b = 2 ** data[0][2], 2 ** data[1][2]
    # Moving distance for each geogrid on latitude and longitude
    dx, dy = (data[0][1] - data[0][0]) / a, (data[1][1] - data[1][0]) / b
    # Go through every grid in polygon
    for x in range(int(a)):
        for y in range(int(b)):
            lat, lon = data[0][0] + x * dx, data[1][0] + y * dy
            # Whether the grid is in polygon?
            if is_point_in_path((lat, lon), poly):
                # If yes, append geohash in the result list
                result.append(Geohash.encode([lat, lon, precision]))
    return set(result)