import telegram
from telegram import Updater
from telegram import MessageHandler, Filters
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def get_search_word_photo(search_word):
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options .add_argument('headless')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=webdriver_options)

    search_url='https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
    driver.get(url = search_url+search_word)
    driver.implicitly_wait(time_to_wait=10)

    save_img_path = search_word + ".png"
    driver.save_screenshot(save_img_path)
    return save_img_path


token = "5400967414:AAEmAvwaQF6du8gny7A9upRniGvtHOi-Ro0"
id = "730238165"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="뉴스 검색어를 입력해주세요. 검색결과를 사진으로 전송합니다.")

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text 
    print(user_text)
    save_img_path = get_search_word_photo(user_text)
    bot.sendPhoto(chat_id=id, photo = open(save_img_path, 'rb'), caption=save_img_path)
    os.remove(save_img_path)

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)