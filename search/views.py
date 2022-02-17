from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def search(request):
    return render(request, 'index.html')


@require_http_methods(["POST"])
def results(request):
    pass
