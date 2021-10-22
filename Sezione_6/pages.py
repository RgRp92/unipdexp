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
    pass

class Page_4(Page):
    form_model = 'player'
    form_fields = ['rHL_1']

    def vars_for_template(self):
        rfix = Constants.rfix

        return {
            'rHL_1': rfix[0],
        }

class Page_5(Page):
    form_model = 'player'
    form_fields = ['rHL_2']

    def vars_for_template(self):
        if self.player.rHL_1 == 1:
            self.participant.vars['new_rfix']=[
                round(19 , 2),
                round(20 , 2),
                round(21 , 2),
                round(22 , 2)]
            return {
                'rHL10': 19 ,
                'rHL11': 20 ,
                'rHL12': 21 ,
                'rHL13': 22 ,
            }
        elif self.player.rHL_1 == 2:
            rfix = Constants.rfix[0]
            self.participant.vars['new_rfix']=[
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL10': rfix + 1,
                'rHL11': rfix + 2,
                'rHL12': rfix + 3,
                'rHL13': rfix + 4,
            }
        elif self.player.rHL_1 == 3:
            rfix = Constants.rfix[1]
            self.participant.vars['new_rfix'] = [
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL10': rfix + 1,
                'rHL11': rfix + 2,
                'rHL12': rfix + 3,
                'rHL13': rfix + 4,
            }
        elif self.player.rHL_1 == 4:
            rfix = Constants.rfix[2]
            self.participant.vars['new_rfix'] = [
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL10': rfix + 1,
                'rHL11': rfix + 2,
                'rHL12': rfix + 3,
                'rHL13': rfix + 4,
            }
        elif self.player.rHL_1 == 5:
            rfix = Constants.rfix[3]
            self.participant.vars['new_rfix'] = [
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL10': rfix + 1,
                'rHL11': rfix + 2,
                'rHL12': rfix + 3,
                'rHL13': rfix + 4,
            }
        elif self.player.rHL_1 == 6:
            rfix = Constants.rfix[4]
            self.participant.vars['new_rfix'] = [
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL10': rfix + 1,
                'rHL11': rfix + 2,
                'rHL12': rfix + 3,
                'rHL13': rfix + 4,
            }
        elif self.player.rHL_1 == 7:
            rfix = Constants.rfix[5]
            self.participant.vars['new_rfix'] = [
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL10': rfix + 1,
                'rHL11': rfix + 2,
                'rHL12': rfix + 3,
                'rHL13': rfix + 4,
            }
        elif self.player.rHL_1 == 8:
            rfix = Constants.rfix[6]
            self.participant.vars['new_rfix'] = [
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL10': rfix + 1,
                'rHL11': rfix + 2,
                'rHL12': rfix + 3,
                'rHL13': rfix + 4,
            }
        elif self.player.rHL_1 == 9:
            rfix = Constants.rfix[7]
            self.participant.vars['new_rfix'] = [
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL10': rfix + 1,
                'rHL11': rfix + 2,
                'rHL12': rfix + 3,
                'rHL13': rfix + 4,
            }
        elif self.player.rHL_1 == 10:
            rfix = Constants.rfix[8]
            self.participant.vars['new_rfix'] = [
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL10': rfix + 1,
                'rHL11': rfix + 2,
                'rHL12': rfix + 3,
                'rHL13': rfix + 4,
            }
