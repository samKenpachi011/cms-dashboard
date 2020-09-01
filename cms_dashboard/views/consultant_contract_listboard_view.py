from .base_listboard_view import BaseListBoardView


class ConsultantContractListBoardView(BaseListBoardView):

    listboard_url = 'consultant_contract_listboard_url'
    navbar_selected_item = 'consultant'
    search_form_url = 'consultant_contract_listboard_url'

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(
            request, identifier__startwith="C", *args, **kwargs)
        return options
