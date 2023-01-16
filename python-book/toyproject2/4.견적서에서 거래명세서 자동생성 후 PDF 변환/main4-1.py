from openpyxl import load_workbook

견적서_파일경로 = r"4.견적서에서 거래명세서 자동생성 후 PDF 변환\견적서_샘플.xlsx"

견적서_wb = load_workbook(견적서_파일경로, data_only=True)
견적서_ws = 견적서_wb.active

#하나의 셀 읽기
견적받는자 = 견적서_ws['A4'].value
소계 = 견적서_ws['X25'].value
부가세 =  견적서_ws['X26'].value
총합계금액 = 견적서_ws['X27'].value

print("견적받는자:",견적받는자)
print("소계:",소계)
print("부가세:",부가세)
print("총합계금액:",총합계금액)

#여러개의 셀 반복하여 읽기
품목명_list = []
수량_list = []
단가_list = []
금액_list = []
for data in 견적서_ws['C13':'X24']:
    for cell in data:
        if cell.column == ord('C')-64:
            if cell.value is not None:
                품목명_list.append(cell.value)
        if cell.column == ord('R')-64:
            if cell.value is not None:
                수량_list.append(cell.value)
        if cell.column == ord('T')-64:
            if cell.value is not None:
                단가_list.append(cell.value)
        if cell.column == ord('X')-64:
            if cell.value is not None:
                금액_list.append(cell.value)

print("품목명:",품목명_list)
print("수량:",수량_list)
print("단가:",단가_list)
print("금액:",금액_list)