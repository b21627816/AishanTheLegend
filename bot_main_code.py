import constants as const
import constantstr as consttr
import buttons as bt
import telebot
import time
import os,combat
import monsters as mt
import player as pl
import random

character = pl.player
API_KEY = os.environ.get("API_KEY")
bot = telebot.TeleBot(API_KEY)
languagecounter = 0
@bot.message_handler(func=lambda msg: msg.text is not None)
def at_answer(message):
    global character
    global languagecounter
    text = message.text.lower()
    healcheck = text
    if text in ["start","help","english","/start"]:
        character.healcondition(0)
        bot.send_message(message.chat.id,const.menu,reply_markup=bt.markupmenu)
        #bot.send_photo(message.chat.id,const.dev_photo,caption=const.menu,reply_markup=bt.markuplanguage)
        #bot.send_sticker(message.chat.id,const.fire_thumbsUp)
        if text in ["english"]:
            languagecounter = 1
    elif text in ["başlat","yardım","yardim","başla","turkish"]:
        bot.send_photo(message.chat.id,const.dev_photo,caption=consttr.beta,reply_markup=bt.markuplanguage)
        if text in ["turkish"]:
            languagecounter = 1
        #bot.send_sticker(message.chat.id,const.fire_thumbsUp)
    elif text in ["inventory","inv"]:
        character.healcondition(0)
        inventory = const.inv
        if character.inv() == 32:
            inventory = inventory + "\nThere is no item in your inventory!"
        else:
            for item in character.inv():
                inventory = inventory + "\n-" + str(item)
        bot.send_message(message.chat.id,inventory,reply_markup=bt.markupmenu)
    elif text in ["hunt","ht"]:
        character.healcondition(0)
        monster = combat.pickmonster(character.lvl())
        result = combat.fight(monster.id,monster.hp,monster.power,monster.xp,character.health(),character.power())
        if result == 255:
            character.hpconfig(100)
            bot.send_message(message.chat.id,const.healer,reply_markup=bt.markupmenu)
        elif result == 0:
            character.hpconfig(0)
            bot.send_message(message.chat.id,const.lost,reply_markup=bt.markupmenu)
        elif result[0] >=1:
            character.repxp(result[0])
            character.dechp(result[1])
            win = "You defeat the " + str(monster.name) +" and earn " + str(result[0]) + " xp. And you lost " + str(result[1]) + " hp! You may rest!"
            bot.send_message(message.chat.id,win,reply_markup=bt.markupmenu)
    elif text in ["rest","rst"]:
        character.healcondition(1)
        print(character.healing())
        bot.send_message(message.chat.id,"While resting, your hp will increase 1 per second. When your hp full you will be notified.",reply_markup=bt.markupmenu)
        while character.health() < 100:
            if character.healing() == 0 :
                break
            character.inchp(1)
            time.sleep(1)
        if character.healing() == 1 :
            bot.send_message(message.chat.id,"Your full! Current hp : " + str(character.health()),reply_markup=bt.markupmenu)
        else:
            bot.send_message(message.chat.id,"Current hp : " + str(character.health()),reply_markup=bt.markupmenu)
    elif text in ["profile","prf"]:
        character.healcondition(1)
        profile_feedback = "\tYour level : " + str(character.lvl()) + "\nYour hp : " + str(character.health()) + "\nEquipped Weapon : " + character.usedweapon() + "\nCurrent Exp: : " + str(character.experience())
        bot.send_message(message.chat.id,profile_feedback,reply_markup=bt.markupmenu)
    else:
        character.healcondition(0)
        if languagecounter == 1:
            bot.send_message(message.chat.id,const.error)
        elif languagecounter == 2:
            bot.send_message(message.chat.id,consttr.error)
        else:
            bot.send_message(message.chat.id,const.error)
        
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(1)