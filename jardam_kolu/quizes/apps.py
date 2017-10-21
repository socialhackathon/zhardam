import logging
import pkgutil

from django.apps import AppConfig
from django.conf import settings
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
        for scenario in cls.scenarios:
            if 'debug' in scenario.script:
                debug_scenario = scenario
        d = cls.scenarios.copy()
        d.remove(debug_scenario)
        if settings.DEBUG:
            return debug_scenario
        else:
            return d[0]  # why? I don't care

    def ready(self):
        from . import scenarios

        package = scenarios
        prefix = package.__name__ + "."

        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            if '__' in modname or ispkg:
                continue

            module = __import__(modname, fromlist=prefix)

            logger.debug("Importing {} module.".format(modname))
            if not hasattr(module, 'scenario'):
                continue
            scenario = Scenario(
                script=modname, scenario=module.scenario,
            )

            if scenario.is_valid():
                self.scenarios.append(scenario)
