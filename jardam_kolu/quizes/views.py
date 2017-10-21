from django.utils.translation import get_language_from_request
from rest_framework.response import Response

from .apps import QuizAppConfig


def get_scenario(request):
    scenario = QuizAppConfig.get_scenario()
    return Response(
        scenario.as_json()
    )
