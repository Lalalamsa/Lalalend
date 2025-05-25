import telebot
import key_boards
import fsm
import ai

bot_token = '7890554839:AAEE2cQU30PclJXCcetfBzVBo9ZVIOgz0aA'
stater = fsm.FSM()
al_service = ai.AI()
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
        try:
            msg = bot.send_message(chat_id = message.chat.id, text = 'Генерируем' )
            image_url = al_service.generate_image(message.text)
            bot.delete_message(chat_id = message.chat.id, message_id = msg.id)
            bot.send_photo(chat_id = message.chat.id, caption = 'Ваше фото', photo = image_url )
        except Exception as e:
            bot.send_message(chat_id =message.chat.id, text = f'Произошла ошибка({str(e)})')
def handle_text_state(message):
    if message.text == 'меню':
        al_service.clear_dialog(message.chat.id)
        return_to_menu(message.chat.id)
    else:
        msg = bot.send_message(message.chat.id, 'Думаю над запросом')
        txt = al_service.generate_text(message.text, message.chat.id)
        msg = bot.edit_message_text(text = txt, chat_id = message.chat.id, message_id = msg.id)
        
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

