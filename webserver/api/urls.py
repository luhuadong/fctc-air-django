from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_host_stat/(?P<ip4addr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$', views.get_host_stat, name='getHostStat'),
    url(r'^get_latest_data/(?P<deviceName>[a-zA-Z0-9_]+$)', views.get_latest_data, name='getLatestData'),
    url(r'^test/(?P<id>[0-9]+$)', views.test, name='test'),
]