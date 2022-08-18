import telebot

bot = telebot.TeleBot("5394587224:AAEuqvPVk6WuVh5wfIHpdLrDUE0OEDdDl6M")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass
# обработчик, чтобы он из сообщения
# брал username и выдавал приветственное сообщение с привязкой к пользователю.
#
import telebot

bot = telebot.TeleBot("5394587224:AAEuqvPVk6WuVh5wfIHpdLrDUE0OEDdDl6M")

# while True:
#     try:
#         @bot.message_handler(commands=['start', 'help'])
#         def repeat(message: telebot.types.Message):
#             print(message.text)  # Позволит распарсить сообщения гостей.
#             bot.reply_to(message, f'Здратути, {message.chat.username}')
#         pass
#
#
#         def get_username(message):
#             usr = bot.get_chat_member(message.chat.id, message.from_user.id)
#             if not usr.user.username:
#                 return usr.user.first_name
#             else:
#                 return usr.user.username
#
#
#         bot.polling(none_stop=True)

# print(a.text)
# обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD».
# Бот должен отвечать не отдельным сообщением, а с привязкой к картинке.

import telebot

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"У тебя очень красивый голос!")

bot.polling(none_stop=True)


def get_username(message):
    usr = bot.get_chat_member(message.chat.id, message.from_user.id)
    if not usr.user.username:
        return usr.user.first_name
    else:
        return usr.user.username


def handle_sticker(message):
    if get_username(message) == bot.get_chat_member(message.chat.id, message.from_user.id).user.username:
        bot.send_message(message.chat.id, f'Привет, {message.chat.username}')
    else:
        bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}')


@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    print(message.text)  # Позволит распарсить сообщения гостей.
    bot.reply_to(message, f'Здратути, {message.chat.first_name}')
pass






bot.polling(none_stop=True)