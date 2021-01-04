sample_arxiv_article = dict(
    split_id='2012.14415v1',
    id='http://arxiv.org/abs/2012.14415v1',
    title='Stochastic Approximation for Online Tensorial Independent Component\n  Analysis',
    primary_category={'term': 'stat.ML'},
    published='2015-04-20T17:58:58Z',
    author='Tony Stark',
    summary='Stochastic Approximation for Online Tensorial Independent Component\n  Analysis',
    authors=['Tony Stark', 'Oliver Queen'],
    arxiv_comment='early draft first preprint. 8 pages',
)


def mock_articles_with_query(query, start, max_results, iterative, sort_order, sort_by):
    """
    Returns a mock response for the arxiv pull articles API for testing purposes
    """
    return [sample_arxiv_article]


def mock_article_with_id_list(id_list, iterative, max_results):
    """
    Returns a mock response for a single arxiv article for testing purposes
    """
    return [sample_arxiv_article]


def mock_article_not_found(id_list, iterative, max_results):
    """
    Returns a mock response representing an article that doesn't exist
    """
    return []
