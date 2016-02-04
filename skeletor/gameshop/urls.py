from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^shop$', views.shop, name='shop'),
    url(r'^play/(?P<game_id>[0-9]+)/$', views.play, name='play'),
    url(r'^payment$', views.payment, name='payment'),
    url(r'^developer$', views.developer, name='developer'),
]

