from django.conf.urls import patterns, url

from frontend import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='frontend'),
    url(r'^algorithms/(?P<model_name>\D+)/$', views.model_info, name='model_info'),
)
