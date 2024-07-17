from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from registration import urls
from core import urls
from sample import urls
from social import urls
from about import urls
from services import urls
from store import urls
from contact import urls
from blog import urls

urlpatterns = [
    # URLS DJANGO
    path('admin/', admin.site.urls),
    path("accounts/", include("registration.urls")),
    # CORE - WEBEMPRESARIAL
    path("", include("core.urls")),
    # SAMPLE - WEBEMPRESARIAL
    path("sample/", include("sample.urls")),
    # SOCIAL - WEBEMPRESARIAL
    path("social/", include("social.urls")),
    # ABOUT - WEBEMPRESARIAL
    path("about/", include("about.urls")),
    # SERVICES - WEBEMPRESARIAL
    path("services/", include("services.urls")),
    # STORE - WEBEMPRESARIAL
    path("store/", include("store.urls")),
    # CONTACT - WEBEMPRESARIAL
    path("contact/", include("contact.urls")),
    # BLOG - WEBEMPRESARIAL
    path("blog/", include("blog.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
