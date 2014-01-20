from django.conf.urls import patterns, url
from vm import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
        url(r'^home_precinct_list/', views.home_precinct_list),
        url(r'^precinct_detail/(?P<precinct_name>\w+)/$', views.precinct_detail, name= 'precinct_detail'),
        )
