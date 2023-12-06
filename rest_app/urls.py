from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from .views import *
from django.urls import path


urlpatterns = [
    path('cars/', MyModelListCreateView.as_view(), name='mymodel-list-create'),
    path('cars/<int:pk>/', AutohausRESTDestroyView.as_view(), name='autohaus-destroy'),
    path('cars/create/', AutohausCreateView.as_view(), name='autohaus-create'),
    path('', AutohausListViews.as_view(), name='search'),
    re_path('^cars/(?P<price>.+)/$', PurchaseList.as_view()),
]

# path('cars/<int:pk>/', AutohausRESTDestroyView.as_view(), name='autohaus-destroy'),