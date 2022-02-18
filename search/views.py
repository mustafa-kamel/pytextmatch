import os
import pandas
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from ratelimit.decorators import ratelimit
from .search import Search


@ratelimit(key='ip', rate='5/m')
@require_http_methods(["GET"])
def search(request):
    with open(
            os.path.join(os.path.dirname(__file__), 'data.csv'), "r") as f:
        options = pandas.read_csv(f, usecols=['Key'])
    return render(request, 'index.html', {'options': options.Key.to_list()})


@ratelimit(key='ip', rate='5/m')
@require_http_methods(["POST"])
def results(request):
    if not request.POST.get('query'):
        return render(request, 'index.html',
                      {'message': 'Please enter a valid search query.'})

    return render(request, 'results.html',
                  {"result": Search(request.POST.get('query')).get_result()})
