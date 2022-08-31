# import random
import telebot

bot = telebot.TeleBot('5474258601:AAEIfTEPWpiQjPZE70oCudgeDmiEvygS1HE')


# def start(message):
# bot.send_message(message.chat.id, 'It works!')
# bot.register_next_step_handler(message, get_size_nose)
@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.from_user.id, 'Введите длинну носа')
    bot.register_next_step_handler(message, get_size_nose)
    pass


def get_size_nose(message):
    bot.send_message(message.from_user.id, 'Введите массу тела')
    global size_nose
    size_nose = message.text
    bot.register_next_step_handler(message, get_mass)


def get_mass(message):
    global mass
    mass = message.text
    bot.send_message(message.from_user.id, 'Введите размер ноги')
    bot.register_next_step_handler(message, get_size_foot)


def get_size_foot(message):
    global size_foot
    global itog
    size_foot = message.text
    itog = 35 * (int(size_foot) + 3 * int(size_nose)) / int(mass)
    itog = int(itog)
    itog = str(itog)
    vivod = 'Идеальная длина члена: ' + itog + ' СМ'
    bot.send_message(message.from_user.id, vivod)



#def get_all(message):
    #global itog
    #itog = 35 * (int(size_foot) + 3 * int(size_nose)) / int(mass)
    #bot.send_message(message.chat.id, itog)


if __name__ == '__main__':
    bot.infinity_polling()
