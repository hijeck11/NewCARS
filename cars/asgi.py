"""
ASGI config for cars project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import application as chat_application
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import application as chat_application
from daphne.server import ProtocolTypeRouter as DaphneProtocolTypeRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cars.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        chat_application
    ),
})

application = DaphneProtocolTypeRouter({
    "http": application,
})
