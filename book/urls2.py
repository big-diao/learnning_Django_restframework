from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from book import views, views1, views2, views4

urlpatterns = [
    url(r'^books/$',view=views4.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$',view=views4.BookDetail.as_view()),
]
# 后缀
urlpatterns = format_suffix_patterns(urlpatterns)