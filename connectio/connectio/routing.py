from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf.urls import url

from chat.consumers import Consumer

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r'^chat/(?P<chat>[\w\s]+)$', Consumer.as_asgi())
                ]
            )
        )
    )
})
