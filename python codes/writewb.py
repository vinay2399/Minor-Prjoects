import xlwt
from datetime import datetime
wb=xlwt.Workbook()
ws=wb.add_sheet('sheet 1')
ws1=wb.add_sheet('sheet 2')
ws2=wb.add_sheet('sheet 3')
patt0=xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
patt1=xlwt.easyxf(num_format_str='DD-MM-YY')
ws.write(0,0,78.56,patt0)
ws.write(2,0,datetime.now(),patt1)
ws.write(3,0,1)
ws.write(4,0,1)
ws.write(5,0,xlwt.Formula('A4+A5'))
ws1.write(0,0,55.0,patt0)
ws2.write(0,0,'hello')
wb.save('mysheet.xls')


