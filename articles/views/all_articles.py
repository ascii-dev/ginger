import arxiv
from django.views.generic import ListView


class AllArticlesView(ListView):
    template_name = 'articles/all.html'
    context_object_name = 'articles'

    def get_queryset(self):
        # start & max_results: used to assist with api pagination.
        start = int(self.request.GET.get('start', 0))
        max_results = int(self.request.GET.get('max_results', 10))

        return arxiv.query(
            query="all:data science OR all:psychiatry OR all:therapy OR all:machine learning",
            start=start,
            max_results=max_results,
            iterative=False,
            sort_order="descending",
            sort_by="submittedDate",
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AllArticlesView, self).get_context_data(**kwargs)
        # make sure previous is always a positive integer as we can't pull articles
        # from a negative start point
        previous = int(self.request.GET.get('start', 0)) - 10

        context['next'] = int(self.request.GET.get('start', 0)) + 10
        # converted previous to a string as a workaround for 0 being a False value
        context['previous'] = str(previous) if previous >= 0 else None
        context['max_results'] = int(self.request.GET.get('max_results', 10))
        return context
