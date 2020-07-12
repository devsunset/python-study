# $ pip install selenium

# Firefox : https://github.com/mozilla/geckodriver/releases
# Chrome  : https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge    : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

# ADD PATH - drive install path

# -----------------------------------------------------------------------

from selenium import webdriver
import time

# Chrome 으로 파이썬 사이트 오픈 해서 PyPI 버튼 클릭 후 브라우져 닫기  
browser = webdriver.Chrome()  #  webdriver.Firefox() , webdriver.Edge()
browser.get("http://www.python.org") 
menus = browser.find_elements_by_css_selector('#top ul.menu li')

                # find_element_*() & find_elements_*()
                # find_element_by_id()
                # find_element_by_name()
                # find_element_by_class_name()
                # find_element_by_css_selector() 
pypi = None

for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)
 
pypi.click()  
time.sleep(5)
browser.quit()





# option 
# options = webdriver.ChromeOptions()
# options.add_argument('headless') # hidden으로 실행
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

# driver = webdriver.Chrome('chromedriver', chrome_options=options) 
# driver = webdriver.Chrome('chromedriver', options=options)