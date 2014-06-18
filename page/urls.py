from django.conf.urls import patterns, url

from page import views

urlpatterns = patterns('',
    url(r'^(?P<url_parameter>.+)/$', views.get_page_by_url_parameter, name='get_page_by_url_parameter'),
)