import constants as const
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time
import os
from aishan_the_legend import test


API_KEY = os.environ['API_KEY']
print("Starting bot...")
print(API_KEY)
updater = Updater(API_KEY)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text('Hi!')


def test_bot(update, context):
    res = test()
    update.message.reply_text(res)


dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(CommandHandler('test', test_bot))

updater.start_polling()


""" 
@bot.message_handler(func=lambda msg: msg.text is not None)
def at_answer(message):
    text = message.text.lower()
    print(text)
    if text in ["start","help"]:
        bot.send_photo(message.chat.id,const.dev_photo,caption=const.intro)
        #bot.send_sticker(message.chat.id,const.fire_thumbsUp)
    elif text in ["başlat","yardım","yardim"]:
        bot.send_photo(message.chat.id,const.dev_photo,caption=const.introtr)
        #bot.send_sticker(message.chat.id,const.fire_thumbsUp)
    elif text in ["flask_test"]:
        bot.send_message(message.chat.id, test())
    else:
        bot.send_message(message.chat.id,const.error)
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(1) """
