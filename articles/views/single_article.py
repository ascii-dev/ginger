import arxiv
from django.http import Http404
from django.views import View
from django.shortcuts import render


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

        # The api returns a list of a single element
        return render(request, self.template_name, {'article': article[0]})
