from datetime import datetime
from decimal import Decimal

from django.http import JsonResponse

from webapp.models import Article


def echo(request):
    article = Article.objects.first()
    test = {
        "my_list": [1,2,3],
        "price": Decimal('10.00'),
        "datetime": datetime.now(),
        "article": {
            "title": article.title,
            "content": article.content,
            "author": article.author.username,
        }
    }
    return JsonResponse(test)

