# pip install python-telegram-bot
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

# token값은 telegram 에서 bot 생성시 확인
token = "token"

# bot id 확인
# bot = telegram.Bot(token=token)
# updates = bot.getUpdates()
# for u in updates:
#     print(u.message)

id = "bot_id"

# 메시지 보내기
# id = "bot_id"
# bot = telegram.Bot(token)
# bot.sendMessage(chat_id=id, text="hello world")


# 자동 응답 예제
bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="자동응답 테스트 입니다. 안녕 또는 뭐해 를 입력하여 보세요")

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text 
    if user_text == "안녕": 
        bot.send_message(chat_id=id, text="어 그래 안녕")
    elif user_text == "뭐해": 
        bot.send_message(chat_id=id, text="그냥 있어") 

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)