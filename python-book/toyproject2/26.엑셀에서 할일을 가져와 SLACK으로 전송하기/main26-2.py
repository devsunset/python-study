import pandas as pd
import time
import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    excel_file_path = '할일.xlsx'
    df_from_excel = pd.read_excel(excel_file_path)

    time_list = df_from_excel['시간'].tolist()
    todo_list = df_from_excel['할일'].tolist()

    now = datetime.datetime.now()
    print( now )
    for i,t in enumerate(time_list) :
        time_difference = t - now
        print(todo_list[i],time_difference.seconds)
        if time_difference.days >= 0 and time_difference.seconds <= 60:
            print(todo_list[i], " 메시지전송!!!")
            time.sleep(61.0)
    time.sleep(1.0)