from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^shop$', views.shop, name='shop'),
    url(r'^play$', views.play, name='play'),
    
]

