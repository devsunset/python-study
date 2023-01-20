# pip install selenium
# pip install webdriver-manager

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

#naver_results = driver.find_elements_by_css_selector('#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div > div > a > span.rank-text')

naver_results = driver.find_elements(By.CSS_SELECTOR, '#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div > div > a > span.rank-text')

naver_list = []
for naver_result in naver_results:
    print(naver_result.text)
    naver_list.append(naver_result.text)

print("=================================")

URL='https://www.nate.com'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

#driver.find_element_by_css_selector('#olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank').click()

driver.find_element(By.CSS_SELECTOR,'#olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank').click()

#nate_results = driver.find_elements_by_css_selector('#search-option > form:nth-child(1) > fieldset > div.issue-kwd > span > a')

nate_results = driver.find_elements(By.CSS_SELECTOR,'#search-option > form:nth-child(1) > fieldset > div.issue-kwd > span > a')

nate_list = []
for nate_result in nate_results:
    print(nate_result.text)
    nate_list.append(nate_result.text)

print("=================================")

import time

URL='https://zum.com'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10) 

#driver.find_element_by_css_selector('#app > div > header > div.search_bar > div > fieldset > div > input[type=text]').send_keys("아무거나 검색")
driver.find_element(By.CSS_SELECTOR,'#app > div > header > div.search_bar > div > fieldset > div > input[type=text]').send_keys("아무거나 검색")
time.sleep(0.5)
#driver.find_element_by_css_selector('#app > div > header > div.search_bar > div > fieldset > div > button.search').click()
driver.find_element(By.CSS_SELECTOR,'#app > div > header > div.search_bar > div > fieldset > div > button.search').click()
time.sleep(1)

#zoom_results = driver.find_elements_by_css_selector('#issue_wrap > ul > li > div > a:nth-child(1) > span.txt')
zoom_results = driver.find_elements(By.CSS_SELECTOR,'#issue_wrap > ul > li > div > a:nth-child(1) > span.txt')

zoom_list = []
for zoom_result in zoom_results:
    print(zoom_result.text)
    zoom_list.append(zoom_result.text)

print("=================================")

print("네이버",naver_list)
print("네이트",nate_list)
print("줌",zoom_list)

