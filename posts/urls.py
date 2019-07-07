from django.conf.urls import url
from . import views

app_name = 'posts'


urlpatterns =[
    url(r'^$', views.PostList.as_view(), name="all"),
    url(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PostDetail.as_view(), name="single")
]