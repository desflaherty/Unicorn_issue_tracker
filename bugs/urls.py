from django.conf.urls import url,include
from .views import all_bugs,add_edit_bug,bug_detail,upvote_bug,add_comment_bugs

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^edit_bug/(?P<id>\d+)/$', add_edit_bug, name='edit_bug'),
    url(r'^add_bug/$', add_edit_bug, name='add_bug'),
    url(r'^upvote_bug/$', upvote_bug, name='upvote_bug'),
    url(r'^add_comment_bugs/(?P<id>\d+)/$',
        add_comment_bugs, name='add_comment_bugs'),
]


