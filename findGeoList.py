import xlrd
import xlwt
import poly

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')


data_0 = xlrd.open_workbook('/Users/jasper/Desktop/gridPloy.xlsx')
table = data_0.sheets()[0]



row_num = table.nrows
print row_num

for i in range(825, 826, 1):
    print i
    grid_id = int(table.row_values(i)[0])
    geo_list = str(table.row_values(i)[2]).split(';')
    #print geo_list
    print grid_id
    outList = []
    for items in geo_list:
        inList = []
        inList.append(float(items.split(',')[0]))
        inList.append(float(items.split(',')[1]))
        outList.append(inList)
    #print outList
    geo_set = poly.get_geohash_list(outList, 7)
    print geo_set
    worksheet.write(i, 0, grid_id)
    worksheet.write(i, 1, str(geo_set))


#workbook.save('GridGeoList1.xls')