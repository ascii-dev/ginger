import arxiv
from django.http import Http404
from django.views import View
from django.shortcuts import render

from favorites.models import Favorite


class ArticleView(View):
    template_name = 'articles/single.html'

    def get(self, request, article_id):
        article = arxiv.query(
            id_list=[article_id],
            iterative=False,
            max_results=1,
        )
        # Simple error handling
        if not article:
            raise Http404("Article not found!")

        context = dict(article=article[0])

        if request.user.is_authenticated:
            # TODO: there possibly is a better way to do this
            try:
                context['favorite'] = Favorite.objects.get(article_id=article_id, user=request.user)
            except Favorite.DoesNotExist:
                context['favorite'] = None

        # The api returns a list of a single element
        return render(request, self.template_name, context)
