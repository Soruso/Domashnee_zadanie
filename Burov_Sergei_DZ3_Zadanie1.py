def translater():
    digit = {"Zero": "ноль",
             "One": "один",
             "Two": "два",
             "Three": "три",
             "Four": "четыре",
             "Five": "пять",
             "Six": "шесть",
             "Seven": "семь",
             "Eight": "восемь",
             "Nine": "девять",
             "Ten": "десять"}
    if chislitelnoe not in digit:
        print("None")
    else:
        print(digit[chislitelnoe].capitalize())
chislitelnoe= input("Введите число для перевода:")
chislitelnoe = chislitelnoe.capitalize()
translater()
