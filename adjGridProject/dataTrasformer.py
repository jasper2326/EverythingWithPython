# author = Jasper_Jiao@ele.me
# -*- coding: utf-8 -*-


import xlrd
import Travel.neighbor

data_0 = xlrd.open_workbook('/Users/jasper/Desktop/yangzhou.xlsx')

table = data_0.sheets()[0]
data = []

row_num = table.nrows


# Create raw data
for i in range(1, 3, 1):
    city = int(table.row_values(i)[3])
    # print org
    org = int(table.row_values(i)[0])
    #print org
    grid = int(table.row_values(i)[1])
    #print first_grid

    points = table.row_values(i)[2].split(';')
    poly = []
    for point in points:
        pair = []
        sub_pair = point.split(',')
        #print sub_pair
        pair.append(float(sub_pair[0]))
        pair.append(float(sub_pair[1]))
        poly.append(pair)
    sub_result = []
    sub_result.append(city)
    sub_result.append(org)
    sub_result.append(grid)
    sub_result.append(poly)

    data.append(sub_result)


for item in data:
    print item