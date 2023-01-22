import pandas as pd
import glob

재고_엑셀_파일들 = glob.glob('./재고_*.xlsx')
print(재고_엑셀_파일들)

merge_df = pd.DataFrame()
for 엑셀파일 in 재고_엑셀_파일들:
    df_from_excel = pd.read_excel(엑셀파일)
    df_from_excel['재고위치'] = 엑셀파일.split(".")[0]
    merge_df = pd.concat([merge_df,df_from_excel])
print(merge_df)


filter_df = merge_df[merge_df['날짜'] < '2015-01-01']
print("print로 출력")
print(filter_df)
print("\n값 출력")


filter_df = merge_df[merge_df['날짜'].between('2012-1-1', '2015-12-31')]
filter_df = merge_df[merge_df['날짜'].between('2012-1-1', '2015-12-31')]
filter_df = filter_df[filter_df['수량'] < 15]
filter_df.to_excel('날짜_수량.xlsx')
print(filter_df)

