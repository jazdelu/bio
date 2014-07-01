from django.conf.urls import patterns, url

from brand import views

urlpatterns = patterns('',
    url(r'^(?P<title>[^\d]+)/$', views.get_brand_by_title, name='get_brand_by_title'),
    url(r'^bio-in-vine/(?P<rid>\d+)/$', views.get_wineries_by_region, name='get_wineries_by_region'),
)