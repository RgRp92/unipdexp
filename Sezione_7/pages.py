from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page_0(Page):
    pass

class Page_1(Page):
    pass

class Page_2(Page):
    pass

class Page_3(Page):
    form_model = 'player'
    form_fields = ['year','year_azienda','gender','istruzione','area','areagrain']

class Page_4(Page):
    form_model = 'player'
    form_fields = ['title','status','businesstype',]

class Page_5(Page):
    form_model = 'player'
    form_fields = ['revenue','q11','q12','q13','q14']

class Page_6(Page):
    form_model = 'player'
    form_fields = ['q15','q16','q17','q18','q19','q20','q21','q22']

class Page_7(Page):
    form_model = 'player'
    form_fields = ['q23','q24','q25','q26','q27','q28']

class Page_8(Page):
    form_model = 'player'
    form_fields = ['q29','q30','q31','q32']

class Page_9(Page):
    form_model = 'player'
    form_fields = ['likert1','likert2','likert3','likert4','likert5','likert6','likert7','likert8']


class Page_10(Page):
    form_model = 'player'
    form_fields = ['likert9','likert10','likert11','likert12','likert13']

class Page_11(Page):
    form_model = 'player'
    form_fields = ['likert14','likert15','likert16','likert17','likert18']

class Page_12(Page):
    form_model = 'player'
    form_fields = ['likert19','likert20','likert21','likert22','likert23','likert24']


page_sequence = [Page_0,
                 Page_1,
                 Page_2,
                 Page_3,
                 Page_4,
                 Page_5,
                 Page_6,
                 Page_7,
                 Page_8,
                 Page_9,
                 Page_10,
                 Page_11,
                 Page_12]
