from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from book import views, views1, views2, views4, views5


urlpatterns = format_suffix_patterns([
    url(r'^$', views5.api_root),
    url(r'^books/$',
        views5.BookList.as_view(),
        name='book-list'),
    url(r'^books/(?P<pk>[0-9]+)/$',
        views5.BookDetail.as_view(),
        name='book-detail'),
    url(r'^books/(?P<pk>[0-9]+)/what/$',
        views5.BookWhat.as_view(),
        name='book-what'),
    url(r'^users/$',
        views5.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views5.UserDetail.as_view(),
        name='user-detail')
])