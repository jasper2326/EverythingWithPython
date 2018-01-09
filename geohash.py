# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import math

try:
    import _geohash
except ImportError:
    _geohash = None

__version__ = "0.1.0"
__all__ = ['encode', 'decode', 'get_8_neighbours', 'get_list_in_polygon']



def encode(point):
    lat = 90
    lng = 180
    lat_code = []
    lng_code = []
    geo = []
    x = float(point[0])
    y = float(point[1])
    precision = 7
    precision = precision * 5 / 2 + 1
    for i in range(int(precision)):
        if x >= 0:
            lng_code.append(1)
            geo.append(1)
            lng /= 2.0
            x -= lng
        else:
            lng_code.append(0)
            geo.append(0)
            lng /= 2.0
            x += lng
        if y >= 0:
            lat_code.append(1)
            geo.append(1)
            lat /= 2.0
            y -= lat
        else:
            lat_code.append(0)
            geo.append(0)
            lat /= 2.0
            y += lat
    # print lat_code
    # print lng_code
    # print geo


    num_array = []
    while len(geo) >= 5:
        subgeo = geo[0:5]
        num_array.append(trans_hashcode_to_10(subgeo))
        geo = geo[5:]

    base_32 = 'abcdefghijklmnopqrstuvwxyz234567'
    # print len(_base_32)

    base_32_map = {}
    for i in range(len(base_32)):
        base_32_map[i] = base_32[i]
    # print base_32_map
    # Release i
    del i
    char_array = []
    for num in num_array:
        # print num
        hash = base_32_map[num]
        # print hash
        char_array.append(hash)

    string = ''
    for num in char_array:
        string += num
    return string

def trans_hashcode_to_10(subgeo):
    result = 0
    power = 1
    while len(subgeo) != 0:
        if subgeo[-1] == 1:
            result += power
        power = power * 2
        subgeo = subgeo[:-1]
    # print result
    return result

    # trans_hashcode_to_10(11101)

def decode(hashcode):
    base_32 = 'abcdefghijklmnopqrstuvwxyz234567'
    base_32_map_inverse = {}
    for i in range(len(base_32)):
        base_32_map_inverse[base_32[i]] = i
    # print base_32_map_inverse


    num_array = []
    for i in range(len(hashcode)):
        c = hashcode[i]
        num_array.append(base_32_map_inverse[c])

    char_array_0 = []
    for num in num_array:
        char_array_0.append(bin(num))

    char_array = ''
    for char in char_array_0:
        char = char[2:]
        while len(char) != 5:
            char = '0' + char
        char_array += char

    lng_code = ''
    lat_code = ''
    for i in range(0, len(char_array), 2):
        lng_code += char_array[i]
    for i in range(1, len(char_array), 2):
        lat_code += char_array[i]

    # print lat_code
    # print lng_code

    lat = 90
    lat_now = -90
    for char in lat_code:
        if char == '1':
            lat_now += lat
        lat = lat / 2.0

    lng = 180
    lng_now = -180
    for char in lng_code:
        if char == '1':
            lng_now += lng
        lng = lng / 2.0

    return [lng_now, lat_now]

def get_8_neighbours(point):
    neighbors = []
    hashcode = encode(point)
    neighbors.append(hashcode)

    dlng = 0.0001
    dlat = 0.0001

    hash_2 = get_2(point, dlng, dlat)
    hash_4 = get_4(point, dlng, dlat)
    hash_6 = get_6(point, dlng, dlat)
    hash_8 = get_8(point, dlng, dlat)
    hash_1 = get_4(decode(hash_2), dlng, dlat)
    hash_7 = get_4(decode(hash_8), dlng, dlat)
    hash_3 = get_6(decode(hash_2), dlng, dlat)
    hash_9 = get_6(decode(hash_8), dlng, dlat)

    neighbors.append(hash_2)
    neighbors.append(hash_4)
    neighbors.append(hash_6)
    neighbors.append(hash_8)
    neighbors.append(hash_1)
    neighbors.append(hash_3)
    neighbors.append(hash_7)
    neighbors.append(hash_9)
    return neighbors

def get_2(point, dlng, dlat):
    lng = point[0]
    lat = point[1]
    # get 2
    new_hashcode = hashcode = encode(point)
    new_lat = lat
    while (new_hashcode == hashcode):
        new_lat += dlat
        new_hashcode = encode([lng, new_lat])
    return new_hashcode

def get_8(point, dlng, dlat):
    lng = point[0]
    lat = point[1]
    # get 2
    new_hashcode = hashcode = encode(point)
    new_lat = lat
    while (new_hashcode == hashcode):
        new_lat -= dlat
        new_hashcode = encode([lng, new_lat])
    return new_hashcode

def get_4(point, dlng, dlat):
    lng = point[0]
    lat = point[1]
    # get 2
    new_hashcode = hashcode = encode(point)
    new_lng = lng
    while (new_hashcode == hashcode):
        new_lng -= dlng
        new_hashcode = encode([new_lng, lat])
    return new_hashcode

def get_6(point, dlng, dlat):
    lng = point[0]
    lat = point[1]
    # get 2
    new_hashcode = hashcode = encode(point)
    new_lng = lng
    while (new_hashcode == hashcode):
        new_lng += dlng
        new_hashcode = encode([new_lng, lat])
    return new_hashcode




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
        d = (b[0] - a[0]) / (b[1] - a[1] + 0.0000001)
        # In the triangle && under the line || In the rectangle formed by a&b
        # Count how many times point falls in the rectangle
        c += (a[1] > y) != (b[1] > y) and ((x - a[0]) < d * (y - a[1]))
        # Move to next vertices pair
        j = i
    # If c is an odd number, then it falls in polygon
    return c % 2 == 1

def get_geohash_list(poly):
    data = [[-90.0, 90.0, 1],
            [-180.0, 180.0, 1]]
    # Define loop times
    for x in range(7):
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
            if is_point_in_path([lat, lon], poly):
                # If yes, append geohash in the result list
                result.append(encode([lat, lon]))
    return result


print(get_8_neighbours([123.456789, 23.456789]))
