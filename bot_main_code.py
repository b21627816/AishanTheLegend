import constants as const
import telebot
import time
import os

API_KEY = os.environ.get("API_KEY")
bot = telebot.TeleBot(API_KEY)

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
    else:
        bot.send_message(message.chat.id,const.error)
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(1)