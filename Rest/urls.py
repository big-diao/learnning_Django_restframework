from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^', include('book.urls2')),
    path('admin/', admin.site.urls),
]
