from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import autohaus_list, auto_detail, order_options, submit_order, celerytest, UpdateBnbUsdtView, UpdateBnbUsdtFormView

urlpatterns = [
    path('', autohaus_list, name='autohaus_list'),
    path('auto/<int:auto_id>/', auto_detail, name='auto_detail'),
    path('auto/<int:auto_id>/order/', order_options, name='order_options'),
    path('auto/<int:auto_id>/submit_order/', submit_order, name='submit_order'),
    path('a/', celerytest, name='celerytest'),
    path('update_bnb_usdt/', UpdateBnbUsdtView.as_view(), name='update_bnb_usdt'),
    path('update_bnb_usdt_form/', UpdateBnbUsdtFormView.as_view(), name='update_bnb_usdt_form'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)