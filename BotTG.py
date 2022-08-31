import random
import telebot

bot = telebot.TeleBot('5474258601:AAEIfTEPWpiQjPZE70oCudgeDmiEvygS1HE')

ruka_igrok = 0
ruka_dealer = 0


def alling(ruka_dealer, ruka_igrok):
    while ruka_dealer < 17:
        ruka_dealer += random.randint(2, 11)

    while ruka_igrok < 17:
        ruka_igrok += random.randint(2, 11)

    if ruka_dealer == 21 and ruka_igrok == 21:
        # bot.send_message("Ничья")
        bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)
    elif ruka_igrok > 21 and ruka_dealer > 21:
        # bot.send_message("Проигрышь обоих")
        bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)
    elif ruka_dealer == 21 and ruka_igrok < 21:
        # bot.send_message("Победа дилера")
        bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)
    elif ruka_igrok == 21 and ruka_dealer < 21:
        # bot.send_message("Победа игрока")
        bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)
    elif ruka_dealer <= 21 and ruka_igrok > 21:
        # bot.send_message("Победа дилера")
        bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)
    elif ruka_igrok <= 21 and ruka_dealer > 21:
        # bot.send_message("Победа игрока")
        bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)
    else:
        if ruka_igrok < ruka_dealer < 21:
            # bot.send_message("Победа дилера")
            bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)
        elif ruka_dealer < ruka_igrok < 21:
            # bot.send_message("Победа игрока")
            bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)
        elif ruka_igrok == ruka_dealer:
            # bot.send_message("Ничья")
            bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)
        else:
            # bot.send_message("Произошел неведомый пиздец")
            bot.send_message("Карты дилера:", ruka_dealer, "Карты игрока:", ruka_igrok)


@bot.message_handler(commands=['start'])
def cycle(start):
    alling(ruka_dealer, ruka_igrok)


# cycle()

# print(x, y)
# cycle_2()
# def test(x, y):

if __name__ == '__main__':
    bot.infinity_polling()
