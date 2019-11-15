# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url('ws/chat/<str:room_name>/', consumers.ChatConsumer),

]