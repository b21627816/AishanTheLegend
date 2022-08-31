def fight(hp,dmg,xp,php,pwr):
    while True:
        hp = hp - pwr
        if hp <= 0:
            feedback = [xp,php]
            return feedback
        php = php - dmg
        if php <= 0:
            return 0