from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status, mixins, generics, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import permissions

from book.permissions import IsOwnerOrReadOnly
from book.serializer_v5 import UserSerializer
from .models import Book
from .serializer_v5 import BookSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


@api_view(['GET',])
def api_root(req,format=None):
    return Response({
        'users':reverse('user-list',request=req,format=None),
        'books': reverse('book-list',request=req,format=format)
    })

class BookName(generics.GenericAPIView):
    queryset = Book.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer)

    def get(self,req,*args,**kwargs):
        book = self.get_object()
        return Response(book.name)