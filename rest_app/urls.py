from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import MyModelListCreateView
from django.urls import path
from . import views

urlpatterns = [
    path('cars/', MyModelListCreateView.as_view(), name='mymodel-list-create'),
]