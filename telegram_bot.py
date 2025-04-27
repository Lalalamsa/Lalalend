import telebot
import key_boards

bot_token = '7890554839:AAEE2cQU30PclJXCcetfBzVBo9ZVIOgz0aA'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def on_message(message):
    mgs_text = message.text
    if mgs_text == 'фото':
        bot.send_message(message.chat.id, text = 'сама фото делай', reply_markup = key_boards.keyboard2)
    elif mgs_text == 'текст':
        bot.send_message(message.chat.id, text = 'сама текст пиши', reply_markup = key_boards.keyboard2)
    else:
        bot.send_message(message.chat.id, text = 'меню сделали', reply_markup = key_boards.keyboard1)
bot.polling()

