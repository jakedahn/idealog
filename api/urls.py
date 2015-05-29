from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^v0/', include('api.v0.urls')),
    url(r'^v1/', include('api.v1.urls')),
]