class Page_6(Page):
    form_model = 'player'
    form_fields = ['rHL_3']

    def vars_for_template(self):
        if self.player.rHL_2 == 10:
            rfix = self.participant.vars['new_rfix'][0]
            self.participant.vars['new_rfix2']=[
            round(rfix - 0.9,2),
            round(rfix - 0.8,2),
            round(rfix - 0.7,2),
            round(rfix - 0.6,2),
            round(rfix - 0.5,2),
            round(rfix - 0.4,2),
            round(rfix - 0.3,2),
            round(rfix - 0.2,2),
            round(rfix - 0.1,2),
            round(rfix, 2),
            ]
            return {
                'rHL14': round(rfix - 0.9,2),
                'rHL15': round(rfix - 0.8,2),
                'rHL16': round(rfix - 0.7,2),
                'rHL17': round(rfix - 0.6,2),
                'rHL18': round(rfix - 0.5,2),
                'rHL19': round(rfix - 0.4,2),
                'rHL20': round(rfix - 0.3, 2),
                'rHL21': round(rfix - 0.2, 2),
                'rHL22': round(rfix - 0.1, 2),
                'rHL23': round(rfix ,2)}
        elif self.player.rHL_2 == 11:
                rfix = self.participant.vars['new_rfix'][0]
                self.participant.vars['new_rfix2'] = [
                    round(rfix + 0.1, 2),
                    round(rfix + 0.2, 2),
                    round(rfix + 0.3, 2),
                    round(rfix + 0.4, 2),
                    round(rfix + 0.5, 2),
                    round(rfix + 0.6, 2),
                    round(rfix + 0.7, 2),
                    round(rfix + 0.8, 2),
                    round(rfix + 0.9, 2),
                    round(rfix + 1, 2),
                ]
                return {
                    'rHL14': round(rfix + 0.1, 2),
                    'rHL15': round(rfix + 0.2, 2),
                    'rHL16': round(rfix + 0.3, 2),
                    'rHL17': round(rfix + 0.4, 2),
                    'rHL18': round(rfix + 0.5, 2),
                    'rHL19': round(rfix + 0.6, 2),
                    'rHL20': round(rfix + 0.7, 2),
                    'rHL21': round(rfix + 0.8, 2),
                    'rHL22': round(rfix + 0.9, 2),
                    'rHL23': round(rfix + 1, 2)}
        elif self.player.rHL_2 == 12:
                rfix = self.participant.vars['new_rfix'][1]
                self.participant.vars['new_rfix2'] = [
                    round(rfix + 0.1, 2),
                    round(rfix + 0.2, 2),
                    round(rfix + 0.3, 2),
                    round(rfix + 0.4, 2),
                    round(rfix + 0.5, 2),
                    round(rfix + 0.6, 2),
                    round(rfix + 0.7, 2),
                    round(rfix + 0.8, 2),
                    round(rfix + 0.9, 2),
                    round(rfix + 1, 2),
                ]
                return {
                    'rHL14': round(rfix + 0.1, 2),
                    'rHL15': round(rfix + 0.2, 2),
                    'rHL16': round(rfix + 0.3, 2),
                    'rHL17': round(rfix + 0.4, 2),
                    'rHL18': round(rfix + 0.5, 2),
                    'rHL19': round(rfix + 0.6, 2),
                    'rHL20': round(rfix + 0.7, 2),
                    'rHL21': round(rfix + 0.8, 2),
                    'rHL22': round(rfix + 0.9, 2),
                    'rHL23': round(rfix + 1, 2)}
        elif self.player.rHL_2 == 13:
                rfix = self.participant.vars['new_rfix'][2]
                self.participant.vars['new_rfix2'] = [
                    round(rfix + 0.1, 2),
                    round(rfix + 0.2, 2),
                    round(rfix + 0.3, 2),
                    round(rfix + 0.4, 2),
                    round(rfix + 0.5, 2),
                    round(rfix + 0.6, 2),
                    round(rfix + 0.7, 2),
                    round(rfix + 0.8, 2),
                    round(rfix + 0.9, 2),
                    round(rfix + 1, 2),
                ]
                return {
                    'rHL14': round(rfix + 0.1, 2),
                    'rHL15': round(rfix + 0.2, 2),
                    'rHL16': round(rfix + 0.3, 2),
                    'rHL17': round(rfix + 0.4, 2),
                    'rHL18': round(rfix + 0.5, 2),
                    'rHL19': round(rfix + 0.6, 2),
                    'rHL20': round(rfix + 0.7, 2),
                    'rHL21': round(rfix + 0.8, 2),
                    'rHL22': round(rfix + 0.9, 2),
                    'rHL23': round(rfix + 1, 2)}

