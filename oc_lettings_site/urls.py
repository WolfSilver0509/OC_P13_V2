from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


import sentry_sdk


def trigger_error(request):
    try:
        _ = 1 / 0
    except ZeroDivisionError as error:
        sentry_sdk.capture_exception(error)  # Capturez l'erreur complète
        return render(request, 'error500.html')


urlpatterns = [
    path('', include('homeapp.urls')),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
