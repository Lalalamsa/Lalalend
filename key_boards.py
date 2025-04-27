import telebot
button1 = telebot.types.KeyboardButton(text= 'фото')
button2 = telebot.types.KeyboardButton(text= 'текст')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.add(button1, button2)

button3 = telebot.types.KeyboardButton(text= 'меню')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.add(button3)
