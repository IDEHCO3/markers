from django.conf.urls import patterns, url
from bookmarker import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^$', views.BookmarksList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.BookmarksDetail.as_view(), name='detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)