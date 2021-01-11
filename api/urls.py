from django.conf.urls import url
from .views import Index


app_name='api'

urlpatterns=[url(r'^$',Index.as_view()),
            ]
