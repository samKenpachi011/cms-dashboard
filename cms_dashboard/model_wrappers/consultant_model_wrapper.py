from edc_model_wrapper import ModelWrapper

from contract.models import Employee, Consultant, Pi
from .contract_model_wrapper_mixin import ContractModelWrapperMixin


class ConsultantModelWrapper(ContractModelWrapperMixin, ModelWrapper):

    model = 'contract.consultant'
    querystring_attrs = ['identifier']
    next_url_attrs = ['identifier']
    next_url_name = 'cms_dashboard:dashboard_url'

    def owner(self):
        try:
            employee = Employee.objects.get(identifier=object.identifier)
        except Employee.DoesNotExist:
            pass
        else:
            return f'{employee.first_name} {employee.middle_name} {employee.last_name}'
        try:
            consultant = Consultant.objects.get(identifier=object.identifier)
        except Consultant.DoesNotExist:
            pass
        else:
            return f'{consultant.first_name} {consultant.middle_name} {consultant.last_name}'
        try:
            pi = Pi.objects.get(identifier=object.identifier)
        except Pi.DoesNotExist:
            pass
        else:
            return f'{pi.first_name} {pi.middle_name} {pi.last_name}'
