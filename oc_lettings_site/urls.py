from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    _ = 1 / 0


urlpatterns = [
    path('', include('homeapp.urls')),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
