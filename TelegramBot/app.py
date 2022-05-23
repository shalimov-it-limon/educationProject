import telebot
from extensions import CurrencyConverter, APIException
from config import keys, TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = f'Чтобы начать работу введите команду боту в следующем формате: ' \
           f'\n<имя валюты><в какую валюту перевести><количество переводимой валюты>' \
           f'\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(commands=['stop'])
def stop(message: telebot.types.Message):
    text = 'Завершаю работу'
    try:
        bot.stop_bot()
    except RuntimeError:
        bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Слишком много параметров')
        else:
            quote, base, amount = values
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message,f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        text = f'За {amount} {quote} можно получить {total_base} валюты {base}'
        bot.send_message(message.chat.id, text)




bot.polling()
