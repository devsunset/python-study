from faker import Faker
import pandas as pd
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

fake = Faker("ko_KR")

fake_name_list = [fake.name() for i in range(10)]
fake_score_list = [random.randint(80,100) for i in range(10)]
fake_email_list = [fake.email() for i in range(10)]

print(fake_name_list)
print(fake_score_list)
print(fake_email_list)

df = pd.DataFrame({ '이름' :  fake_name_list,
                    '점수' :  fake_score_list,
                    '이메일' : fake_email_list
                    })

df.to_excel('이름_점수_이메일.xlsx')