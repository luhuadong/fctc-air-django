from django.conf.urls import url

from . import views

urlpatterns = [
    #path('monitor/', include('monitor.urls')),
    #url(r'^admin/', admin.site.urls),
    #url(r'^', include('monitor.urls')),
    #url(r'^api/', include('api.urls')),


    url(r'^login$',   views.login,   name="login"),
    url(r'^dologin$', views.dologin, name="dologin"),
    url(r'^logout$',  views.logout,  name="logout"),

    url(r'^', views.index, name='index'),
    url(r'(?P<pIndex>[0-99]+)$', views.index, name='index'),

    url(r'^add$', views.add, name='monitor_add'),
    url(r'^insert$', views.insert, name='monitor_insert'),
    url(r'^delete/(?P<hid>\d+)$', views.delete, name='monitor_delete'),
    url(r'^edit/(?P<hid>\d+)$', views.edit, name='monitor_edit'),
    url(r'^update/(?P<hid>\d+)$', views.update, name='monitor_update'),

    #url(r'^monitor/(?P<pIndex>[0-99]+)$', views.index, name='index'),
    #url(r'^monitor/(?P<pIndex>[0-99]+)$', views.index, name='index'),

    url(r'^details/(?P<hid>\d+)$', views.details, name='details'),
    url(r'^manual', views.manual, name='manual'),
    url(r'^settings', views.settings, name='settings'),
]
