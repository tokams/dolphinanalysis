import openpyxl
import csv
from time import gmtime, strftime

print("heheh")
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
wb = openpyxl.load_workbook('C:\workspace\dolphin\test.xlsx')
sh = wb.get_active_sheet()
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
with open('testsmall.csv', 'wb') as f:
    c = csv.writer(f)
    for r in sh.rows:
        c.writerow([cell.value for cell in r])
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
