from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [

]

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        websocket_urlpatterns
    ),
})
