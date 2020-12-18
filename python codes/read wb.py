import xlrd
# pip install xlutils
from xlutils.copy import copy
book=xlrd.open_workbook('/Users/vickysharma/Desktop/python_codes/mysheet.xls')
print(book.nsheets)
print(book.sheet_names())
first_sheet=book.sheet_by_index(0)
print(first_sheet.row_values(0))
print(first_sheet.col_values(0)[0])
