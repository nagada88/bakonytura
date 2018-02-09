from django.conf.urls import  include, url
import myapp.views as views

urlpatterns = [
    url(r'^trips/', views.trips, name = 'trips'),
    url(r'^news/', views.news, name = 'news'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]