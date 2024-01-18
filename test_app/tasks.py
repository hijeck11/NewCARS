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
    url = 'https://www.binance.com/en/trade/BNB_USDT?type=spot'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Получаем title страницы
    title_element = soup.find('title')

    if title_element:
        current_price = title_element.text.strip()
        print(f'BNB/USDT текущая цена: {current_price}')
    else:
        print('Не удалось найти элемент title страницы.')

print_time_task.delay()

