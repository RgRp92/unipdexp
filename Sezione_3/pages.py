from otree.api import Currency as c, currency_range
from ._builtin import Page, Page
from .models import Constants


class Page_0(Page):
    form_model = 'player'

class Page_1(Page):
    pass
class Page_2(Page):
    pass
class Page_3(Page):
    pass
class Page_4(Page):
    pass
class Page_5(Page):
    pass
class Page_6(Page):
    pass
class Page_6a(Page):
    pass
class Page_6b(Page):
    pass
class Page_7(Page):
    pass
class Page_8(Page):
    pass
class Page_9(Page):
    pass
class Page_10(Page):
    pass
class Page_11(Page):
    pass
class Page_12(Page):
    pass
class Page_13(Page):
    pass
class Page_14(Page):
    pass
class Page_15(Page):
    pass
class Page_16(Page):
    form_model = 'player'
    form_fields = ['HL_1']

    def vars_for_template(self):
        fix = Constants.fix

        return {
            'HL_1': fix[0],
        }

class Page_17(Page):
    form_model = 'player'
    form_fields = ['HL_2']

    def vars_for_template(self):
        if self.player.HL_1 == 1:
            self.participant.vars['new_fix']=[
                round(19 , 2),
                round(20 , 2),
                round(21 , 2),
                round(22, 2)]
            return {
                'HL10': 19 ,
                'HL11': 20 ,
                'HL12': 21 ,
                'HL13' :22
            }
        elif self.player.HL_1 == 2:
            fix = Constants.fix[0]
            self.participant.vars['new_fix']=[
                round(fix + 1, 2),
                round(fix + 2, 2),
                round(fix + 3, 2),
                round(fix + 4, 2)]
            return {
                'HL10': fix + 1,
                'HL11': fix + 2,
                'HL12': fix + 3,
                'HL13': fix + 4,

            }
        elif self.player.HL_1 == 3:
            fix = Constants.fix[1]
            self.participant.vars['new_fix'] = [
                round(fix + 1, 2),
                round(fix + 2, 2),
                round(fix + 3, 2),
                round(fix + 4, 2)]
            return {
                'HL10': fix + 1,
                'HL11': fix + 2,
                'HL12': fix + 3,
                'HL13': fix + 4,

            }
        elif self.player.HL_1 == 4:
            fix = Constants.fix[2]
            self.participant.vars['new_fix'] = [
                round(fix + 1, 2),
                round(fix + 2, 2),
                round(fix + 3, 2),
                round(fix + 4, 2)]
            return {
                'HL10': fix + 1,
                'HL11': fix + 2,
                'HL12': fix + 3,
                'HL13': fix + 4,

            }
        elif self.player.HL_1 == 5:
            fix = Constants.fix[3]
            self.participant.vars['new_fix'] = [
                round(fix + 1, 2),
                round(fix + 2, 2),
                round(fix + 3, 2),
                round(fix + 4, 2)]
            return {
                'HL10': fix + 1,
                'HL11': fix + 2,
                'HL12': fix + 3,
                'HL13': fix + 4,

            }
        elif self.player.HL_1 == 6:
            fix = Constants.fix[4]
            self.participant.vars['new_fix'] = [
                round(fix + 1, 2),
                round(fix + 2, 2),
                round(fix + 3, 2),
                round(fix + 4, 2)]
            return {
                'HL10': fix + 1,
                'HL11': fix + 2,
                'HL12': fix + 3,
                'HL13': fix + 4,
            }
        elif self.player.HL_1 == 7:
            fix = Constants.fix[5]
            self.participant.vars['new_fix'] = [
                round(fix + 1, 2),
                round(fix + 2, 2),
                round(fix + 3, 2),
                round(fix + 4, 2)]

            return {
                'HL10': fix + 1,
                'HL11': fix + 2,
                'HL12': fix + 3,
                'HL13': fix + 4,

            }
        elif self.player.HL_1 == 8:
            fix = Constants.fix[6]
            self.participant.vars['new_fix'] = [
                round(fix + 1, 2),
                round(fix + 2, 2),
                round(fix + 3, 2),
                round(fix + 4, 2)]

            return {
                'HL10': fix + 1,
                'HL11': fix + 2,
                'HL12': fix + 3,
                'HL13': fix + 4,

            }
        elif self.player.HL_1 == 9:
            fix = Constants.fix[7]
            self.participant.vars['new_fix'] = [
                round(fix + 1, 2),
                round(fix + 2, 2),
                round(fix + 3, 2),
                round(fix + 4, 2)]

            return {
                'HL10': fix + 1,
                'HL11': fix + 2,
                'HL12': fix + 3,
                'HL13': fix + 4,
            }

