from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Book
from .serializer_v2 import BookSerializer

@csrf_exempt
def book_list(req):
    if req.method == 'GET':
        objs = Book.objects.all()
        serializer = BookSerializer(objs,many=True)
        return JsonResponse(serializer.data,safe=False)
    if req.method == 'POST':
        print(type(req))
        data = JSONParser.parse(req)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def book_detail(req,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if req.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)

    if req.method == 'PUT':
        data = JSONParser().parse(req)
        serializer = BookSerializer(book,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    if req.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)

