# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import xlrd
import Travel.neighbor as nei
import xlwt
import time

start = time.clock()

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')

data_0 = xlrd.open_workbook('/Users/jasper/Desktop/page1.xlsx')

table = data_0.sheets()[0]
data = []

row_num = table.nrows


# Create raw data

for i in range(1, 1000):
    print('%4.2f' % (i*100.0/row_num) + '%')
    city = int(table.row_values(i)[3])
    org = int(table.row_values(i)[0])
    grid = int(table.row_values(i)[1])

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

    geo_list = nei.get_geohash_list(poly, 7)
    sub_result.append(geo_list)
    #print(sub_result)
    data.append(sub_result)



final_result = []

for i in range(0, len(data), 1):

    city_0 = data[i][0]
    org_0 = data[i][1]
    grid_0 = data[i][2]
    set_0 = data[i][4]
    j = i + 1

    for j in range(j, len(data), 1):

        elapsed = (time.clock() - start)
        print('Time used: ' + str(elapsed) + ' seconds')

        city_1 = data[j][0]
        org_1 = data[j][1]

        if city_0 != city_1 or org_0 != org_1:
            break

        grid_1 = data[j][2]
        set_1 = data[j][4]
        if len(set_1.intersection(set_0)) != 0:
            result = []
            result.append(city_0)
            result.append(org_0)
            result.append(grid_0)
            result.append(grid_1)
            print(city_0, org_0, grid_0, grid_1)
            final_result.append(result)

for i in range(0, len(final_result), 1):
    for j in range(0, 4, 1):
        worksheet.write(i, j, final_result[i][j])

workbook.save('Excel_Workbook2.xls')