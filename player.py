inventory=[]
hp = 100
xp = 0
chatid = 0
class player:
    global inventory
    global hp
    global xp
    def health():
        global hp
        return hp
    def zerohp():
        global hp
        hp = 0
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

