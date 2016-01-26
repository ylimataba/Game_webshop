from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^shop$', views.shop, name='shop'),
    url(r'^play/(?P<game_id>[0-9]+)/$', views.play, name='play'),
    url(r'^shop/success$', views.shop_success, name='shop_success'),
    url(r'^shop/cancel$', views.shop_cancel, name='shop_cancel'),
    url(r'^shop/error$', views.shop_error, name='shop_error'),
    
]

