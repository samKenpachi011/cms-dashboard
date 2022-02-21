from edc_base.utils import get_utcnow
from edc_dashboard.listboard_filter import ListboardFilter, \
    ListboardViewFilters


class EmployeeListBoardFilters(ListboardViewFilters):

    all = ListboardFilter(
        name='all',
        label='All',
        lookup={})