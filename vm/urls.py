from django.conf.urls import patterns, url
from vm import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
        )
