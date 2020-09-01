"""potlako_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/"""
from edc_dashboard import UrlConfig

from .patterns import identifier
from .views import (
    ContractListBoardView, ConsultantListBoardView,
    EmployeeListBoardView, PiListBoardView, AllEmployeesListBoardView)

app_name = 'cms_dashboard'

contract_listboard_url_config = UrlConfig(
    url_name='contract_listboard_url',
    view_class=ContractListBoardView,
    label='contract_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

consultant_listboard_url_config = UrlConfig(
    url_name='consultant_listboard_url',
    view_class=ConsultantListBoardView,
    label='consultant_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

employee_dashboard_url_config = UrlConfig(
    url_name='employee_listboard_url',
    view_class=EmployeeListBoardView,
    label='employee_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

allemployees_dashboard_url_config = UrlConfig(
    url_name='allemployees_listboard_url',
    view_class=AllEmployeesListBoardView,
    label='allemployees_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

pi_dashboard_url_config = UrlConfig(
    url_name='pi_listboard_url',
    view_class=PiListBoardView,
    label='pi_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

urlpatterns = []
urlpatterns += contract_listboard_url_config.listboard_urls
urlpatterns += consultant_listboard_url_config.listboard_urls
urlpatterns += employee_dashboard_url_config.listboard_urls
urlpatterns += allemployees_dashboard_url_config.listboard_urls
urlpatterns += pi_dashboard_url_config.listboard_urls

