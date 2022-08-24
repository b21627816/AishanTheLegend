import random

class stick:
    def stick():
        damage = random.random()*100
        if damage <= 25:
            return "5"
        elif damage <= 50:
            return "4"
        elif damage <= 100:
            return "3"

class swordgen:
    def woodensword():
        damage = random.random()*100
        if damage <= 10:
            return "8"
        elif damage <= 25:
            return "7"
        elif damage <= 50:
            return "6"
        elif damage <= 100:
            return "5"

class staffgen:
    def woodenstaff():
        damage = random.random()*100
        if damage <= 10:
            return "8"
        elif damage <= 25:
            return "7"
        elif damage <= 50:
            return "6"
        elif damage <= 100:
            return "5"


class rangedgen:
    def sling():
        damage = random.random()*100
        if damage <= 10:
            return "8"
        elif damage <= 25:
            return "7"
        elif damage <= 50:
            return "6"
        elif damage <= 100:
            return "5"

class glovegen:
    def leatherglove():
        damage = random.random()*100
        if damage <= 10:
            return "8"
        elif damage <= 25:
            return "7"
        elif damage <= 50:
            return "6"
        elif damage <= 100:
            return "5"
