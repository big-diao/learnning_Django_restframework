from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    # created = serializers.DateTimeField()

    # serializer.save()时候调用 create() update()

    def create(self,data):
        return Book.objects.create(**data)

    def update(self,instance, data):
        instance.name = data.get('name',instance.name)
        instance.created = data.get('created',instance.created)
        instance.save()
        return instance