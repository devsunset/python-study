import win32com.client
import os

excel = win32com.client.Dispatch("Excel.Application")

load_file_path = r"C:\일잘러 파이썬과 40개의 작품들 코드\4.견적서에서 거래명세서 자동생성 후 PDF 변환\거래명세표_땡땡초등학교.xlsx"

wb = excel.Workbooks.Open(load_file_path)
ws_sheet = wb.ActiveSheet
ws_sheet.Select()

save_path = os.path.splitext(load_file_path)[0] + '.pdf'
wb.ActiveSheet.ExportAsFixedFormat(0, save_path)

wb.Close(False)
excel.Quit()