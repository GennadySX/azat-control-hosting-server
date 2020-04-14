from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('get', ApiProjectView.as_view()),
    path('projects', ApiProjectView.as_view()),
    path('projects/create', ApiProjectView.create),
    path('projects/status', ApiProjectView.as_view()),
    path('domain', ApiDomainView.as_view()),
    path('domain/create', ApiDomainView.as_view()),
    path('domain/status', ApiDomainView.as_view()),
]