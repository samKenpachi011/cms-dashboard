from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin


class DashboardView(NavbarViewMixin, EdcBaseViewMixin, TemplateView):
    
    template_name = 'cms_dashboard/dashboard.html'
    navbar_name = 'cms_dashboard'


    @property
    def contracts(self):
        """Returns a Queryset of all contracts for this subject.
        """
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update()
        return context


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)