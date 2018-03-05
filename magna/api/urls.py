from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/entries/(?P<pk>[0-9]+)$',
        views.get_delete_put_user_entry,
        name='get_delete_put_user_entry'
    ),
    url(
        r'^api/entries/$',
        views.get_post_user_entry,
        name='get_post_user_entry'
    ),
    url(
        r'^api/top/(?P<number>[0-9]+)$',
        views.get_top_donors,
        name='get_top_donors'
    ),
    url( 
        r'^api/name/(?P<name>[a-zA-Z]+)$',
        views.get_users_by_name,
        name='get_users_by_name'
    ),
    url(
        r'^api/latest/(?P<number>[0-9]+)$',
        views.get_latest_donors,
        name='get_latest_donors'
    ),
    url(
        r'^api/donations/$',
        views.get_total_donations,
        name='get_total_donations'
    ),
    url(
        r'^api/recent/(?P<number>[0-9]+)$',
        views.get_recent_entries,
        name='get_recent_entries'
    ),
    url(
        r'^api/incrementvotes/(?P<pk>[0-9]+)$',
        views.put_vote,
        name='put_vote'
    ),
]
