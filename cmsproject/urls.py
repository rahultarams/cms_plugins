from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog

admin.autodiscover()

urlpatterns = [
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    #path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
]


urlpatterns += i18n_patterns(
                             path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
                             path("admin/", admin.site.urls),
                             path(r'^i18n/', include('django.conf.urls.i18n')),
                             path("plugins/", include("plugins.urls")),
                             path("", include("cms.urls")),
                             path("djangocms-faq/", include("djangocms_faq.urls")),
                             )


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
