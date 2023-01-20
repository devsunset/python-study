from faker import Faker
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

fake = Faker("ko_KR")

가짜이름_list = [fake.name() for i in range(10)]
수험번호_list = ["2022-" + str(i+1).zfill(3) for i in range(10)]

print(가짜이름_list)
print(수험번호_list)

df = pd.DataFrame({ '이름' :  가짜이름_list,
                    '수험번호' :  수험번호_list
                    })

df.to_excel('수험번호.xlsx')