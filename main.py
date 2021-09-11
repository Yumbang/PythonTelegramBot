import telegram

bot = telegram.Bot(token='1986430016:AAG37he-O23D6GegnOZWRNymBeYS45QiNgo')

print('-------------------- BOT INFO ---------------------')
print(bot.get_me())


updates = bot.get_updates()

print('-------------------- UPDATED INFO -----------------')
print(updates[0])
