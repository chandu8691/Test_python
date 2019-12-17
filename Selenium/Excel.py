# import xlrd
# loc="C:\\Users\\kodiak\\Desktop\\info.xlsx"
# wb=xlrd.open_workbook(loc)
# sheet1=wb.sheet_by_index(0)
# #print(sheet1.cell_value(4,1))
# row=sheet1.nrows
# col=sheet1.ncols
# for i in range(0,row):
#     print(sheet1.cell_value(i,1))

from xlwt import Workbook
wb=Workbook()
sheet1=wb.add_sheet('sheet1')
sheet1.write(1,0,'jandj')
sheet1.write(2,0,'hjda')
sheet1.write(3,0,'aueyui')
sheet1.write(4,0,'auyooi')
sheet1.write(0,1,'ASAD')
sheet1.write(0,2,'SHSJKNH')
sheet1.write(0,3,'SHGJSH')

wb.save("C:\\Users\\kodiak\\Desktop\\write.xls")

