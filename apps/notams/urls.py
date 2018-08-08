from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^apirequest$',views.api),
    url(r'^new$', views.create),
    url(r'^find$', views.find)
  ]
