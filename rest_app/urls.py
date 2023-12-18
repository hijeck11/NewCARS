from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from .views import *
from django.urls import path


urlpatterns = [
    path('cars/', MyModelListCreateView.as_view(), name='mymodel-list-create'),
    path('cars/create/', AutohausCreateView.as_view(), name='autohaus-create'),
    path('cars/destroy/<int:pk>/', WonderDestroy.as_view()),
    path('', AutohausListViews.as_view(), name='search'),
    path('cars/export/', ExportAPIViews.as_view(), name='export-api'),
    re_path('^cars/(?P<price>.+)/$', PurchaseList.as_view()),
    path('message/', send_message, name='send_message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
