from django.conf.urls import patterns, url

from brand import views

urlpatterns = patterns('',
    url(r'^(?P<title>[^\d]+)/$', views.get_brand_by_title, name='get_brand_by_title'),
    url(r'^bio-in-wine/(?P<wid>\d+)/$', views.get_winery_by_id, name='get_winery_by_id'),
)