class Page_18(Page):
    form_model = 'player'
    form_fields = ['HL_3']

    def vars_for_template(self):
        if self.player.HL_2 == 10:
            fix = self.participant.vars['new_fix'][0]
            self.participant.vars['new_fix2']=[
            round(fix - 0.9,2),
            round(fix - 0.8,2),
            round(fix - 0.7,2),
            round(fix - 0.6,2),
            round(fix - 0.5,2),
            round(fix - 0.4,2),
            round(fix - 0.3,2),
            round(fix - 0.2,2),
            round(fix - 0.1,2),
            round(fix, 2),
            ]
            return {
                'HL14': round(fix - 0.9,2),
                'HL15': round(fix - 0.8,2),
                'HL16': round(fix - 0.7,2),
                'HL17': round(fix - 0.6,2),
                'HL18': round(fix - 0.5,2),
                'HL19': round(fix - 0.4,2),
                'HL20': round(fix - 0.3, 2),
                'HL21': round(fix - 0.2, 2),
                'HL22': round(fix - 0.1, 2),
                'HL23': round(fix ,2)}
        elif self.player.HL_2 == 11:
                fix = self.participant.vars['new_fix'][0]
                self.participant.vars['new_fix2'] = [
                    round(fix + 0.1, 2),
                    round(fix + 0.2, 2),
                    round(fix + 0.3, 2),
                    round(fix + 0.4, 2),
                    round(fix + 0.5, 2),
                    round(fix + 0.6, 2),
                    round(fix + 0.7, 2),
                    round(fix + 0.8, 2),
                    round(fix + 0.9, 2),
                    round(fix + 1, 2),
                ]
                return {
                    'HL14': round(fix + 0.1, 2),
                    'HL15': round(fix + 0.2, 2),
                    'HL16': round(fix + 0.3, 2),
                    'HL17': round(fix + 0.4, 2),
                    'HL18': round(fix + 0.5, 2),
                    'HL19': round(fix + 0.6, 2),
                    'HL20': round(fix + 0.7, 2),
                    'HL21': round(fix + 0.8, 2),
                    'HL22': round(fix + 0.9, 2),
                    'HL23': round(fix + 1, 2)}
        elif self.player.HL_2 == 12:
                fix = self.participant.vars['new_fix'][1]
                self.participant.vars['new_fix2'] = [
                    round(fix + 0.1, 2),
                    round(fix + 0.2, 2),
                    round(fix + 0.3, 2),
                    round(fix + 0.4, 2),
                    round(fix + 0.5, 2),
                    round(fix + 0.6, 2),
                    round(fix + 0.7, 2),
                    round(fix + 0.8, 2),
                    round(fix + 0.9, 2),
                    round(fix + 1, 2),
                ]
                return {
                    'HL14': round(fix + 0.1, 2),
                    'HL15': round(fix + 0.2, 2),
                    'HL16': round(fix + 0.3, 2),
                    'HL17': round(fix + 0.4, 2),
                    'HL18': round(fix + 0.5, 2),
                    'HL19': round(fix + 0.6, 2),
                    'HL20': round(fix + 0.7, 2),
                    'HL21': round(fix + 0.8, 2),
                    'HL22': round(fix + 0.9, 2),
                    'HL23': round(fix + 1, 2)}
        elif self.player.HL_2 == 13:
                fix = self.participant.vars['new_fix'][2]
                self.participant.vars['new_fix2'] = [
                    round(fix + 0.1, 2),
                    round(fix + 0.2, 2),
                    round(fix + 0.3, 2),
                    round(fix + 0.4, 2),
                    round(fix + 0.5, 2),
                    round(fix + 0.6, 2),
                    round(fix + 0.7, 2),
                    round(fix + 0.8, 2),
                    round(fix + 0.9, 2),
                    round(fix + 1, 2),
                ]
                return {
                    'HL14': round(fix + 0.1, 2),
                    'HL15': round(fix + 0.2, 2),
                    'HL16': round(fix + 0.3, 2),
                    'HL17': round(fix + 0.4, 2),
                    'HL18': round(fix + 0.5, 2),
                    'HL19': round(fix + 0.6, 2),
                    'HL20': round(fix + 0.7, 2),
                    'HL21': round(fix + 0.8, 2),
                    'HL22': round(fix + 0.9, 2),
                    'HL23': round(fix + 1, 2)}

