import monsters as mt
import random

def fight(id,hp,dmg,xp,php,pwr):
    while True:
        if id == 3:
            return 255
        hp = hp - pwr
        if hp <= 0:
            feedback = [xp,php]
            return feedback
        php = php - dmg
        if php <= 0:
            return 0

def pickmonster(lvl):
    if lvl == 1:
        mtch = random.random()*100
        if mtch <= 1:
            monster = mt.healer
            return monster
        if mtch <= 34:
            monster = mt.haund
            return monster
        elif mtch <= 67:
            monster = mt.slime
            return monster
        elif mtch <= 100:
            monster = mt.worm
            return monster