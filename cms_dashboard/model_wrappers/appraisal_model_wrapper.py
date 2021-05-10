from django.apps import apps as django_apps
from django.conf import settings

from edc_model_wrapper import ModelWrapper

from .employee_model_wrapper_mixin import EmployeeModelWrapperMixin
from .kpa_model_wrapper_mixin import KpaModelWrapperMixin
from .kpa_model_wrapper import KpaModelWrapper
from .professional_skills_model_wrapper_mixin import (
    StrategicOrientationModelWrapperMixin, ResultsFocusModelWrapperMixin,
    LeadershipAndMotivationModelWrapperMixin,
    InnovationAndCreativityModelWrapperMixin, PlanningSkillsModelWrapperMixin,
    InterpersonalSkillsModelWrapperMixin, CommunicationSkillsModelWrapperMixin,
    KnowledgeAndProductivityModelWrapperMixin, QualityOfWorkModelWrapperMixin)
from .performance_imp_model_wrapper_mixin import \
    PerformanceImpModelWrapperMixin


class AppraisalModelWrapper(EmployeeModelWrapperMixin,
                            PerformanceImpModelWrapperMixin,
                            KpaModelWrapperMixin,
                            QualityOfWorkModelWrapperMixin,
                            KnowledgeAndProductivityModelWrapperMixin,
                            CommunicationSkillsModelWrapperMixin,
                            InterpersonalSkillsModelWrapperMixin,
                            PlanningSkillsModelWrapperMixin,
                            InnovationAndCreativityModelWrapperMixin,
                            LeadershipAndMotivationModelWrapperMixin,
                            ResultsFocusModelWrapperMixin,
                            StrategicOrientationModelWrapperMixin,
                            ModelWrapper):

    model = 'bhp_personnel.performanceassessment'
    querystring_attrs = ['contract', 'emp_identifier', ]
    next_url_attrs = ['contract', 'emp_identifier', ]
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')

    @property
    def contract(self):
        return self.object.contract

    @property
    def emp_identifier(self):
        return self.object.emp_identifier

    @property
    def contract_cls(self):
        return django_apps.get_model('bhp_personnel.contract')

    # @property
    # def kpa_cls(self):
    #     return django_apps.get_model(
    #         'bhp_personnel.keyperformancearea')

    @property
    def kpa_cls(self):
        return django_apps.get_model('bhp_personnel.keyperformancearea')

    @property
    def kpa_list(self):
        wrapped_kpas = []
        kpas = self.kpa_cls.objects.filter(contract=self.contract)
        for kpa in kpas:
            wrapped_kpas.append(KpaModelWrapper(kpa))
        return wrapped_kpas