class Page_19(Page):
    form_model = 'player'
    form_fields = ['HL_4']

    def vars_for_template(self):
        if self.player.HL_3 == 14:
            fix = self.participant.vars['new_fix2'][0]
            self.participant.vars['new_fix3'] = [
                round(fix - 0.09, 2),
                round(fix - 0.08, 2),
                round(fix - 0.07, 2),
                round(fix - 0.06, 2),
                round(fix - 0.05, 2),
                round(fix - 0.04, 2),
                round(fix - 0.03, 2),
                round(fix - 0.02, 2),
                round(fix - 0.01, 2),
                round(fix, 2),
            ]
            return {
                'HL24': round(fix - 0.09, 2),
                'HL25': round(fix - 0.08, 2),
                'HL26': round(fix - 0.07, 2),
                'HL27': round(fix - 0.06, 2),
                'HL28': round(fix - 0.05, 2),
                'HL29': round(fix - 0.04, 2),
                'HL30': round(fix - 0.03, 2),
                'HL31': round(fix - 0.02, 2),
                'HL32': round(fix - 0.01, 2),
                'HL33': round(fix , 2)
            }
        elif self.player.HL_3 == 15:
            fix = self.participant.vars['new_fix2'][0]
            self.participant.vars['new_fix3'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2),
                round(fix + 0.10, 2),
            ]
            return {
                'HL24': round(fix + 0.01, 2),
                'HL25': round(fix + 0.02, 2),
                'HL26': round(fix + 0.03, 2),
                'HL27': round(fix + 0.04, 2),
                'HL28': round(fix + 0.05, 2),
                'HL29': round(fix + 0.06, 2),
                'HL30': round(fix + 0.07, 2),
                'HL31': round(fix + 0.08, 2),
                'HL32': round(fix + 0.09, 2),
                'HL33': round(fix + 0.10, 2)
            }
        elif self.player.HL_3 == 16:
            fix = self.participant.vars['new_fix2'][1]
            self.participant.vars['new_fix3'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2),
                round(fix + 0.10, 2),
            ]
            return {
                'HL24': round(fix + 0.01, 2),
                'HL25': round(fix + 0.02, 2),
                'HL26': round(fix + 0.03, 2),
                'HL27': round(fix + 0.04, 2),
                'HL28': round(fix + 0.05, 2),
                'HL29': round(fix + 0.06, 2),
                'HL30': round(fix + 0.07, 2),
                'HL31': round(fix + 0.08, 2),
                'HL32': round(fix + 0.09, 2),
                'HL33': round(fix + 0.10, 2)
            }
        elif self.player.HL_3 == 17:
            fix = self.participant.vars['new_fix2'][2]
            self.participant.vars['new_fix3'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2),
                round(fix + 0.10, 2),
            ]
            return {
                'HL24': round(fix + 0.01, 2),
                'HL25': round(fix + 0.02, 2),
                'HL26': round(fix + 0.03, 2),
                'HL27': round(fix + 0.04, 2),
                'HL28': round(fix + 0.05, 2),
                'HL29': round(fix + 0.06, 2),
                'HL30': round(fix + 0.07, 2),
                'HL31': round(fix + 0.08, 2),
                'HL32': round(fix + 0.09, 2),
                'HL33': round(fix + 0.10, 2)
            }
        elif self.player.HL_3 == 18:
            fix = self.participant.vars['new_fix2'][3]
            self.participant.vars['new_fix3'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2),
                round(fix + 0.10, 2),
            ]
            return {
                'HL24': round(fix + 0.01, 2),
                'HL25': round(fix + 0.02, 2),
                'HL26': round(fix + 0.03, 2),
                'HL27': round(fix + 0.04, 2),
                'HL28': round(fix + 0.05, 2),
                'HL29': round(fix + 0.06, 2),
                'HL30': round(fix + 0.07, 2),
                'HL31': round(fix + 0.08, 2),
                'HL32': round(fix + 0.09, 2),
                'HL33': round(fix + 0.10, 2)
            }
        elif self.player.HL_3 == 19:
            fix = self.participant.vars['new_fix2'][4]
            self.participant.vars['new_fix3'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2),
                round(fix + 0.10, 2),
]
            return {
                'HL24': round(fix + 0.01, 2),
                'HL25': round(fix + 0.02, 2),
                'HL26': round(fix + 0.03, 2),
                'HL27': round(fix + 0.04, 2),
                'HL28': round(fix + 0.05, 2),
                'HL29': round(fix + 0.06, 2),
                'HL30': round(fix + 0.07, 2),
                'HL31': round(fix + 0.08, 2),
                'HL32': round(fix + 0.09, 2),
                'HL33': round(fix + 0.10, 2)
            }
        elif self.player.HL_3 == 20:
            fix = self.participant.vars['new_fix2'][5]
            self.participant.vars['new_fix3'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2),
                round(fix + 0.10, 2),
            ]
            return {
                'HL24': round(fix + 0.01, 2),
                'HL25': round(fix + 0.02, 2),
                'HL26': round(fix + 0.03, 2),
                'HL27': round(fix + 0.04, 2),
                'HL28': round(fix + 0.05, 2),
                'HL29': round(fix + 0.06, 2),
                'HL30': round(fix + 0.07, 2),
                'HL31': round(fix + 0.08, 2),
                'HL32': round(fix + 0.09, 2),
                'HL33': round(fix + 0.10, 2)
            }
        elif self.player.HL_3 == 21:
            fix = self.participant.vars['new_fix2'][6]
            self.participant.vars['new_fix3'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2),
                round(fix + 0.10, 2),
            ]
            return {
                'HL24': round(fix + 0.01, 2),
                'HL25': round(fix + 0.02, 2),
                'HL26': round(fix + 0.03, 2),
                'HL27': round(fix + 0.04, 2),
                'HL28': round(fix + 0.05, 2),
                'HL29': round(fix + 0.06, 2),
                'HL30': round(fix + 0.07, 2),
                'HL31': round(fix + 0.08, 2),
                'HL32': round(fix + 0.09, 2),
                'HL33': round(fix + 0.10, 2)
            }
        elif self.player.HL_3 == 22:
            fix = self.participant.vars['new_fix2'][7]
            self.participant.vars['new_fix3'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2),
                round(fix + 0.10, 2),
            ]
            return {
                'HL24': round(fix + 0.01, 2),
                'HL25': round(fix + 0.02, 2),
                'HL26': round(fix + 0.03, 2),
                'HL27': round(fix + 0.04, 2),
                'HL28': round(fix + 0.05, 2),
                'HL29': round(fix + 0.06, 2),
                'HL30': round(fix + 0.07, 2),
                'HL31': round(fix + 0.08, 2),
                'HL32': round(fix + 0.09, 2),
                'HL33': round(fix + 0.10, 2)
            }
        elif self.player.HL_3 == 23:
            fix = self.participant.vars['new_fix2'][8]
            self.participant.vars['new_fix3'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2),
                round(fix + 0.10,2)]
            return {
                'HL24': round(fix + 0.01, 2),
                'HL25': round(fix + 0.02, 2),
                'HL26': round(fix + 0.03, 2),
                'HL27': round(fix + 0.04, 2),
                'HL28': round(fix + 0.05, 2),
                'HL29': round(fix + 0.06, 2),
                'HL30': round(fix + 0.07, 2),
                'HL31': round(fix + 0.08, 2),
                'HL32': round(fix + 0.09, 2),
                'HL33': round(fix + 0.10, 2)
            }

    def before_next_page(self):
        self.participant.vars['final_fix'] = Constants.fix + \
                                             self.participant.vars['new_fix'] + \
                                             self.participant.vars['new_fix2'] + \
                                             self.participant.vars['new_fix3']
        self.player.set_row()
        self.player.set_payoff_HL()

