from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.CharField(source='owner.username',read_only=True)
    name = serializers.HyperlinkedIdentityField(view_name='book-name',format='html')

    class Meta:
        model = Book
        fields = ('owner','name','created')

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True,queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ('id','username','books')

