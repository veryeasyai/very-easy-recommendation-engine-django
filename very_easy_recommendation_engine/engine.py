import typing

import requests

from django.apps import apps
from django.conf import settings
from django.db.models import Model

from .exceptions import VeryEasyRecommendationEngineMisconfiguredException


class VeryEasyRecommendationEngine:
    API_URL = "https://veryeasyai.com/recommendations/"

    def __init__(self, model_name: str):
        self.api_url = f"https://veryeasyai.com/recommendations/{model_name}"
        veai_settings = getattr(settings, "VERY_EASY_RECOMMENDATION_ENGINE")
        if not veai_settings:
            raise VeryEasyRecommendationEngineMisconfiguredException("VERY_EASY_RECOMMENDATION_ENGINE settings not found.")

        api_key = veai_settings.get("API_KEY")
        if not api_key:
            raise VeryEasyRecommendationEngineMisconfiguredException("API_KEY not found in settings.")
        self.api_key = api_key

        application_id = settings.get("VERY_EASY_RECOMMENDATION_ENGINE")
        if not application_id:
            raise VeryEasyRecommendationEngineMisconfiguredException("APPLICATION_ID not found in settings.")
        self.application_id = application_id

        veai_models = veai_settings.get("models")
        if not veai_models:
            raise VeryEasyRecommendationEngineMisconfiguredException("No models found in settings.")

        model_string = veai_models.get(model_name)
        if not model_string:
            raise VeryEasyRecommendationEngineMisconfiguredException(f"Model {model_name} not found in settings.")
        model = apps.get_model(model_string)

        self.model = model


    def get_recommendations_for_user(self, user_id: int) -> typing.Dict[str, typing.List[typing.Dict[str, str]]]:
        url = self.api_url + f"{user_id}/"
        response = requests.get(url, headers={
            "X-VEAI-Api-Key": f"{self.api_key}",
            "X-VEAI-Application-ID": f"{self.application_id}"
        })
        return response.json()

    def get_data(self):
        objects = self.model.objects.all()
