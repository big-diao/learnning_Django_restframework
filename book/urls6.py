from django.conf.urls import url
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from book.views5 import api_root
from book.views6 import BookViewSet, UserViewSet

book_list = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = BookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
book_what = BookViewSet.as_view({
    'get': 'what'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^books/$', book_list, name='book-list'),
    url(r'^books/(?P<pk>[0-9]+)/$', book_detail, name='book-detail'),
    url(r'^books/(?P<pk>[0-9]+)/what/$', book_what, name='book-what'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])