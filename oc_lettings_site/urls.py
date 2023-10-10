from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def trigger_error(request):
    _ = 1 / 0
    return render(request, 'templates/error500.html')



urlpatterns = [
    path('', include('homeapp.urls')),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