class Page_7(Page):
    form_model = 'player'
    form_fields = ['rHL_4']

    def vars_for_template(self):
        if self.player.rHL_3 == 14:
            rfix = self.participant.vars['new_rfix2'][0]
            self.participant.vars['new_rfix3'] = [
                round(rfix - 0.09, 2),
                round(rfix - 0.08, 2),
                round(rfix - 0.07, 2),
                round(rfix - 0.06, 2),
                round(rfix - 0.05, 2),
                round(rfix - 0.04, 2),
                round(rfix - 0.03, 2),
                round(rfix - 0.02, 2),
                round(rfix - 0.01, 2),
                round(rfix, 2),
            ]
            return {
                'rHL24': round(rfix - 0.09, 2),
                'rHL25': round(rfix - 0.08, 2),
                'rHL26': round(rfix - 0.07, 2),
                'rHL27': round(rfix - 0.06, 2),
                'rHL28': round(rfix - 0.05, 2),
                'rHL29': round(rfix - 0.04, 2),
                'rHL30': round(rfix - 0.03, 2),
                'rHL31': round(rfix - 0.02, 2),
                'rHL32': round(rfix - 0.01, 2),
                'rHL33': round(rfix , 2)
            }
        elif self.player.rHL_3 == 15:
            rfix = self.participant.vars['new_rfix2'][0]
            self.participant.vars['new_rfix3'] = [
                round(rfix + 0.01, 2),
                round(rfix + 0.02, 2),
                round(rfix + 0.03, 2),
                round(rfix + 0.04, 2),
                round(rfix + 0.05, 2),
                round(rfix + 0.06, 2),
                round(rfix + 0.07, 2),
                round(rfix + 0.08, 2),
                round(rfix + 0.09, 2),
                round(rfix + 0.10, 2),
            ]
            return {
                'rHL24': round(rfix + 0.01, 2),
                'rHL25': round(rfix + 0.02, 2),
                'rHL26': round(rfix + 0.03, 2),
                'rHL27': round(rfix + 0.04, 2),
                'rHL28': round(rfix + 0.05, 2),
                'rHL29': round(rfix + 0.06, 2),
                'rHL30': round(rfix + 0.07, 2),
                'rHL31': round(rfix + 0.08, 2),
                'rHL32': round(rfix + 0.09, 2),
                'rHL33': round(rfix + 0.10, 2)
            }
        elif self.player.rHL_3 == 16:
            rfix = self.participant.vars['new_rfix2'][1]
            self.participant.vars['new_rfix3'] = [
                round(rfix + 0.01, 2),
                round(rfix + 0.02, 2),
                round(rfix + 0.03, 2),
                round(rfix + 0.04, 2),
                round(rfix + 0.05, 2),
                round(rfix + 0.06, 2),
                round(rfix + 0.07, 2),
                round(rfix + 0.08, 2),
                round(rfix + 0.09, 2),
                round(rfix + 0.10, 2),
            ]
            return {
                'rHL24': round(rfix + 0.01, 2),
                'rHL25': round(rfix + 0.02, 2),
                'rHL26': round(rfix + 0.03, 2),
                'rHL27': round(rfix + 0.04, 2),
                'rHL28': round(rfix + 0.05, 2),
                'rHL29': round(rfix + 0.06, 2),
                'rHL30': round(rfix + 0.07, 2),
                'rHL31': round(rfix + 0.08, 2),
                'rHL32': round(rfix + 0.09, 2),
                'rHL33': round(rfix + 0.10, 2)
            }
        elif self.player.rHL_3 == 17:
            rfix = self.participant.vars['new_rfix2'][2]
            self.participant.vars['new_rfix3'] = [
                round(rfix + 0.01, 2),
                round(rfix + 0.02, 2),
                round(rfix + 0.03, 2),
                round(rfix + 0.04, 2),
                round(rfix + 0.05, 2),
                round(rfix + 0.06, 2),
                round(rfix + 0.07, 2),
                round(rfix + 0.08, 2),
                round(rfix + 0.09, 2),
                round(rfix + 0.10, 2),
            ]
            return {
                'rHL24': round(rfix + 0.01, 2),
                'rHL25': round(rfix + 0.02, 2),
                'rHL26': round(rfix + 0.03, 2),
                'rHL27': round(rfix + 0.04, 2),
                'rHL28': round(rfix + 0.05, 2),
                'rHL29': round(rfix + 0.06, 2),
                'rHL30': round(rfix + 0.07, 2),
                'rHL31': round(rfix + 0.08, 2),
                'rHL32': round(rfix + 0.09, 2),
                'rHL33': round(rfix + 0.10, 2)
            }
        elif self.player.rHL_3 == 18:
            rfix = self.participant.vars['new_rfix2'][3]
            self.participant.vars['new_rfix3'] = [
                round(rfix + 0.01, 2),
                round(rfix + 0.02, 2),
                round(rfix + 0.03, 2),
                round(rfix + 0.04, 2),
                round(rfix + 0.05, 2),
                round(rfix + 0.06, 2),
                round(rfix + 0.07, 2),
                round(rfix + 0.08, 2),
                round(rfix + 0.09, 2),
                round(rfix + 0.10, 2),
            ]
            return {
                'rHL24': round(rfix + 0.01, 2),
                'rHL25': round(rfix + 0.02, 2),
                'rHL26': round(rfix + 0.03, 2),
                'rHL27': round(rfix + 0.04, 2),
                'rHL28': round(rfix + 0.05, 2),
                'rHL29': round(rfix + 0.06, 2),
                'rHL30': round(rfix + 0.07, 2),
                'rHL31': round(rfix + 0.08, 2),
                'rHL32': round(rfix + 0.09, 2),
                'rHL33': round(rfix + 0.10, 2)
            }
        elif self.player.rHL_3 == 19:
            rfix = self.participant.vars['new_rfix2'][4]
            self.participant.vars['new_rfix3'] = [
                round(rfix + 0.01, 2),
                round(rfix + 0.02, 2),
                round(rfix + 0.03, 2),
                round(rfix + 0.04, 2),
                round(rfix + 0.05, 2),
                round(rfix + 0.06, 2),
                round(rfix + 0.07, 2),
                round(rfix + 0.08, 2),
                round(rfix + 0.09, 2),
                round(rfix + 0.10, 2),
]
            return {
                'rHL24': round(rfix + 0.01, 2),
                'rHL25': round(rfix + 0.02, 2),
                'rHL26': round(rfix + 0.03, 2),
                'rHL27': round(rfix + 0.04, 2),
                'rHL28': round(rfix + 0.05, 2),
                'rHL29': round(rfix + 0.06, 2),
                'rHL30': round(rfix + 0.07, 2),
                'rHL31': round(rfix + 0.08, 2),
                'rHL32': round(rfix + 0.09, 2),
                'rHL33': round(rfix + 0.10, 2)
            }
        elif self.player.rHL_3 == 20:
            rfix = self.participant.vars['new_rfix2'][5]
            self.participant.vars['new_rfix3'] = [
                round(rfix + 0.01, 2),
                round(rfix + 0.02, 2),
                round(rfix + 0.03, 2),
                round(rfix + 0.04, 2),
                round(rfix + 0.05, 2),
                round(rfix + 0.06, 2),
                round(rfix + 0.07, 2),
                round(rfix + 0.08, 2),
                round(rfix + 0.09, 2),
                round(rfix + 0.10, 2),
            ]
            return {
                'rHL24': round(rfix + 0.01, 2),
                'rHL25': round(rfix + 0.02, 2),
                'rHL26': round(rfix + 0.03, 2),
                'rHL27': round(rfix + 0.04, 2),
                'rHL28': round(rfix + 0.05, 2),
                'rHL29': round(rfix + 0.06, 2),
                'rHL30': round(rfix + 0.07, 2),
                'rHL31': round(rfix + 0.08, 2),
                'rHL32': round(rfix + 0.09, 2),
                'rHL33': round(rfix + 0.10, 2)
            }
        elif self.player.rHL_3 == 21:
            rfix = self.participant.vars['new_rfix2'][6]
            self.participant.vars['new_rfix3'] = [
                round(rfix + 0.01, 2),
                round(rfix + 0.02, 2),
                round(rfix + 0.03, 2),
                round(rfix + 0.04, 2),
                round(rfix + 0.05, 2),
                round(rfix + 0.06, 2),
                round(rfix + 0.07, 2),
                round(rfix + 0.08, 2),
                round(rfix + 0.09, 2),
                round(rfix + 0.10, 2),
            ]
            return {
                'rHL24': round(rfix + 0.01, 2),
                'rHL25': round(rfix + 0.02, 2),
                'rHL26': round(rfix + 0.03, 2),
                'rHL27': round(rfix + 0.04, 2),
                'rHL28': round(rfix + 0.05, 2),
                'rHL29': round(rfix + 0.06, 2),
                'rHL30': round(rfix + 0.07, 2),
                'rHL31': round(rfix + 0.08, 2),
                'rHL32': round(rfix + 0.09, 2),
                'rHL33': round(rfix + 0.10, 2)
            }
        elif self.player.rHL_3 == 22:
            rfix = self.participant.vars['new_rfix2'][7]
            self.participant.vars['new_rfix3'] = [
                round(rfix + 0.01, 2),
                round(rfix + 0.02, 2),
                round(rfix + 0.03, 2),
                round(rfix + 0.04, 2),
                round(rfix + 0.05, 2),
                round(rfix + 0.06, 2),
                round(rfix + 0.07, 2),
                round(rfix + 0.08, 2),
                round(rfix + 0.09, 2),
                round(rfix + 0.10, 2),
            ]
            return {
                'rHL24': round(rfix + 0.01, 2),
                'rHL25': round(rfix + 0.02, 2),
                'rHL26': round(rfix + 0.03, 2),
                'rHL27': round(rfix + 0.04, 2),
                'rHL28': round(rfix + 0.05, 2),
                'rHL29': round(rfix + 0.06, 2),
                'rHL30': round(rfix + 0.07, 2),
                'rHL31': round(rfix + 0.08, 2),
                'rHL32': round(rfix + 0.09, 2),
                'rHL33': round(rfix + 0.10, 2)
            }
        elif self.player.rHL_3 == 23:
            rfix = self.participant.vars['new_rfix2'][8]
            self.participant.vars['new_rfix3'] = [
                round(rfix + 0.01, 2),
                round(rfix + 0.02, 2),
                round(rfix + 0.03, 2),
                round(rfix + 0.04, 2),
                round(rfix + 0.05, 2),
                round(rfix + 0.06, 2),
                round(rfix + 0.07, 2),
                round(rfix + 0.08, 2),
                round(rfix + 0.09, 2),
                round(rfix + 0.10,2)]
            return {
                'rHL24': round(rfix + 0.01, 2),
                'rHL25': round(rfix + 0.02, 2),
                'rHL26': round(rfix + 0.03, 2),
                'rHL27': round(rfix + 0.04, 2),
                'rHL28': round(rfix + 0.05, 2),
                'rHL29': round(rfix + 0.06, 2),
                'rHL30': round(rfix + 0.07, 2),
                'rHL31': round(rfix + 0.08, 2),
                'rHL32': round(rfix + 0.09, 2),
                'rHL33': round(rfix + 0.10, 2)
            }

    def before_next_page(self):
        self.participant.vars['final_rfix'] = Constants.rfix + \
                                             self.participant.vars['new_rfix'] + \
                                             self.participant.vars['new_rfix2'] + \
                                             self.participant.vars['new_rfix3']
        self.player.set_row2()
        self.player.set_payoff_HLr()


