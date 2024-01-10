from cars.celery import app
import datetime

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


print_time_task.delay()