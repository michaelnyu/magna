from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/entries/(?P<pk>[0-9]+)$',
        views.get_delete_update_user_entry,
        name='get_delete_update_user_entry'
    ),
    url(
        r'^api/v1/entries/$',
        views.get_post_puppies,
        name='get_post_puppies'
    )
]