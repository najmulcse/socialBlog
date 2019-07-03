from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^$', views.ListGroups.as_view(), name='all')
]