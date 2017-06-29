from django.conf.urls import url
from . import views
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
	url(r'^$', views.CartDetail, name='CartDetail'),
	url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
	url(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
	url(r'^cart/', views.CartDetail, name='CartDetail')
]
