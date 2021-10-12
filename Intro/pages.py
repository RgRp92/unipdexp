from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page_0(Page):
    pass

class Obiettivi_Studio(Page):
    pass

class Struttura_Studio(Page):
    pass

class Struttura_Studio2(Page):
    pass

class Compenso_base(Page):
    pass

class Compenso_aggiuntivo(Page):
    pass

class Compenso_aggiuntivo2(Page):
    def vars_for_template(self):
        return {
            "n_winners": self.session.vars['n_winners']
        }

class Privacy(Page):
    pass

page_sequence = [Page_0,
                 Obiettivi_Studio,
                 Struttura_Studio,
                 Struttura_Studio2,
                 Compenso_base,
                 Compenso_aggiuntivo,
                 Compenso_aggiuntivo2,
                 Privacy]