class Page_8(Page):

    def vars_for_template(self):
        ra1_value = self.participant.vars['final_rfix'][self.session.vars['rHL_row']-1]
        ra2_value = self.participant.vars['final_rfix'][self.session.vars['rHL_row2']-1]
        ra3_value = self.participant.vars['final_rfix'][self.session.vars['rHL_row3']-1]
        ra4_value = self.participant.vars['final_rfix'][self.session.vars['rHL_row4']-1]

        self.participant.vars['ra1_value'] = ra1_value
        self.participant.vars['ra2_value'] = ra2_value
        self.participant.vars['ra3_value'] = ra3_value
        self.participant.vars['ra4_value'] = ra4_value

        return {
            'payoff_HLr': self.player.participant.vars['payoff_HLr'],  # payoff
            'rrow': self.player.participant.vars['w_rrow'],  # randomly chosen row
            'rrow1': self.player.session.vars['rHL_row'],  # randomly chosen row
            'rrow2': self.player.session.vars['rHL_row2'],  # randomly chosen row
            'rrow3': self.player.session.vars['rHL_row3'],  # randomly chosen row
            'rrow4': self.player.session.vars['rHL_row4'],  # randomly chosen row
            'rvalue': self.session.vars['rHL_random'],  # randomly chosen value to define outcome
            'rchoice1': self.participant.vars['rchoices'][0],  # actual choice
            'rchoice2': self.participant.vars['rchoices'][1],
            'rchoice3': self.participant.vars['rchoices'][2],
            'rchoice4': self.participant.vars['rchoices'][3],
            'ra1_value': ra1_value,
            'ra2_value': ra2_value,
            'ra3_value': ra3_value,
            'ra4_value': ra4_value,

        }

page_sequence = [Page_0,
                 Page_1,
                 Page_2,
                 Page_3,
                 Page_4,
                 Page_5,
                 Page_6,
                 Page_7,
                 Page_8
]
