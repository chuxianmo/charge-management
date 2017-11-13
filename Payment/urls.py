from django.conf.urls import url,include
from . import views


urlpatterns = [
     url(r'^payment/$', views.payment, name='payment'),
     url(r'^pay/$',views.pay,name='pay'),
     url(r'^form/$', views.form, name='form'),
     url(r'^confirmpay/$', views.form, name='confirmpay'),
     url(r'^test/$', views.test, name='test'),
]
