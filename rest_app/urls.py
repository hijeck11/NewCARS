from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.urls import path


urlpatterns = [
    path('cars/', MyModelListCreateView.as_view(), name='mymodel-list-create'),
    path('cars/<int:pk>/', MyModelListCreateView.as_view(), name='mymodel-list-delete'),
    path('cars/create/', AutohausCreateView.as_view(), name='autohaus-create'),
]