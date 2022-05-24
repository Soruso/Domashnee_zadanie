duration = int(input("Введите количество секунд"))
#Секунды
if duration >= 0 and duration <= 60:
    print(duration, "сек")
#Минуты
elif duration >= 60 and duration <= 3600:
    minutes = duration / 60
    seconds = duration % 60
    print(int(minutes), "мин", int(seconds), "сек")
#Часы
elif duration >= 3600 and duration <= 86400:
    hour = duration / 3600
    minutes = duration % 3600
    minutes = minutes / 60
    seconds = duration % 60
    print(int(hour), "час", int(minutes), "мин", int(seconds), "сек")
#Дни
elif duration > 86400:
    day = duration / 86400
    hour = duration / 3600
    hour = hour % 60
    minutes = duration % 3600
    minutes = minutes / 60
    seconds = duration % 60
    print(int(day), "дн", int(hour), "час", int(minutes), "мин", int(seconds), "сек")
#Исключение
else:
    print("Введено неверное значение")