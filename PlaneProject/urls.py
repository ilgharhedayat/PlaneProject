from azbankgateways.urls import az_bank_gateways_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("airlines/", include("airlines.urls", namespace="airlines")),
    path("", include("passangers.urls", namespace="passengers")),
    path("bankgateways/", az_bank_gateways_urls()),
    path('hotels/', include('hotels.urls', namespace='hotel')),
    path('core/', include('core.urls', namespace='core')),
]

if settings.DEBUG:
    # ADD ROOT MEDIA FILES
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
