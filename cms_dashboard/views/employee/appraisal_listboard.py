import re
from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin

from ...model_wrappers import AppraisalModelWrapper


class AppraisalListBoardView(
        NavbarViewMixin, EdcBaseViewMixin, ListboardFilterViewMixin,
        SearchFormViewMixin, ListboardView):

    listboard_template = 'appraisal_listboard_template'
    listboard_url = 'appraisal_listboard_url'
    listboard_panel_style = 'info'
    listboard_fa_icon = "fa-user-plus"

    model = 'contract.performanceassessment'
    model_wrapper_cls = AppraisalModelWrapper
    navbar_name = 'cms_dashboard'
    navbar_selected_item = None
    ordering = '-modified'
    paginate_by = 10
    search_form_url = 'appraisal_listboard_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contract = self.kwargs.get('contract')
        model_cls = django_apps.get_model('contract.performanceassessment')
        wrapped = self.model_wrapper_cls(
            model_cls(contract=self.contract_obj,
                      emp_identifier=self.contract_obj.identifier))
        context.update(
            contract=contract,
            appraisal_add_url=wrapped.href,
        )
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('identifier'):
            options.update(
                {'identifier': kwargs.get('identifier')})
        if kwargs.get('contract'):
            options.update(
                {'contract': kwargs.get('contract')})
        options.update()
        return options

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q

    @property
    def contract_obj(self):
        contract_model_cls = django_apps.get_model('contract.contract')
        try:
            contract = contract_model_cls.objects.get(
                id=self.kwargs.get('contract'))
        except contract_model_cls.DoesNotExist:
            raise ValidationError('Please make sure this contract exists.')
        else:
            return contract
