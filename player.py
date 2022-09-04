inventory=[]
hp = 100
xp = 0
chatid = 0
level = 1
weapon = "none"
heal = 0
class player:
    global inventory
    global hp
    global xp
    global level
    global weapon
    global heal
    if xp == 100:
        level = level + 1
        xp = 0
    def healcondition(a):
        global heal
        heal = a
    def healing():
        global heal
        return heal
    def lvl():
        global level
        return level
    def health():
        global hp
        return hp
    def hpconfig(k):
        global hp
        hp = k
    def dechp(a):
        global hp
        hp = hp - a
    def inchp(a):
        global hp
        hp = hp + a
    def experience():
        global xp
        return xp
    def repxp(b):
        global xp
        xp = xp + b
    def id(c):
        global chatid
        chatid = c
        return chatid
    def additem(item):
        global inventory
        inventory.append(item)
    def inv():
        global inventory
        if len(inventory) == 0:
            return 32
        return inventory
    def power():
        return 10
    def weaponchange(weaponname):
        global weapon
        weapon = str(weaponname)
    def usedweapon():
        global weapon
        return weapon
