from django.urls import path

from api_v1.views import echo

app_name = 'v1'

urlpatterns = [
    path('echo/', echo, name='echo'),
]
