from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from book import views, views1

urlpatterns = [
    url(r'^books/$',view=views1.book_list),
    url(r'^books/(?P<pk>[0-9]+)/$',view=views1.book_detail),
]
# 后缀
urlpatterns = format_suffix_patterns(urlpatterns)