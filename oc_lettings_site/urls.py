from django.contrib import admin
from django.urls import path, include


import sentry_sdk


def trigger_error(request):
    try:
        _ = 1 / 0
    except ZeroDivisionError as e:
        # Capturer l'erreur et la signaler à Sentry
        sentry_sdk.capture_exception(e)


urlpatterns = [
    path('', include('homeapp.urls')),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
