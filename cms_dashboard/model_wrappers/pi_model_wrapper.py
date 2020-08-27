from django.conf import settings
from edc_model_wrapper import ModelWrapper


class PiModelWrapper(ModelWrapper):

    model = 'contract.pi'
    querystring_attrs = ['identifier']
    next_url_attrs = ['identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('pi_listboard_url')
