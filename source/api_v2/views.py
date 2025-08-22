import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseBadRequest
from django.views import View

from api_v2.serializers import ArticleSerializer
from webapp.models import Article

from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        serializer = ArticleSerializer(data=body)
        if serializer.is_valid():
            user = get_user_model().objects.last()
            article = serializer.save(author=user)
            return JsonResponse({"id": article.id}, status=201)
        else:
            return JsonResponse({"errors": serializer.errors}, status=400)
