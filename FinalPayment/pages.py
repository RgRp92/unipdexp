from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Page_0(Page):
    pass


class Page_1(Page):
    def vars_for_template(self):
        return {
        'app' : self.session.vars["app"],
        'id':   self.player.id_in_group
        }


class Sezione_2(Page):
    def vars_for_template(self):
        return{
        "beliefs": self.participant.vars["beliefs_results"],
        "w_amt": self.participant.vars["w_amt"],
        "nw_bin": self.participant.vars["nw_bin"]
        }

    def is_displayed(self):
        return self.session.vars["app"] == 2

    def before_next_page(self):
        self.player.payoff = round(self.participant.vars["w_amt"],2)

class Sezione_3(Page):
    def vars_for_template(self):


        return {
            'payoff_HL': self.player.participant.vars['payoff_HL'],
            'row': self.participant.vars['w_row'],  # randomly chosen row
            'value': self.session.vars['HL_random'],  # randomly chosen value to define outcome
            'choice1': self.participant.vars['choices'][0],
            'choice2': self.participant.vars['choices'][1],
            'choice3': self.participant.vars['choices'][2],
            'choice4': self.participant.vars['choices'][3],
            'a1_value': self.participant.vars['a1_value'],
            'a2_value': self.participant.vars['a2_value'],
            'a3_value': self.participant.vars['a3_value'],
            'a4_value': self.participant.vars['a4_value'],

        }

    def is_displayed(self):
        return self.session.vars["app"] == 3

    def before_next_page(self):
        self.player.payoff = self.player.participant.vars['payoff_HL']



class Sezione_5(Page):
    def vars_for_template(self):
        return{
        "nbeliefs": self.participant.vars["nbeliefs_results"],
        "nw_amt": self.participant.vars["nw_amt"],
        "nw_bin": self.participant.vars["nw_bin"]
        }

    def is_displayed(self):
        return self.session.vars["app"] == 5

    def before_next_page(self):
        self.player.payoff = round(self.participant.vars["nw_amt"],2)

class Sezione_6(Page):
    def vars_for_template(self):
        return {
            'payoff_HLr': self.player.participant.vars['payoff_HLr'],
            'rrow': self.participant.vars['w_rrow'],  # randomly chosen row
            'rvalue': self.session.vars['rHL_random'],  # randomly chosen value to define outcome
            'rchoice1': self.participant.vars['rchoices'][0],
            'rchoice2': self.participant.vars['rchoices'][1],
            'rchoice3': self.participant.vars['rchoices'][2],
            'rchoice4': self.participant.vars['rchoices'][3],
            'ra1_value': self.participant.vars['ra1_value'],
            'ra2_value': self.participant.vars['ra2_value'],
            'ra3_value': self.participant.vars['ra3_value'],
            'ra4_value': self.participant.vars['ra4_value'],
        }

    def is_displayed(self):
        return self.session.vars["app"] == 6

    def before_next_page(self):
            self.player.payoff = self.player.participant.vars['payoff_HLr']


class Goodbye_Winner(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
        'app' : self.session.vars["app"],
        'id':   self.player.id_in_group
        }



page_sequence = [Page_0, Page_1, Sezione_2, Sezione_3, Sezione_5, Sezione_6, Goodbye_Winner]
