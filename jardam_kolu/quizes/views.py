from rest_framework.response import Response
from rest_framework.decorators import api_view

from .apps import QuizAppConfig


@api_view(['GET', ])
def get_scenario(request):
    scenario = QuizAppConfig.get_scenario()
    return Response(
        scenario.scenario
    )
