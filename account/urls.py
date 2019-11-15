from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.conf.urls import url

from account import views

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    url('register/', views.register, name='register'),

    # login logout
    url('login/', login, name='login'),
    url('logout/', logout, name='logout'),
    url('logout-then-login/', logout_then_login, name='logout_then_login'),

]