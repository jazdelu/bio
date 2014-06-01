from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bio.views.home', name='home'),
    url(r'^brand/$', 'bio.views.brand', name='brand'),
    url(r'^consumption/$', 'bio.views.consumption', name='consumption'),
    url(r'^about/$', 'bio.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
