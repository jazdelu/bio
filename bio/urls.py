from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^brand/', include('brand.urls')),
    url(r'^$','bio.views.coming', name='coming soon'),
    url(r'^page/', include('page.urls')),
    url(r'^send_mail/$','bio.views.sendmail',name='sendmail'),
    url(r'^cn/$','bio.views.coming_cn',name='coming_cn'),
    # url(r'^blog/', include('blog.urls')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)