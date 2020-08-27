from django.apps import apps as django_apps
from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .contract_model_wrapper_mixin import ContractObj


class EmployeeModelWrapper(ContractObj, ModelWrapper):

    model = 'contract.employee'
    querystring_attrs = ['identifier']
    next_url_attrs = ['identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('employee_listboard_url')

    @property
    def contract_cls(self):
        return django_apps.get_model('contract.contract')
