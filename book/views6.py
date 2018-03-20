from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from book.models import Book
from book.permissions import IsOwnerOrReadOnly
from book.serializer_v5 import UserSerializer, BookSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = (permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def what(self,req,*args,**kwargs):
        book = self.get_object()
        return Response(book.what)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

