from django import template
# from django.conf import settings
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('cms_dashboard/buttons/appraisal_listboard_button.html')
def appraisal_listboard_button(model_wrapper):
    title = ['Appraise employee.']
    url_name = "cms_dashboard:appraisal_listboard_url"
    redirect_url = reverse(url_name, kwargs={'contract': model_wrapper.id})
    return dict(
        href=redirect_url,
        contract=model_wrapper,
        title=' '.join(title))


@register.inclusion_tag('cms_dashboard/buttons/edit_appraisal_button.html')
def edit_appraisal_button(model_wrapper):
    title = ['Edit appraisal form.']
    return dict(
        # identifier=model_wrapper.object.identifier,
        href=model_wrapper.href,
        title=' '.join(title))


@register.inclusion_tag('cms_dashboard/buttons/edit_details_button.html')
def edit_details_button(model_wrapper):
    title = ['Edit details form.']
    return dict(
        identifier=model_wrapper.object.identifier,
        href=model_wrapper.href,
        title=' '.join(title))


@register.inclusion_tag('cms_dashboard/buttons/performance_imp_button.html')
def add_performance_imp_button(model_wrapper):
    title = ['Add performance improvement plan.']
    return dict(
        performance_assessment=model_wrapper.object,
        add_performance_imp=model_wrapper.performance_imp.href,
        title=' '.join(title))
