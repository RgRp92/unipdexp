from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page_0(Page):
    pass
class Page_1(Page):
    pass
class Page_2(Page):
    form_model = 'player'
    form_fields = ['tab_1', 'tab_2', 'tab_3', 'tab_4', 'tab_5', 'tab_6', 'tab_7']




page_sequence = [Page_0, Page_1, Page_2]
