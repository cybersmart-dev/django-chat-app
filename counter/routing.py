
from django.urls import path
from .consumers import CounterConsumer


ws_urlpatterns = [
    path("ws/counter/", CounterConsumer.as_asgi())
]