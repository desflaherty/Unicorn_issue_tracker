from django.conf.urls import url,include
from .views import all_bugs,add_edit_bug

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^edit_bug/(?P<id>\d+)/$', add_edit_bug, name='edit_bug'),
    url(r'^add_bug/$', add_edit_bug, name='add_bug'),
]


