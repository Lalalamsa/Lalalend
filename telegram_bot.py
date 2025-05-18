import telebot
import key_boards
import fsm

bot_token = '7890554839:AAEE2cQU30PclJXCcetfBzVBo9ZVIOgz0aA'
stater = fsm.FSM()
bot = telebot.TeleBot(bot_token)

def handle_default_state(message):
    if message.text == 'фото':
        stater.set_state(message.chat.id,fsm.image_state)
        bot.send_message(message.chat.id, text = 'Опиши фото', reply_markup = key_boards.keyboard2)
    elif message.text == 'текст':
        stater.set_state(message.chat.id,fsm.text_state)
        bot.send_message(message.chat.id, text = 'Опиши текст', reply_markup = key_boards.keyboard2)
    else:
        return_to_menu(message.chat.id)
def handle_image_state(message):
    if message.text == 'меню':
        return_to_menu(message.chat.id)
    else:
        bot.send_message(message.chat.id, text = 'Делаем')
def handle_text_state(message):
    if message.text == 'меню':
        return_to_menu(message.chat.id)
    else:
        bot.send_message(message.chat.id, text = 'Делаем')
def return_to_menu(chat_id):
    stater.set_state(chat_id,fsm.default_state)
    bot.send_message(chat_id, text = 'Главное меню:', reply_markup = key_boards.keyboard1)


@bot.message_handler(func=lambda message: True)
def on_message(message):
    state = stater.get_state(message.chat.id)

    if state == fsm.default_state:
        handle_default_state(message)
    elif state == fsm.image_state:
        handle_image_state(message)
    elif state == fsm.text_state:
        handle_text_state(message)
    else:
        return_to_menu(message.chat.id)
bot.polling()

