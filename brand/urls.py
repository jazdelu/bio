from django.conf.urls import patterns, url

from brand import views

urlpatterns = patterns('',
    url(r'^(?P<title>.+)/$', views.get_brand_by_title, name='get_brand_by_title'),
)