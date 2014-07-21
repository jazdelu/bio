from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


from brand.models import Brand
from brand.sitemap import BrandSitemap

sitemaps = {
    'brand':BrandSitemap,
}



urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^brand/', include('brand.urls')),
    url(r'^contact/', 'bio.views.contact',name="Contact Us"),
    url(r'^$','bio.views.home', name='homepage'),
    url(r'^index/$','bio.views.home', name='homepage'),
    url(r'^page/', include('page.urls')),
    url(r'^partner/','partner.views.get_partners',name='get partners'),
    url(r'^send_mail/$','bio.views.sendmail',name='sendmail'),
    url(r'^cn/$','bio.views.coming_cn',name='coming_cn'),
    url(r'^setlang/$', 'bio.views.set_language',name="set language"),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # url(r'^blog/', include('blog.urls')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)