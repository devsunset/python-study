import telegram

token = "5400967414:AAEmAvwaQF6du8gny7A9upRniGvtHOi-Ro0"
id = "730238165"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")