from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import telegram
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#셀레니움으로 키워드 사진 캡쳐
webdriver_options = webdriver.ChromeOptions()
webdriver_options .add_argument('headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=webdriver_options)

search_url='https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
search_word = "날씨"
driver.get(url = search_url+search_word)
driver.implicitly_wait(time_to_wait=10)

save_img_path = search_word + ".png"
driver.save_screenshot(save_img_path)

#텔레그램으로 전송
token = ""
id = ""

bot = telegram.Bot(token)
bot.sendPhoto(chat_id=id, photo = open(save_img_path, 'rb'), caption=save_img_path)
os.remove(save_img_path)