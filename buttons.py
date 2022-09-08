import telebot

markuplanguage=telebot.types.ReplyKeyboardMarkup()
markuplanguage.row("English","Turkish")
markupmenu=telebot.types.ReplyKeyboardMarkup()
markupmenu.row("Inventory","Hunt","Profile","Rest")