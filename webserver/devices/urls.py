from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'devices'

urlpatterns = [
    url(r'^$', views.index, name='index')
    #path('', views.index, name='index')
]
