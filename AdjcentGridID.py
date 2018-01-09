# author = Jasper_Jiao@ele.me
# -*- coding: utf-8 -*-


import xlrd
import Travel.neighbor as neighbor
import xlwt
import time

start = time.clock()

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')

data_0 = xlrd.open_workbook('/Users/jasper/Desktop/')

table = data_0.sheets()[0]
data = []

row_num = table.nrows


# Create raw data
for i in range(1, row_num):

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

print(data)


final_result = []

for i in range(0, len(data), 1):

    city_0 = data[i][0]
    org_0 = data[i][1]
    grid_0 = data[i][2]
    poly_0 = data[i][3]

    j = i + 1

    for j in range(j, len(data), 1):
        elapsed = (time.clock() - start)
        print('Time used: ' + str(elapsed) + ' seconds')

        city_1 = data[j][0]
        org_1 = data[j][1]
        if city_0 != city_1 or org_0 != org_1:
            break

        grid_1 = data[j][2]
        poly_1 = data[j][3]
        first_poly = neighbor.get_geohash_list(poly_0, 7)
        second_poly = neighbor.get_geohash_list(poly_1, 7)
        if len(first_poly.intersection(second_poly)) != 0:
            result = []
            result.append(city_0)
            result.append(org_0)
            result.append(grid_0)
            result.append(grid_1)
            print (city_0, org_0, grid_0, grid_1)
            final_result.append(result)


##Writer

for i in range(0, len(final_result), 1):
    for j in range(0, 4, 1):
        worksheet.write(i, j, final_result[i][j])

workbook.save('Excel_Workbook1.xls')




#for item in final_result:
#    print item


#final = []
#
#for item in final_result:
#    #print item,len(item)
#    if len(item) != 1:
#        final.append(item)
#
#
#i = 0
#while i <= len(final) - 1:
#    a = final[i]
#    #print a
#    j = i + 1
#    while j <= len(final) - 1:
#        b = final[j]
#        if a.intersection(b) != set({}):
#            a = a.union(b)
#            final.remove(b)
#        else:
#            j += 1
#    i += 1
#
#
##print final
#for item in final:
#    print item