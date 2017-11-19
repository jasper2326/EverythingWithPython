# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import xlrd
import neighbor

data_0 = xlrd.open_workbook('/Users/jasper/Desktop/2017-11-08-test.xlsx')

table = data_0.sheets()[1]
data = []

row_num = table.nrows


# Create raw data
for i in range(row_num):
    first_grid = str(table.row_values(i)[0])[:-2]
    #print first_grid

    points = table.row_values(i)[1].split(';')
    poly = []
    for point in points:
        pair = []
        sub_pair = point.split(',')
        pair.append(float(sub_pair[0]))
        pair.append(float(sub_pair[1]))
        poly.append(pair)
    sub_result = []
    sub_result.append(first_grid)
    sub_result.append(poly)

    data.append(sub_result)

#print data


final_result = []

for i in range(len(data) - 1):
    grid_0 = int(data[i][0])
    poly_0 = data[i][1]
    #print grid_0
    #print poly_0
    first_poly = neighbor.get_geohash_list(poly_0, 7)
    index = i + 1
    #print first_poly
    #print index

    sub_result = set()
    sub_result.add(grid_0)

    for j in range(index, len(data)):
        grid_1 = int(data[j][0])
        poly_1 = data[j][1]
        second_poly = neighbor.get_geohash_list(poly_1, 7)
        if len(first_poly.intersection(second_poly)) != 0:
            sub_result.add(grid_1)
            print grid_0, grid_1

    final_result.append(sub_result)

final = []

for item in final_result:
    #print item,len(item)
    if len(item) != 1:
        final.append(item)


i = 0
while i <= len(final) - 1:
    a = final[i]
    #print a
    j = i + 1
    while j <= len(final) - 1:
        b = final[j]
        if a.intersection(b) != set({}):
            a = a.union(b)
            final.remove(b)
        else:
            j += 1
    i += 1


#print final
for item in final:
    #print item
    pass
