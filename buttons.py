import telebot

markuplanguage=telebot.types.ReplyKeyboardMarkup()
markuplanguage.row("English","Turkish")
markupmenu=telebot.types.ReplyKeyboardMarkup()
markupmenu.add("Inventory","Hunt","Profile","Rest",row_width=2)