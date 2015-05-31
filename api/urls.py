from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'v0/ideas/', include('api.v0.urls', namespace='v0')),
    url(r'v1/ideas/', include('api.v1.urls', namespace='v1')),
]
