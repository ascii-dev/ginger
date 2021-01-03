def set_pagination_context(context, start, max_results):
    """
    Sets pagination on view contexts for use within the templates
    to paginate the api results
    :param context: the view context we need to attach the api to
    :param start: current page's start index
    :param max_results: maximum result per page
    :return:
    """
    # make sure previous is always a positive integer as we can't pull articles
    # from a negative start point
    previous = int(start) - 10

    context['next'] = int(start) + 10
    # converted previous to a string as a workaround for 0 being a False value
    context['previous'] = str(previous) if previous >= 0 else None
    context['max_results'] = int(max_results)
