from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from django.views.static import serve


favicon_view = RedirectView.as_view(url='/static/favicon/favicon.ico', permanent=True)

urlpatterns = [
    path('', include( 'client.base.urls' )),
    path('adminsite/', admin.site.urls),
    path('auth/', include( 'server.auth.urls' )),
    path('dashboard/', include( 'client.panel.urls' )),
    re_path(r'^favicon\.ico$', favicon_view),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),        
    ]