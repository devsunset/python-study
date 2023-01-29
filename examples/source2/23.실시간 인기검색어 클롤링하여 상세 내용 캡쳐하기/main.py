
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL='https://www.google.co.kr'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)


from selenium.webdriver.common.by import By

URL='https://signal.bz/news'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10) 

naver_results = driver.find_elements(By.CSS_SELECTOR, '#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div > div > a')


#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(1) > a
#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(1) > a
#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(2) > a
#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div > div > a



naver_list = []
link_list = []
for naver_result in naver_results:
    print(naver_result.text.split("\n")[1])
    print(naver_result.get_attribute("href"))
    naver_list.append(naver_result.text.split("\n")[1])
    link_list.append(naver_result.get_attribute("href"))


for i,link in enumerate(link_list):
    print(naver_list[i],link)
    driver.get(url=link)
    driver.implicitly_wait(time_to_wait=10) 
    driver.save_screenshot(str(i+1) + '_' + naver_list[i] + ".png")

