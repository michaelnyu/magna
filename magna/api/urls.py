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
        r'^api/v1/top/(?P<number>[0-9]+)$',
        views.get_top_donors,
        name='get_top_donors'
    ),
    url( 
        r'^api/v1/name/(?P<name>[a-zA-Z]+)$',
        views.get_users_by_name,
        name='get_users_by_name'
    ),
    url(
        r'^api/v1/latest/(?P<number>[0-9]+)$',
        views.get_latest_donors,
        name='get_latest_donors'
    ),
    url(
        r'^api/v1/donations/$',
        views.get_total_donations,
        name='get_total_donations'
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
