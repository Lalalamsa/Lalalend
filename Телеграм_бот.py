import telebot

bot_token = '7890554839:AAEE2cQU30PclJXCcetfBzVBo9ZVIOgz0aA'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)
bot.polling()
