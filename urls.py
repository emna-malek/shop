from django.urls import re_path
from . import views

app_name = 'boutique'

urlpatterns = [

    re_path(r'^$', views.product_list, name='product_list'),
    re_path(r'^(?P<catégorie_libellé>[-\w]+)/$', views.product_list, name='product_list_category'),
    re_path(r'^(?P<id>\d+)/(?P<libellé>[-\w]+)/$', views.product_detail, name='product_detail'),

]
