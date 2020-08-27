from .contract_model_wrapper import ContractModelWrapper


class ContractObj:

    @property
    def contract_obj(self):
        """Return today's temperature obj or an empty wrapped temperature obj.
        """
        contracts = self.contract_cls.objects.filter(
            identifier=self.identifier)
        if contracts:
            # contract = contracts.order_by('start_date').last()
            # if contract.start_date == get_utcnow().year():
            #     return ContractModelWrapper(
            #         contract, next_url_name=self.next_url_name)

            return ContractModelWrapper(
                self.contract_cls(identifier=self.identifier),
                next_url_name=self.next_url_name)
