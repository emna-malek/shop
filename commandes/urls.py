from django.urls import re_path
from . import views

app_name = 'commandes'

urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),

]
