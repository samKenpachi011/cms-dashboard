from django.apps import apps as django_apps
from django.conf import settings

from edc_model_wrapper import ModelWrapper

from .employee_model_wrapper_mixin import EmployeeModelWrapperMixin
from .performance_imp_model_wrapper_mixin import PerformanceImpModelWrapperMixin


class AppraisalModelWrapper(EmployeeModelWrapperMixin,
                            PerformanceImpModelWrapperMixin, ModelWrapper):

    model = 'contract.performanceassessment'
    querystring_attrs = ['contract', 'performance_assessment']
    next_url_attrs = ['contract', 'performance_assessment']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')

    @property
    def contract(self):
        return self.object.contract

    @property
    def contract_cls(self):
        return django_apps.get_model('contract.contract')
