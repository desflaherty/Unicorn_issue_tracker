from django.conf.urls import url, include
from .views import featuresgraphs

urlpatterns = [
    url(r'^featuresgraphs/$', featuresgraphs, name='featuresgraphs'),
]