from django.conf.urls import include, url
from django.contrib import admin

from api.v0 import views

urlpatterns = [
    url(r'^ideas', views.IdeaList.as_view()),
]
