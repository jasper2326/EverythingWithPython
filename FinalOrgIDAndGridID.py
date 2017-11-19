# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import xlrd
import neighbor

data_0 = xlrd.open_workbook('/Users/jasper/Desktop/2017-11-04-grid.xlsx')

table = data_0.sheets()[0]
data = []

row_num = table.nrows
#print row_num


for i in range(1, row_num, 1):
    org_id_1 = str(table.row_values(i)[0])[:-2]
    #print org_id
    grid_id_1 = set()
    grid_1 = str(table.row_values(i)[1])[:-2]
    grid_2 = str(table.row_values(i)[2])[:-2]
    grid_3 = str(table.row_values(i)[3])[:-2]
    grid_4 = str(table.row_values(i)[4])[:-2]
    grid_5 = str(table.row_values(i)[5])[:-2]
    grid_6 = str(table.row_values(i)[6])[:-2]
    grid_id_1.add(grid_1)
    grid_id_1.add(grid_2)
    grid_id_1.add(grid_3)
    grid_id_1.add(grid_4)
    grid_id_1.add(grid_5)
    grid_id_1.add(grid_6)
    grid_id_1.add('')
    grid_id_1.remove('')
    #print grid_id_1

    for j in range(i + 1, row_num, 1):
        org_id_2 = str(table.row_values(j)[0])[:-2]
        # print org_id
        if org_id_1 == org_id_2:
            continue
        grid_id_2 = set()
        grid_01 = str(table.row_values(j)[1])[:-2]
        grid_02 = str(table.row_values(j)[2])[:-2]
        grid_03 = str(table.row_values(j)[3])[:-2]
        grid_04 = str(table.row_values(j)[4])[:-2]
        grid_05 = str(table.row_values(j)[5])[:-2]
        grid_06 = str(table.row_values(j)[6])[:-2]
        grid_id_2.add(grid_01)
        grid_id_2.add(grid_02)
        grid_id_2.add(grid_03)
        grid_id_2.add(grid_04)
        grid_id_2.add(grid_05)
        grid_id_2.add(grid_06)
        grid_id_2.add('')
        grid_id_2.remove('')
        #print grid_id_2

        a = grid_id_1.intersection(grid_id_2)


        if len(a) >= 2:
            print(org_id_1, org_id_2, a)

