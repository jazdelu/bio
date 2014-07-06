from django.conf.urls import patterns, url

from page import views

urlpatterns = patterns('',
    url(r'^(?P<title>.+)/$', views.get_page_by_title, name='get_page_by_title'),
)