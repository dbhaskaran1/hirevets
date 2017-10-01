from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.job_list, name='job_list'),
    url(r'^job/(?P<pk>\d+)/$', views.job_detail, name='job_detail'),
]
