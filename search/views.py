from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from ratelimit.decorators import ratelimit


def get_result(query):
    values = [{"value": "result 1", "percentage": "%91"},
              {"value": "result 2", "percentage": "%85"},
              {"value": "result 3", "percentage": "%66"},
              {"value": "result 4", "percentage": "%59"},
              {"value": "result 5", "percentage": "%51"},
              ]
    return {
        "key": query,
        "values": values,
        "length": len(values) + 1
    }


@ratelimit(key='ip', rate='5/m')
@require_http_methods(["GET"])
def search(request):
    return render(request, 'index.html')


@ratelimit(key='ip', rate='5/m')
@require_http_methods(["POST"])
def results(request):
    if not request.POST.get('query'):
        return render(request, 'index.html',
                      {'message': 'Please enter a valid search query.'})

    return render(request, 'results.html',
                  {"result": get_result(request.POST.get('query'))})
