from django.conf.urls import url,include
from .views import all_features,add_edit_feature

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^edit_feature/(?P<id>\d+)/$', add_edit_feature, name='edit_feature'),
    url(r'^add_feature/$', add_edit_feature, name='add_feature'),
]