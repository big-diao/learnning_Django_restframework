
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view, throttle_classes, schema, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from app1.permissions import BlacklistPermission, IsOwnerOrReadOnly


@api_view(['GET','POST'])
def hello_world1(request):
    if request.method == 'POST':
        return Response({'msg':'Come on some data!','data':request.data})
    return Response({"message": "Hello, world!"})

class OncePerdayUserThrottle(UserRateThrottle):
    rate = '1/day'

@api_view(['GET'])
@throttle_classes([OncePerdayUserThrottle]) # throttle 油门
def hello_world(req):
    return Response({'msg':'helllo for today! see u tomorrow!'})

@api_view(['GET'])
@schema(None)   # 模式
def view(request):
    return Response({"message": "Will not appear in schema!"})


@api_view()
@renderer_classes([JSONRenderer,])
def usercount(req):
    user_count = User.objects.filter().count()
    return Response({'count': user_count})

@api_view(['GET'])
@permission_classes([BlacklistPermission,])
def examp(request, format=None):
    # request.META['']
    # request.META
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# receiver 接收器
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
# @permission_classes([IsOwnerOrReadOnly,])
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

