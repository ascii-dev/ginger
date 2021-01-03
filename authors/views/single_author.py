import arxiv
from django.http import Http404
from django.views.generic import ListView

from ginger.utils.set_pagination_context import set_pagination_context


class SingleAuthorView(ListView):
    template_name = 'authors/single.html'
    context_object_name = 'articles'

    def get_queryset(self):
        # start & max_results: used to assist with api pagination.
        start = int(self.request.GET.get('start', 0))
        max_results = int(self.request.GET.get('max_results', 10))

        author = self.kwargs.get('author')
        # TODO: error handling can be better
        if not author:
            raise Http404('Author not found!')

        # TODO: refactor to make sure only 6 months worth of articles are returned in total
        return arxiv.query(
            query=f"au:{author}",
            start=start,
            max_results=max_results,
            iterative=False,
            sort_order="descending",
            sort_by="submittedDate",
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SingleAuthorView, self).get_context_data(**kwargs)
        set_pagination_context(
            context,
            self.request.GET.get('start', 0),
            self.request.GET.get('max_results', 10),
        )
        context['author_name'] = self.kwargs.get('author')
        return context
