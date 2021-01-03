import arxiv
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from ginger.utils.set_pagination_context import set_pagination_context

from favorites.models import Favorite


class AllFavoritesView(LoginRequiredMixin, ListView):
    template_name = 'favorites/all.html'
    context_object_name = 'articles'

    def get_queryset(self):
        # start & max_results: used to assist with api pagination.
        start = int(self.request.GET.get('start', 0))
        max_results = int(self.request.GET.get('max_results', 10))

        favorites = Favorite.objects.filter(
            user_id=self.request.user.id)\
            .order_by('-created_at')

        article_ids = [favorite.article_id for favorite in favorites]

        return arxiv.query(
            id_list=article_ids,
            start=start,
            max_results=max_results,
            iterative=False,
            sort_order="descending",
            sort_by="submittedDate",
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AllFavoritesView, self).get_context_data(**kwargs)
        set_pagination_context(
            context,
            self.request.GET.get('start', 0),
            self.request.GET.get('max_results', 10),
        )
        return context
