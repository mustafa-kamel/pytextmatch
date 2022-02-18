from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='5/m')
@require_http_methods(["GET"])
def search(request):
    return render(request, 'index.html')


@ratelimit(key='ip', rate='5/m')
@require_http_methods(["POST"])
def results(request):
    pass
