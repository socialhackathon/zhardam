import logging
import pkgutil

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .utils import Scenario

logger = logging.getLogger('Quizes')


class QuizAppConfig(AppConfig):
    name = 'jardam_kolu.quizes'
    verbose_name = _('Quizes')
    scenarios = []

    @classmethod
    def get_scenarios(cls):
        return cls.scenarios

    @classmethod
    def get_scenario(cls):
        return cls.scenarios[0]  # why? I don't care

    def ready(self):
        from . import scenarios

        package = scenarios
        prefix = package.__name__ + "."

        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            if '__' in modname:
                continue
            module = __import__(modname)

            logger.debug("Importing {} module.".format(modname))
            print(modname)
            if not hasattr(module, 'scenario'):
                continue
            scenario = Scenario(
                script=modname, scenario=module.scenario,
            )
            if scenario.is_valid():
                self.scenarios.append(scenarios)
