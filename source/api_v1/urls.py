from django.urls import path

from api_v1.views import echo, articles, get_token_view

app_name = 'v1'

urlpatterns = [
    path('echo/', echo, name='echo'),
    path('articles/', articles, name='articles'),
    path('get-csrf/', get_token_view, name='get-csrf'),

]
