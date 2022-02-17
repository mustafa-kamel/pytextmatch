from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def search(request):
    pass


@require_http_methods(["POST"])
def results(request):
    pass
