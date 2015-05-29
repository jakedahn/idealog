from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^v0/', include('api.v0.urls')),
]
