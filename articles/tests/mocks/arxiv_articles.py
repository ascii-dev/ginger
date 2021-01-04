sample_arxiv_article = dict(
    id='http://arxiv.org/abs/2012.14415v1',
    title='Stochastic Approximation for Online Tensorial Independent Component\n  Analysis',
    primary_category={'term': 'stat.ML'},
    published='2015-04-20T17:58:58Z',
    author='Some Author',
    summary='Stochastic Approximation for Online Tensorial Independent Component\n  Analysis'
)


def mock_arxiv_articles(query, start, max_results, iterative, sort_order, sort_by):
    """
    Returns a mock response for the arxiv pull articles API for testing purposes
    """
    return [sample_arxiv_article]
