from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


app_name= 'myapp'
urlpatterns = [
    url(r'^$', login, {'template_name': 'myapp/login.html'}),
    url(r'^added/(?P<pk>\d+)/$', views.added, name='added'),
    url(r'^subtracted/(?P<pk>\d+)/$', views.subtracted, name='subtracted'),
]
