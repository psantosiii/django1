from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^quotes$', views.quotes),
    url(r'^create$', views.create),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^users/(?P<id>\d+)$', views.users),
    # url(r'^show_trip/(?P<trip_id>\d+)$', views.show_trip),
    # url(r'^join/(?P<trip_id>\d+)$', views.join),
    # url(r'^create_trip$', views.create_trip),
    # url(r'^home$', views.index)

]