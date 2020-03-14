# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""General utilities used across apps"""

from django.http import JsonResponse


def paginate_to_json(request, data):
    """Paginate a list of dicts and return as a ``JsonResponse``

    For expected in/outputs of paginated data, see
    https://datatables.net/manual/server-side .

    Args:
        request (HttpRequest): Incoming HTTP request
        data           (list): The data to paginate
    """

    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    draw = request.GET.get('draw', -1)

    paginated_alerts = data[start:start + length]

    response = {
        'draw': draw,
        'data': paginated_alerts,
        'recordsTotal': len(data),
        'recordsFiltered': len(paginated_alerts),
    }

    return JsonResponse(response)
