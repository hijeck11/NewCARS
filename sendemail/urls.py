from django.contrib import admin
from django.urls import path

from .views import SendMessageView

urlpatterns = [
    # path('contact/', contact_view, name='contact'),
    # path('success/', success_view, name='success'),
    path('send-message/', SendMessageView.as_view(), name='send-message'),
]