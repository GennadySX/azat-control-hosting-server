from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('project', ApiDomainView.as_view()),
    path('project/<int:id>/', ApiDomainView.as_view()),
    ]