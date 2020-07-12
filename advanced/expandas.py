# $ pip install pandas

# https://github.com/minsuk-heo/pandas
# https://github.com/minsuk-heo/pandas/blob/master/%ED%8C%AC%EB%8D%94%EC%8A%A4_%EB%AA%85%EB%A0%B9%EC%96%B4_%EA%BF%80%ED%8C%81.ipynb

import pandas as pd

# Series
data = [1, 3, 5, 7, 9]
s = pd.Series(data)
print(s)
print('-------------------------------- case 1')


# DataFrame
data = {
    'year': [2018, 2019, 2020],
    'gender': ['M', 'W', 'A'],
    'count': [10, 20, 30]
}
 
df = pd.DataFrame(data)
print(df)
print('--------------------------------')

data_dic = [
    {'year':2018,'gender': 'M', 'count':10},
    {'year':2019,'gender': 'W', 'count':20},
    {'year':2020,'gender': 'A', 'count':20}
]

df = pd.DataFrame(data_dic)
df  = df[['gender','count','year']]
print(df)
print('--------------------------------')

from collections import OrderedDict

friend_ordered_dict = OrderedDict([ ('name', ['John', 'Jenny', 'Nate']),
          ('age', [20, 30, 30]),
          ('job', ['student', 'developer', 'teacher']) ] )
df = pd.DataFrame.from_dict(friend_ordered_dict)
print(df.head())
print('-------------------------------- case 2')


# Write csv file
df.to_csv('dataframe.csv') # 확장자는 뭐든지 상관 없음
# df.to_csv('dataframe.csv',index=False,header=False,na_rep='-')
print('DataFrame to csv file')
print('-------------------------------- case 3')


# Read csv file
df = pd.read_csv('test.csv') 
# df = pd.read_csv('test.txt')                  # *.txt file read
# df = pd.read_csv('test.tsv',delimiter='\t')   # 구분자 지정 

# df = pd.read_csv('test_sub.csv',header=None)  # Header 없는 파일
# df.columns = ['order','type','result']        # Header 값 부여
# df = pd.read_csv('test_sub.csv',header=None,names = ['order','type','result'])      # 위의 2줄 내용 한번에 처리
print(df)
# print(df.head()) # 앞에서
# print(df.head(1))
# print(df.tail()) # 뒤에서
# print(df.tail(1)) 
print('-------------------------------- case 4')