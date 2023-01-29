
#데이터 읽기
import pandas as pd

file_path = "01_01_01_P.xlsx"
df = pd.read_excel(file_path)
print(len(df))



#column 이름 확인
for i, col in enumerate(df.columns):
    i += 1
    if i % 5 == 0:
        print(i, col)
    else:
        print(i, col, end=",")


# 소재지전체주소에서 값이 없으면 도로명전체주소값으로 대체하여 "주소" 에 저장
import numpy as np

df['주소'] = np.where(pd.notnull(df['도로명전체주소']) == True, df['도로명전체주소'], df['소재지전체주소'])

print("소재지전체주소 빈 데이터 수",df["소재지전체주소"].isnull().sum()) # numll 확인
print("도로명전체주소 빈 데이터 수",df["도로명전체주소"].isnull().sum()) # numll 확인
print("주소 빈 데이터 수",df["주소"].isnull().sum()) # numll 확인

df.to_excel("결과확인.xlsx")

# 상세영업상태명  에서 폐업의 수와, 영업중 수 확인
print("폐업: ",(df["상세영업상태명"].str.contains('영업중',na=False) == False).sum())
print("영업중: ",df["상세영업상태명"].str.contains('영업중').sum())


# 주소에서 시/도 주소만 분리하여 저장
df['시도주소'] = df['주소'].str.split(" ")

# 시 + 도 로 "시도주소"에 저장
df['시도주소'] = df['시도주소'].str.get(0) +" " +df['시도주소'].str.get(1)
print(df['시도주소'])


# 시도 이름으로 묶고, 병원수가 많은 20개의 순서대로 출력하기
new_df = pd.DataFrame()
new_df["병원수"] = df.groupby('시도주소').size()
new_df["순위"] = new_df['병원수'].rank(ascending=False)
new_df["순위"] = new_df["순위"].astype(int)
new_df.sort_values(by='순위')[0:20]

