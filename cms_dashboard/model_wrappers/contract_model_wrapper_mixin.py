from django.apps import apps as django_apps

from .contract_model_wrapper import ContractModelWrapper


class ContractModelWrapperMixin:

    @property
    def contract_obj(self):
        return ContractModelWrapper(
            self.contract_cls(identifier=self.identifier),
            next_url_name=self.next_url_name)

    @property
    def contract_cls(self):
        return django_apps.get_model('contract.contract')
