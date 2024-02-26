from django.urls import path

from .consumers import FileExtensionConsumer

websocket_urlpatterns = [
    path("ws/file_extension/", FileExtensionConsumer.as_asgi()),
]
