from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Page_0(Page):
    pass


class Page_1(Page):
    def vars_for_template(self):
        return {
        "winners": self.session.vars['winners'],
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
        payoff_HLc = round((self.player.participant.vars['payoff_HL']/1000) * (1.06),2)
        # retrieve values from participant.vars and store them in a dictionary

        if self.session.vars['HL_scenario'] <= 30 :
            price = 24.00
        elif  self.session.vars['HL_scenario'] > 30 and self.session.vars['HL_scenario'] <= 54:
            price = 26.00
        elif self.session.vars['HL_scenario'] > 54 and self.session.vars['HL_scenario'] <= 73:
            price = 28.00
        elif self.session.vars['HL_scenario'] > 73 and self.session.vars['HL_scenario'] <= 88:
            price = 30.00
        elif self.session.vars['HL_scenario'] > 88 and self.session.vars['HL_scenario'] <= 90:
            price = 32.00
        elif self.session.vars['HL_scenario'] > 90 and self.session.vars['HL_scenario'] <= 100:
            price = 34.00

        self.participant.vars['price'] = price

        return {
            'payoff_HL': self.player.participant.vars['payoff_HL'],
            'row': self.player.session.vars['HL_row'],  # randomly chosen row
            'value': self.session.vars['HL_random'],  # randomly chosen value to define outcome
            'value2': self.session.vars['HL_scenario'],
            'choice': self.participant.vars['choices'],  # actual choice
            # outcomes of the selected row
            'a1_value': self.participant.vars['a1_value'],
            'price': self.participant.vars['price'],
            'p_A_1': self.session.vars['HL_row'],
            'p_A_2': 10 - self.session.vars['HL_row'],
            'p_B_1': self.session.vars['HL_row'],
            'p_B_2': 10 - self.session.vars['HL_row'],

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
        payoff_HLc = round((self.player.participant.vars['payoff_HL']/1000) * (1.06),2)
        # retrieve values from participant.vars and store them in a dictionary

        if  self.session.vars['rHL_scenario'] <= 30 :
            rprice =  24.00
        elif   self.session.vars['rHL_scenario'] > 30 and  self.session.vars['rHL_scenario'] <= 54:
            rprice = 26.00
        elif  self.session.vars['rHL_scenario'] > 54 and self.session.vars['rHL_scenario'] <= 73:
            rprice = 28.00
        elif self.session.vars['rHL_scenario'] > 73 and  self.session.vars['rHL_scenario'] <= 88:
            rprice = 30.00
        elif  self.session.vars['rHL_scenario'] > 88 and  self.session.vars['rHL_scenario'] <= 90:
            rprice = 32.00
        elif  self.session.vars['rHL_scenario'] > 90 and  self.session.vars['rHL_scenario'] <= 100:
            rprice = 34.00

        self.participant.vars['rprice'] = rprice

        return {
            'rpayoff_HL': self.player.participant.vars['rpayoff_HL'],
            'rrow': self.player.session.vars['rHL_row'],  # randomly chosen row
            'rvalue': self.session.vars['rHL_random'],  # randomly chosen value to define outcome
            'rvalue2': self.session.vars['rHL_scenario'],
            'rchoice': self.participant.vars['rchoices'],  # actual choice
            # outcomes of the selected row
            'ra1_value': self.participant.vars['ra1_value'],
            'rprice': self.participant.vars['rprice'],
            'rp_A_1': self.session.vars['rHL_row'],
            'rp_A_2': 10 - self.session.vars['rHL_row'],
            'rp_B_1': self.session.vars['rHL_row'],
            'rp_B_2': 10 - self.session.vars['rHL_row'],

        }

    def is_displayed(self):
        return self.session.vars["app"] == 6

    def before_next_page(self):
        self.player.payoff = self.player.participant.vars['payoff_rHL']


class Goodbye_Winner(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
        "winners": self.session.vars["winners"],
        'app' : self.session.vars["app"],
        'id':   self.player.id_in_group
        }
    def is_displayed(self):
        return self.player.id_in_group in self.session.vars["winners"]

class Goodbye(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
        "winners": self.session.vars["winners"],
        'app' : self.session.vars["app"],
        'id':   self.player.id_in_group
        }
    def is_displayed(self):
        return self.player.id_in_group not in self.session.vars["winners"]


page_sequence = [Page_0, Page_1, Sezione_2, Sezione_3, Sezione_5, Sezione_6, Goodbye_Winner,Goodbye]
