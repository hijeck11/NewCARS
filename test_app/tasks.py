from cars.celery import app
import datetime
import requests
from bs4 import BeautifulSoup

@app.task
def add(x, y):
    print(x * y)
    return x * y

def print_time():
    now = datetime.datetime.now()
    print(now)
    print("Current time is:",now)

@app.task
def print_time_task():
    print_time()


@app.task
def update_bnb_usdt():
    # URL для получения текущей цены BNB/USDT
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT'

    # Отправляем GET-запрос к Binance API
    response = requests.get(url)

    # Если запрос успешен, выводим текущую цену
    if response.status_code == 200:
        data = response.json()
        current_price = data['price']
        print(f'Текущая цена BNB/USDT: {current_price}')
    else:
        print('Ошибка при получении данных о цене')

# Вызываем функцию для получения текущей цены BNB/USDT


update_bnb_usdt()

