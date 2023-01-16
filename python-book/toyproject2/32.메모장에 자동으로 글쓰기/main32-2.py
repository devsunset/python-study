import telegram
from telegram import Updater
from telegram import MessageHandler, Filters
from pywinauto import Application


token = "5400967414:AAEmAvwaQF6du8gny7A9upRniGvtHOi-Ro0"
id = "730238165"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="메모장에 보여주는 단어를 입력하세요")

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def write_notepad(text):
    app = Application(backend="uia").start("notepad.exe")
    dig = app.window(title_re=".* 메모장")
    dig['최대화Button'].click()
    dig.Document.type_keys(text, with_spaces=True)

def handler(update, context):
    user_text = update.message.text 
    write_notepad(user_text)

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)