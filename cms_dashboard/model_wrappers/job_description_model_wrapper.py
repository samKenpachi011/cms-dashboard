from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .employee_model_wrapper_mixin import EmployeeModelWrapperMixin
from .consultant_model_wrapper_mixin import ConsultantModelWrapperMixin
from .pi_model_wrapper_mixin import PiModelWrapperMixin


class JobDescriptionModelWrapper(ModelWrapper):

    model = 'contract.jobdescription'
    querystring_attrs = ['contract', 'identifier', 'job_title', 'supervisor',
                         'department']
    next_url_attrs = ['identifier', ]
    next_url_name = settings.DASHBOARD_URL_NAMES.get('employee_dashboard_url')


    @property
    def identifier(self):
        return self.object.identifier

    @property
    def supervisor(self):
        return self.object.supervisor

    @property
    def department(self):
        return self.object.department