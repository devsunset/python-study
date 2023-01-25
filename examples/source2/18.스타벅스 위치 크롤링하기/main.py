from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL='https://www.starbucks.co.kr/store/store_map.do?disp=locale'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)



from selenium.webdriver.common.by import By
import time

#지역검색 버튼 클릭
location_search = driver.find_element(By.CSS_SELECTOR,"#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a")
location_search.click()



#시/도를 모두 찾아 출력
location_list = driver.find_elements(By.CSS_SELECTOR,"#container > div > form > fieldset > div > section > article.find_store_cont > article > article > div.loca_step1 > div.loca_step1_cont > ul > li > a")
for location in location_list:
    print(location.text,end=",")



#전체 클릭
driver.find_element(By.CSS_SELECTOR,"#mCSB_2_container > ul > li:nth-child(1) > a").click()


#지역에서 데이터수집하여 출력
data_name_list = []
data_lat_list = []
data_long_list = []
매장_list = driver.find_elements(By.CSS_SELECTOR,"#mCSB_3_container > ul > li")
for 매장 in 매장_list:
    data_name_list.append(매장.get_attribute("data-name"))
    data_lat_list.append(매장.get_attribute("data-lat"))
    data_long_list.append(매장.get_attribute("data-long"))

print(data_name_list[0:10])
print(data_lat_list[0:10])
print(data_long_list[0:10])


#1.시/도 클릭 -> 2.전체 클릭 -> 3.데이터수집 -> 4.지역검색 버튼을 눌러 시/도로 이동
location_search = driver.find_element(By.CSS_SELECTOR,"#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a")
location_search.click()
location_list = driver.find_elements(By.CSS_SELECTOR,"#container > div > form > fieldset > div > section > article.find_store_cont > article > article > div.loca_step1 > div.loca_step1_cont > ul > li > a")

data_location_list = []
data_name_list = []
data_lat_list = []
data_long_list = []
for location in location_list:
    #1.시/도 클릭
    지역 = location.text
    print(지역,"[지역버튼] 클릭")
    location.click()
    time.sleep(3.0)

    #2.전체 클릭
    try:
        print("전체 클릭")
        driver.find_element(By.CSS_SELECTOR,"#mCSB_2_container > ul > li:nth-child(1) > a").click()
        time.sleep(3.0)
    except:
        print("전체가 없어 계속진행합니다")
        time.sleep(3.0)
    
    #3.데이터수집
    print(지역,"데이터수집중")
    매장_list = driver.find_elements(By.CSS_SELECTOR,"#mCSB_3_container > ul > li")
    for 매장 in 매장_list:
        data_location_list.append(지역)
        data_name_list.append(매장.get_attribute("data-name"))
        data_lat_list.append(매장.get_attribute("data-lat"))
        data_long_list.append(매장.get_attribute("data-long"))
    
    #4.지역검색 버튼을 눌러 시/도로 이동
    print("[지역검색버튼] 클릭")
    location_search.click()
    time.sleep(3.0)



import pandas as pd

df = pd.DataFrame()

print(data_location_list)
print(data_name_list)
print(data_lat_list)
print(data_long_list)

df["지역"] = data_location_list
df["이름"] = data_name_list
df["lat"] = data_lat_list
df["long"] = data_long_list

df.to_excel("스타벅스위치.xlsx")