class Page_20(Page):

    def vars_for_template(self):
       a1_value = self.participant.vars['final_fix'][self.session.vars['HL_row']-1]
       a2_value = self.participant.vars['final_fix'][self.session.vars['HL_row2']-1]
       a3_value = self.participant.vars['final_fix'][self.session.vars['HL_row3']-1]
       a4_value = self.participant.vars['final_fix'][self.session.vars['HL_row4']-1]

       self.participant.vars['a1_value'] = a1_value
       self.participant.vars['a2_value'] = a2_value
       self.participant.vars['a3_value'] = a3_value
       self.participant.vars['a4_value'] = a4_value


       return{
            'payoff_HL': self.player.participant.vars['payoff_HL'],#payoff
            'row': self.player.participant.vars['w_row'],  # randomly chosen row
            'row1': self.player.session.vars['HL_row'], # randomly chosen row
            'row2': self.player.session.vars['HL_row2'],  # randomly chosen row
            'row3': self.player.session.vars['HL_row3'],  # randomly chosen row
            'row4': self.player.session.vars['HL_row4'],  # randomly chosen row
            'value': self.session.vars['HL_random'],# randomly chosen value to define outcome
            'choice1': self.participant.vars['choices'][0],# actual choice
            'choice2': self.participant.vars['choices'][1],
            'choice3': self.participant.vars['choices'][2],
            'choice4': self.participant.vars['choices'][3],
            'a1_value': a1_value,
            'a2_value': a2_value,
            'a3_value': a3_value,
            'a4_value': a4_value,

       }



page_sequence = [Page_0,
                 Page_1,
                 Page_2,
                 Page_3,
                 Page_4,
                 Page_5,
                 Page_6,
                 Page_6a,
                 Page_6b,
                 Page_7,
                 Page_8,
                 Page_9,
                 Page_10,
                 Page_11,
                 Page_12,
                 Page_13,
                 Page_14,
                 Page_15,
                 Page_16,
                 Page_17,
                 Page_18,
                 Page_19,
                 Page_20,
                 ]
