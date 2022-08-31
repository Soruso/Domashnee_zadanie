import requests
import json


def currency_rates():
    valuta = input('Введите валюту')
    valuta = valuta.upper()
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = requests.get(URL)

    dict_json = json.loads(response.text)
    kurs = dict_json['Valute'][valuta]['Value']
    print(f'1 {valuta} =  {kurs} RUB')
    return


currency_rates()
