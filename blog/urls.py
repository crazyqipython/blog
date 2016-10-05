__author__ = 'huangqi'
from django.conf.urls import url,include
from . import views

urlpatterns = [

    url(r'^$',views.BlogIndex.as_view(),name='index'),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
]
