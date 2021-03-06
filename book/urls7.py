from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from book import views6 as views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]