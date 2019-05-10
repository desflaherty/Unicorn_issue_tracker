from django.conf.urls import url,include
from .views import all_features,add_edit_feature,feature_detail,upvote_feature,add_comment_features

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^feature_detail/(?P<id>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^edit_feature/(?P<id>\d+)/$', add_edit_feature, name='edit_feature'),
    url(r'^add_feature/$', add_edit_feature, name='add_feature'),
    url(r'^upvote_feature/$', upvote_feature, name='upvote_feature'),
    url(r'^add_comment_features/(?P<id>\d+)/$',
        add_comment_features, name='add_comment_features'),
]