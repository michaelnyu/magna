from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/entries/(?P<pk>[0-9]+)$',
        views.get_delete_put_user_entry,
        name='get_delete_put_user_entry'
    ),
    url(
        r'^api/v1/entries/$',
        views.get_post_user_entry,
        name='get_post_user_entry'
    ),
    url(
        r'^api/v1/recent/(?P<number>[0-9]+)$',
        views.get_recent_entries,
        name='get_recent_entries'
    ),
    url(
        r'^api/v1/incrementvotes/(?P<pk>[0-9]+)$',
        views.put_vote,
        name='put_vote'
    ),
]