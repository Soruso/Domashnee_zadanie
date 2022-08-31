import random
import telebot

bot = telebot.TeleBot('5474258601:AAEIfTEPWpiQjPZE70oCudgeDmiEvygS1HE')


@bot.message_handler(commands=['start'])
def privetstvie(message):
    bot.send_message(message.from_user.id, 'Угадайте число от 0 до 100')
    global chislo_bota
    chislo_bota = random.randint(0, 100)
    bot.register_next_step_handler(message, ugadaika)


def menshe(message):
    bot.send_message(message.from_user.id, 'Число меньше')
    bot.register_next_step_handler(message, ugadaika)


def bolshe(message):
    bot.send_message(message.from_user.id, 'Число больше')
    bot.register_next_step_handler(message, ugadaika)


def ugadaika(message):
    chislo_igroka = message.text
    chislo_igroka = int(chislo_igroka)
    if chislo_igroka > chislo_bota:
        menshe(message)
    elif chislo_igroka < chislo_bota:
        bolshe(message)
    else:
        bot.send_message(message.from_user.id, 'Победа')
        privetstvie(message)


if __name__ == '__main__':
    bot.infinity_polling()
