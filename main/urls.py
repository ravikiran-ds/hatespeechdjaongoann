from django.conf.urls import url
from .views import index


app_name='main'

urlpatterns=[url(r'^$',index)]
