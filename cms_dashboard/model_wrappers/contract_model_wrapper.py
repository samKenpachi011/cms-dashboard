from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .employee_model_wrapper_mixin import EmployeeModelWrapperMixin


class ContractModelWrapper(EmployeeModelWrapperMixin, ModelWrapper):

    model = 'contract.contract'
    querystring_attrs = ['identifier']
    next_url_attrs = ['identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('contract_listboard_url')
