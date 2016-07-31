# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = i18n_patterns('',
    (r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
    url(r'^admin-lecheng-location/', include(admin.site.urls)),  # NOQA
    url(r'^_nested_admin/', include('nested_admin.urls')),
    #    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^rent_lookup/', include('rent_lookup.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
#if settings.DEBUG:
#    urlpatterns = patterns('',
#        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
#            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#       ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
