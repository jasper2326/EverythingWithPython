# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

"""
geohash_1.0.0.py
目前版本支持7个函数
encode(point): get geohash code of a point,
decode(hashcode): get lng&lat of a geohash,
get_8_neighbours(point): get 8 geohash neighbours of a point,
get_2(point): get downward geohash,
get_8(point): get upward geohash,
get_4(point): get leftward geohash,
get_6(point): get rightward geohash.
"""

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
    for i in range(precision):
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

def get_2(point, dlng=0.0001, dlat=0.0001):
    lng = point[0]
    lat = point[1]
    # get 2
    new_hashcode = hashcode = encode(point)
    new_lat = lat
    while (new_hashcode == hashcode):
        new_lat -= dlat
        new_hashcode = encode([lng, new_lat])
    return new_hashcode

def get_8(point, dlng=0.0001, dlat=0.0001):
    lng = point[0]
    lat = point[1]
    # get 2
    new_hashcode = hashcode = encode(point)
    new_lat = lat
    while (new_hashcode == hashcode):
        new_lat += dlat
        new_hashcode = encode([lng, new_lat])
    return new_hashcode

def get_4(point, dlng=0.0001, dlat=0.0001):
    lng = point[0]
    lat = point[1]
    # get 2
    new_hashcode = hashcode = encode(point)
    new_lng = lng
    while (new_hashcode == hashcode):
        new_lng -= dlng
        new_hashcode = encode([new_lng, lat])
    return new_hashcode

def get_6(point, dlng=0.0001, dlat=0.0001):
    lng = point[0]
    lat = point[1]
    # get 2
    new_hashcode = hashcode = encode(point)
    new_lng = lng
    while (new_hashcode == hashcode):
        new_lng += dlng
        new_hashcode = encode([new_lng, lat])
    return new_hashcode
