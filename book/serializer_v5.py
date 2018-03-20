from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.CharField(source='owner.username')
    what = serializers.HyperlinkedIdentityField(view_name='book-what',format='html')

    class Meta:
        model = Book
        fields = ('name','created','owner','what')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True,view_name='book-detail',read_only=True)

    class Meta:
        model = User
        fields = ('id','username','books')

