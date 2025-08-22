import json
from datetime import datetime
from decimal import Decimal
from json import JSONDecodeError

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseBadRequest

from webapp.models import Article

from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')



def articles(request):
    if request.method == 'GET':
        articles = Article.objects.all()

        response_articles = []

        for article in articles:
            response_articles.append({
                "title": article.title,
                "content": article.content,
                "author": article.author.username,
            })

        return JsonResponse(response_articles, safe=False)
    elif request.method == 'POST':
        try:
            print(request.user)
            body = json.loads(request.body)
            article = Article.objects.create(**body, author=request.user)
            return JsonResponse({"id": article.id}, status=201)
        except JSONDecodeError as e:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

