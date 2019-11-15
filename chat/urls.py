from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='chat'),
    url('<str:room_name>/', views.room, name='room'),
]