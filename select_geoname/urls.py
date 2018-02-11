from django.conf.urls import url
from django.conf.urls import include, url
from . import views

urlpatterns = [
   url(r'^$', views.where_are_you, name='where_are_you'),
   # url(r'^$submit', views.submit, name='submit'),
]
