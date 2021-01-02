import arxiv
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from favorites.models import Favorite


class CreateFavoriteView(LoginRequiredMixin, View):
    def post(self, request, article_id):
        article = arxiv.query(
            id_list=[article_id],
            iterative=False,
            max_results=1,
        )

        # Very simple error handling
        if not article:
            raise Http404({'error': 'Article not found'})

        Favorite.objects.get_or_create(article_id=article_id, user=request.user)

        return redirect(reverse('single-article', args=[article_id]))
