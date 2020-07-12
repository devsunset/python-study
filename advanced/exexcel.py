# $ pip install openpyxl

import openpyxl
 
wb = openpyxl.load_workbook('test.xlsx')

# 활성화된 Sheet 구하기 
ws = wb.active

# Sheet 명칭으로 구하기 
# ws = wb.get_sheet_by_name("Sheet1")
 
for r in ws.rows:
    row_index = r[0].row   
    one = r[1].value
    two = r[2].value
    three = r[3].value
    sum = one + two + three

    ws.cell(row=row_index, column=5).value = sum 
    
    print(one, two, three, sum)
 
wb.save("test.xlsx")
wb.close()