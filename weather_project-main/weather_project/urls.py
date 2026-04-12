from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('weather_app.urls')),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'weather_app/images/favicon.ico')),
]
