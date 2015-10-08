from django.conf.urls import patterns, url
from administrator import views


urlpatterns = patterns('',

    url(r'^institute/$', views.institute_list, name='institute_list'),
    url(r'^institute/new$', views.institute_create, name='institute_new'),
    url(r'^institute/edit/(?P<pk>[0-9]+)$', views.institute_update, name='institute_edit'),
    url(r'^institute/delete/(?P<pk>[0-9]+)$', views.institute_delete, name='institute_delete'),
    )