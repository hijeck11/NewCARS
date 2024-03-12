import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cars.settings')

app = Celery('cars', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'print_time_task': {
        'task': 'test_app.tasks.print_time_task',
        'schedule': 10.0
    },
}

app.conf.beat_schedule = {
    'update_bnb_usdt_task': {
        'task': 'test_app.tasks.update_bnb_usdt',
        'schedule': 5.0
    },
}


app.autodiscover_tasks()