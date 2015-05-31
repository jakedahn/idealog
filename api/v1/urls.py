from django.conf.urls import include, url
from django.contrib import admin

import views

urlpatterns = [
    url('^$', views.IdeaList.as_view()),
]
