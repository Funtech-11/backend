
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from events.views import EventViewSet, LocationViewSet, SpeakerViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'v1/events', EventViewSet)
router.register(r'v1/speakers', SpeakerViewSet)
router.register(r'v1/locations', LocationViewSet)

urlpatterns = [
    path('there-is-no-admin/', admin.site.urls),

    # API
    path('api/', include(router.urls)),
    path('api/v1/user/', include('users.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Optional UI:
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# {
#     "username": "name",
#     "email": "admin@admin.ru",
#     "id": 1
# }
