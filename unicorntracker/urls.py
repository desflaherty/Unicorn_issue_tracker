"""unicorntracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from features import urls as urls_features
from bugs import urls as urls_bugs
from features.views import all_features
from bugs.views import all_bugs
from cart import urls as urls_cart
from search import urls as urls_search
from search2 import urls as urls_search2
from graphs import urls as urls_graphs
from django.views import static
from .settings import MEDIA_ROOT 
from home.views import index
from checkout import urls as urls_checkout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^features/', include(urls_features)),
    url(r'^bugs/', include(urls_bugs)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^search2/', include(urls_search2)),
    url(r'^graphs/', include(urls_graphs)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
