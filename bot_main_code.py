import constants as const
import constantstr as consttr
import buttons as bt
import telebot
import time
import os
import monsters as mt

API_KEY = os.environ.get("API_KEY")
bot = telebot.TeleBot(API_KEY)
languagecounter = 0


@bot.message_handler(func=lambda msg: msg.text is not None)
def at_answer(message):
    global languagecounter
    text = message.text.lower()
    print(languagecounter)
    if text in ["start", "help", "english", "/start"]:
        bot.send_photo(message.chat.id, const.dev_photo,
                       caption=const.intro, reply_markup=bt.markuplanguage)
        # bot.send_sticker(message.chat.id,const.fire_thumbsUp)
        if text in ["english"]:
            languagecounter = 1
    elif text in ["başlat", "yardım", "yardim", "başla", "turkish"]:
        bot.send_photo(message.chat.id, const.dev_photo,
                       caption=consttr.intro, reply_markup=bt.markuplanguage)
        if text in ["turkish"]:
            languagecounter = 2
        # bot.send_sticker(message.chat.id,const.fire_thumbsUp)
    else:
        if languagecounter == 1:
            bot.send_message(message.chat.id, const.error)
        elif languagecounter == 2:
            bot.send_message(message.chat.id, consttr.error)
        else:
            bot.send_message(message.chat.id, const.error)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(1)
