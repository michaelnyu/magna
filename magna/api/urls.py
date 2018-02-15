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
        r'^api/v1/top/donors/$',
        views.get_top_five_donors,
        name='get_top_five_donors'
    )
  #  url(
  #      r'^api/v1/donations/$',
  #      views.get_total_donations,
  #      name='get_total_donations'
  #  )

]
