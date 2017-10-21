from django.test import TestCase
from jardam_kolu.quizes.utils import Scenario


class ScenarioValidatorTestCase(TestCase):
    def test_simple_success(self):
        scenario = {
            '1': {
                'text': 'question 1',
                'answers': {
                    'a1': {
                        'text': 'answer 1 for question 1',
                        'type': 'question',
                        'content': '2'
                    }
                }
            },
            '2': {
                'text': 'question 2',
                'image': 'http://example.com/image_url/',
                'answers': {
                    'a2_1': {
                        'text': 'answer 1 for question 2',
                        'type': 'article',
                        'content': 'https://yolo.swag/keke.pepe.html'
                    }
                }
            }
        }
        scenario_object = Scenario(
            script='yoloswag',
            scenario=scenario
        )
        self.assertTrue(scenario_object.is_valid())
