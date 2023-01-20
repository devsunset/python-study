import telegram

token = '5400967414:AAEmAvwaQF6du8gny7A9upRniGvtHOi-Ro0'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)