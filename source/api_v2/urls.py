from django.urls import path

from api_v1.views import articles, get_token_view

app_name = 'v2'

urlpatterns = [
    path('articles/', articles, name='articles'),
    path('get-csrf/', get_token_view, name='get-csrf'),

]
