import os
import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

tokenFile = open("token.txt", 'r')
tokenString =tokenFile.read()
print(tokenString)
tokenFile.close()


updater = Updater(token=tokenString, use_context = True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello Human! I'm a bot!")

def echo(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)

def caps(update, context):
    text_caps = ''.join(context.args).upper()
    context.bot.send_message(chat_id = update.effective_chat.id, text = text_caps)

def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
            InlineQueryResultArticle(
                    id = query.upper(),
                    title = "Caps",
                    input_message_content = InputTextMessageContent(query.upper())
                )
            )
    context.bot.answer_inline_query(update.inline_query.id, results)

def unknown(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Sorry, I don't understand.")



start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text &(~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.start_polling()







