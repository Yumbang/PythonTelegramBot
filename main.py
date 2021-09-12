import time
import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token='1986430016:AAG37he-O23D6GegnOZWRNymBeYS45QiNgo', use_context = True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello Human! I'm a bot!")

def echo(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)

def caps(update, context):
    text_caps = ''.join(context.args).upper()
    context.bot.send_message(chat_id = update.effective_chat.id, text = text_caps)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text &(~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)



updater.start_polling()







