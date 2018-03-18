from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializer_v2 import BookSerializer


class BookList(APIView):

    def get(self,req,format=None):
        print('+++++++++++++++++++ views2')
        book = Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)

    def post(self,req,format=None):
        serializer = BookSerializer(req.data, )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_obj(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self,req,pk,format=None):
        book = self.get_obj(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self,req,pk,format=None):
        book = self.get_obj(pk)
        serializer = BookSerializer(book,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delet(self,req,pk,format=None):
        book = self.get_obj(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
