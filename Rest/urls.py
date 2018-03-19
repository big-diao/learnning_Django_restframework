from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^', include('book.urls5')),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]
