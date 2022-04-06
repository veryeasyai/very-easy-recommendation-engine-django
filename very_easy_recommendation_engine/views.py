"""
Views for Very Easy AI's Python/Django module.
"""
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from very_easy_recommendation_engine.engine import VeryEasyRecommendationEngine


# TODO: Limit this to only certain IP addresses and use an auth token.
@require_GET
def data_available_endpoint(request):
    """
    Endpoint to provide data to VeryEasyAI.

    Currently uses a paginated response of a queryset.

    In the future we could consider a streaming download, something like:
    https://stackoverflow.com/a/8601118/2532070
    """
    rec_engine = VeryEasyRecommendationEngine(model_name=request.GET["model_name"])
    # TODO: Paginate this via Paginator class: https://docs.djangoproject.com/en/4.0/topics/pagination/
    # See also https://stackoverflow.com/a/54755628/2532070
    response_data = rec_engine.get_data()

    return JsonResponse(response_data)
