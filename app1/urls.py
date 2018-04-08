from django.conf.urls import url

from app1 import views
from rest_framework.authtoken import views as tokenview

urlpatterns = [
    url(r'helloworld/$',view=views.hello_world),
    url(r'helloworld1/$',view=views.hello_world1),
    url(r'view/$',view=views.view),
    url(r'usercount/$',view=views.usercount),
    url(r'examp/$',view=views.examp),
    url(r'api-token-auth/',view=tokenview.obtain_auth_token)
]
