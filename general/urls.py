from django.conf.urls import url
from . import views

app_name = 'general'
urlpatterns = [
    url(r'^$', views.TopView.as_view(), name="top"),
    url(r'^search$', views.SearchView.as_view(), name="search"),
    url(r'^question/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
]
