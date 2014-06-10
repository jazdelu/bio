from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^brand/', include('brand.urls')),
    url(r'^$','bio.views.home', name='home'),
    url(r'^(?P<url_parameter>.+)/$', 'page.views.get_page_by_url_parameter', name='get_page_by_url_parameter'),
    # url(r'^blog/', include('blog.urls')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)