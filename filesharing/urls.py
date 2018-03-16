from django.conf.urls import url
from filesharing import views

urlpatterns = [
    url(r'^', views.remoteConnection),
]
