import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token='1986430016:AAG37he-O23D6GegnOZWRNymBeYS45QiNgo', use_context = True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello Human! I'm a bot!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()












