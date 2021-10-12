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
class Page_4a(Page):
    form_model = 'player'

    def vars_for_template(self):
        rHL_1 = self.player.rHL_1

        return {'rHL_1': rHL_1}

class Page_5(Page):
    form_model = 'player'
    form_fields = ['rHL_2']

    def vars_for_template(self):
        if self.player.rHL_1 == 1:
            self.participant.vars['new_rfix']=[
                round(18 , 2),
                round(19 , 2),
                round(20 , 2),
                round(21 , 2),
                round(22 , 2)]
            return {
                'rHL11': 18 ,
                'rHL12': 19 ,
                'rHL13': 20 ,
                'rHL14': 21 ,
                'rHL15': 22 ,
            }
        elif self.player.rHL_1 == 2:
            rfix = Constants.rfix[0]
            self.participant.vars['new_rfix']=[
                round(rfix , 2),
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL11': rfix ,
                'rHL12': rfix + 1,
                'rHL13': rfix + 2,
                'rHL14': rfix + 3,
                'rHL15': rfix + 4,
            }
        elif self.player.rHL_1 == 3:
            rfix = Constants.rfix[1]
            self.participant.vars['new_rfix'] = [
                round(rfix, 2),
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL11': rfix,
                'rHL12': rfix + 1,
                'rHL13': rfix + 2,
                'rHL14': rfix + 3,
                'rHL15': rfix + 4,
            }
        elif self.player.rHL_1 == 4:
            rfix = Constants.rfix[2]
            self.participant.vars['new_rfix'] = [
                round(rfix, 2),
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL11': rfix,
                'rHL12': rfix + 1,
                'rHL13': rfix + 2,
                'rHL14': rfix + 3,
                'rHL15': rfix + 4,
            }
        elif self.player.rHL_1 == 5:
            rfix = Constants.rfix[3]
            self.participant.vars['new_rfix'] = [
                round(rfix, 2),
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL11': rfix,
                'rHL12': rfix + 1,
                'rHL13': rfix + 2,
                'rHL14': rfix + 3,
                'rHL15': rfix + 4,
            }
        elif self.player.rHL_1 == 6:
            rfix = Constants.rfix[4]
            self.participant.vars['new_rfix'] = [
                round(rfix, 2),
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL11': rfix,
                'rHL12': rfix + 1,
                'rHL13': rfix + 2,
                'rHL14': rfix + 3,
                'rHL15': rfix + 4,
            }
        elif self.player.rHL_1 == 7:
            rfix = Constants.rfix[5]
            self.participant.vars['new_rfix'] = [
                round(rfix, 2),
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL11': rfix,
                'rHL12': rfix + 1,
                'rHL13': rfix + 2,
                'rHL14': rfix + 3,
                'rHL15': rfix + 4,
            }
        elif self.player.rHL_1 == 8:
            rfix = Constants.rfix[6]
            self.participant.vars['new_rfix'] = [
                round(rfix, 2),
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL11': rfix,
                'rHL12': rfix + 1,
                'rHL13': rfix + 2,
                'rHL14': rfix + 3,
                'rHL15': rfix + 4,
            }
        elif self.player.rHL_1 == 9:
            rfix = Constants.rfix[7]
            self.participant.vars['new_rfix'] = [
                round(rfix, 2),
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL11': rfix,
                'rHL12': rfix + 1,
                'rHL13': rfix + 2,
                'rHL14': rfix + 3,
                'rHL15': rfix + 4,
            }
        elif self.player.rHL_1 == 10:
            rfix = Constants.rfix[8]
            self.participant.vars['new_rfix'] = [
                round(rfix, 2),
                round(rfix + 1, 2),
                round(rfix + 2, 2),
                round(rfix + 3, 2),
                round(rfix + 4, 2)]
            return {
                'rHL11': rfix,
                'rHL12': rfix + 1,
                'rHL13': rfix + 2,
                'rHL14': rfix + 3,
                'rHL15': rfix + 4,
            }
class Page_5a(Page):
    form_model = 'player'

    def vars_for_template(self):
        rHL_2 = self.player.rHL_2
        rHL11 = self.participant.vars['new_rfix'][0]
        rHL12 = self.participant.vars['new_rfix'][1]
        rHL13 = self.participant.vars['new_rfix'][2]
        rHL14 = self.participant.vars['new_rfix'][3]
        rHL15 = self.participant.vars['new_rfix'][4]

        return {'rHL_2': rHL_2,
                'rHL11': rHL11,
                'rHL12': rHL12,
                'rHL13': rHL13,
                'rHL14': rHL14,
                'rHL15': rHL15,
                }


class Page_6(Page):
    form_model = 'player'
    form_fields = ['rHL_3']

    def vars_for_template(self):
        if self.player.rHL_2 == 11:
            rfix = self.participant.vars['new_rfix'][0]
            self.participant.vars['new_rfix2'] = [
                round(rfix - 0.9, 2),
                round(rfix - 0.8, 2),
                round(rfix - 0.7, 2),
                round(rfix - 0.6, 2),
                round(rfix - 0.5, 2),
                round(rfix - 0.4, 2),
                round(rfix - 0.3, 2),
                round(rfix - 0.2, 2),
                round(rfix - 0.1, 2)]
            return {
                'rHL17': round(rfix - 0.9, 2),
                'rHL18': round(rfix - 0.8, 2),
                'rHL19': round(rfix - 0.7, 2),
                'rHL20': round(rfix - 0.6, 2),
                'rHL21': round(rfix - 0.5, 2),
                'rHL22': round(rfix - 0.4, 2),
                'rHL23': round(rfix - 0.3, 2),
                'rHL24': round(rfix - 0.2, 2),
                'rHL25': round(rfix - 0.1, 2),

            }
        elif self.player.rHL_2 == 12:
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
                round(rfix + 0.9, 2)]
            return {
                'rHL17': round(rfix + 0.1, 2),
                'rHL18': round(rfix + 0.2, 2),
                'rHL19': round(rfix + 0.3, 2),
                'rHL20': round(rfix + 0.4, 2),
                'rHL21': round(rfix + 0.5, 2),
                'rHL22': round(rfix + 0.6, 2),
                'rHL23': round(rfix + 0.7, 2),
                'rHL24': round(rfix + 0.8, 2),
                'rHL25': round(rfix + 0.9, 2),
            }
        elif self.player.rHL_2 == 13:
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
                round(rfix + 0.9, 2)]
            return {
                'rHL17': round(rfix + 0.1, 2),
                'rHL18': round(rfix + 0.2, 2),
                'rHL19': round(rfix + 0.3, 2),
                'rHL20': round(rfix + 0.4, 2),
                'rHL21': round(rfix + 0.5, 2),
                'rHL22': round(rfix + 0.6, 2),
                'rHL23': round(rfix + 0.7, 2),
                'rHL24': round(rfix + 0.8, 2),
                'rHL25': round(rfix + 0.9, 2),
            }
        elif self.player.rHL_2 == 14:
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
                round(rfix + 0.9, 2)]
            return {
                'rHL17': round(rfix + 0.1, 2),
                'rHL18': round(rfix + 0.2, 2),
                'rHL19': round(rfix + 0.3, 2),
                'rHL20': round(rfix + 0.4, 2),
                'rHL21': round(rfix + 0.5, 2),
                'rHL22': round(rfix + 0.6, 2),
                'rHL23': round(rfix + 0.7, 2),
                'rHL24': round(rfix + 0.8, 2),
                'rHL25': round(rfix + 0.9, 2),

            }
        elif self.player.rHL_2 == 15:
            rfix = self.participant.vars['new_rfix'][3]
            self.participant.vars['new_rfix2'] = [
                round(rfix + 0.1, 2),
                round(rfix + 0.2, 2),
                round(rfix + 0.3, 2),
                round(rfix + 0.4, 2),
                round(rfix + 0.5, 2),
                round(rfix + 0.6, 2),
                round(rfix + 0.7, 2),
                round(rfix + 0.8, 2),
                round(rfix + 0.9, 2)]
            return {
                'rHL17': round(rfix + 0.1, 2),
                'rHL18': round(rfix + 0.2, 2),
                'rHL19': round(rfix + 0.3, 2),
                'rHL20': round(rfix + 0.4, 2),
                'rHL21': round(rfix + 0.5, 2),
                'rHL22': round(rfix + 0.6, 2),
                'rHL23': round(rfix + 0.7, 2),
                'rHL24': round(rfix + 0.8, 2),
                'rHL25': round(rfix + 0.9, 2),

            }
        elif self.player.rHL_2 == 16:
            rfix = self.participant.vars['new_rfix'][4]
            self.participant.vars['new_rfix2'] = [
                round(rfix + 0.1, 2),
                round(rfix + 0.2, 2),
                round(rfix + 0.3, 2),
                round(rfix + 0.4, 2),
                round(rfix + 0.5, 2),
                round(rfix + 0.6, 2),
                round(rfix + 0.7, 2),
                round(rfix + 0.8, 2),
                round(rfix + 0.9, 2)]
            return {
                'rHL17': round(rfix + 0.1, 2),
                'rHL18': round(rfix + 0.2, 2),
                'rHL19': round(rfix + 0.3, 2),
                'rHL20': round(rfix + 0.4, 2),
                'rHL21': round(rfix + 0.5, 2),
                'rHL22': round(rfix + 0.6, 2),
                'rHL23': round(rfix + 0.7, 2),
                'rHL24': round(rfix + 0.8, 2),
                'rHL25': round(rfix + 0.9, 2),

            }

class Page_6a(Page):
    form_model = 'player'

    def vars_for_template(self):
        rHL_3 = self.player.rHL_3
        rHL17 = self.participant.vars['new_rfix2'][0]
        rHL18 = self.participant.vars['new_rfix2'][1]
        rHL19 = self.participant.vars['new_rfix2'][2]
        rHL20 = self.participant.vars['new_rfix2'][3]
        rHL21 = self.participant.vars['new_rfix2'][4]
        rHL22 = self.participant.vars['new_rfix2'][5]
        rHL23 = self.participant.vars['new_rfix2'][6]
        rHL24 = self.participant.vars['new_rfix2'][7]
        rHL25 = self.participant.vars['new_rfix2'][8]

        return {'rHL_3': rHL_3,
                'rHL17': rHL17,
                'rHL18': rHL18,
                'rHL19': rHL19,
                'rHL20': rHL20,
                'rHL21': rHL21,
                'rHL22': rHL22,
                'rHL23': rHL23,
                'rHL24': rHL24,
                'rHL25': rHL25,

                }


class Page_7(Page):
    form_model = 'player'
    form_fields = ['rHL_4']

    def vars_for_template(self):
        if self.player.rHL_3 == 17:
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
                round(rfix - 0.01, 2)]
            return {
                'rHL27': round(rfix - 0.09, 2),
                'rHL28': round(rfix - 0.08, 2),
                'rHL29': round(rfix - 0.07, 2),
                'rHL30': round(rfix - 0.06, 2),
                'rHL31': round(rfix - 0.05, 2),
                'rHL32': round(rfix - 0.04, 2),
                'rHL33': round(rfix - 0.03, 2),
                'rHL34': round(rfix - 0.02, 2),
                'rHL35': round(rfix - 0.01, 2),

            }
        elif self.player.rHL_3 == 18:
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
                round(rfix + 0.09, 2)]
            return {
                'rHL27': round(rfix + 0.01, 2),
                'rHL28': round(rfix + 0.02, 2),
                'rHL29': round(rfix + 0.03, 2),
                'rHL30': round(rfix + 0.04, 2),
                'rHL31': round(rfix + 0.05, 2),
                'rHL32': round(rfix + 0.06, 2),
                'rHL33': round(rfix + 0.07, 2),
                'rHL34': round(rfix + 0.08, 2),
                'rHL35': round(rfix + 0.09, 2),

            }
        elif self.player.rHL_3 == 19:
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
                round(rfix + 0.09, 2)]
            return {
                'rHL27': round(rfix + 0.01, 2),
                'rHL28': round(rfix + 0.02, 2),
                'rHL29': round(rfix + 0.03, 2),
                'rHL30': round(rfix + 0.04, 2),
                'rHL31': round(rfix + 0.05, 2),
                'rHL32': round(rfix + 0.06, 2),
                'rHL33': round(rfix + 0.07, 2),
                'rHL34': round(rfix + 0.08, 2),
                'rHL35': round(rfix + 0.09, 2),

            }
        elif self.player.rHL_3 == 20:
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
                round(rfix + 0.09, 2)]
            return {
                'rHL27': round(rfix + 0.01, 2),
                'rHL28': round(rfix + 0.02, 2),
                'rHL29': round(rfix + 0.03, 2),
                'rHL30': round(rfix + 0.04, 2),
                'rHL31': round(rfix + 0.05, 2),
                'rHL32': round(rfix + 0.06, 2),
                'rHL33': round(rfix + 0.07, 2),
                'rHL34': round(rfix + 0.08, 2),
                'rHL35': round(rfix + 0.09, 2),

            }
        elif self.player.rHL_3 == 21:
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
                round(rfix + 0.09, 2)]
            return {
                'rHL27': round(rfix + 0.01, 2),
                'rHL28': round(rfix + 0.02, 2),
                'rHL29': round(rfix + 0.03, 2),
                'rHL30': round(rfix + 0.04, 2),
                'rHL31': round(rfix + 0.05, 2),
                'rHL32': round(rfix + 0.06, 2),
                'rHL33': round(rfix + 0.07, 2),
                'rHL34': round(rfix + 0.08, 2),
                'rHL35': round(rfix + 0.09, 2),

            }
        elif self.player.rHL_3 == 22:
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
                round(rfix + 0.09, 2)]
            return {
                'rHL27': round(rfix + 0.01, 2),
                'rHL28': round(rfix + 0.02, 2),
                'rHL29': round(rfix + 0.03, 2),
                'rHL30': round(rfix + 0.04, 2),
                'rHL31': round(rfix + 0.05, 2),
                'rHL32': round(rfix + 0.06, 2),
                'rHL33': round(rfix + 0.07, 2),
                'rHL34': round(rfix + 0.08, 2),
                'rHL35': round(rfix + 0.09, 2),

            }
        elif self.player.rHL_3 == 23:
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
                round(rfix + 0.09, 2)]
           return {
                'rHL27': round(rfix + 0.01, 2),
                'rHL28': round(rfix + 0.02, 2),
                'rHL29': round(rfix + 0.03, 2),
                'rHL30': round(rfix + 0.04, 2),
                'rHL31': round(rfix + 0.05, 2),
                'rHL32': round(rfix + 0.06, 2),
                'rHL33': round(rfix + 0.07, 2),
                'rHL34': round(rfix + 0.08, 2),
                'rHL35': round(rfix + 0.09, 2),
            }
        elif self.player.rHL_3 == 24:
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
                round(rfix + 0.09, 2)]
            return {
                'rHL27': round(rfix + 0.01, 2),
                'rHL28': round(rfix + 0.02, 2),
                'rHL29': round(rfix + 0.03, 2),
                'rHL30': round(rfix + 0.04, 2),
                'rHL31': round(rfix + 0.05, 2),
                'rHL32': round(rfix + 0.06, 2),
                'rHL33': round(rfix + 0.07, 2),
                'rHL34': round(rfix + 0.08, 2),
                'rHL35': round(rfix + 0.09, 2),
            }
        elif self.player.rHL_3 == 25:
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
                round(rfix + 0.09, 2)]
            return {
                'rHL27': round(rfix + 0.01, 2),
                'rHL28': round(rfix + 0.02, 2),
                'rHL29': round(rfix + 0.03, 2),
                'rHL30': round(rfix + 0.04, 2),
                'rHL31': round(rfix + 0.05, 2),
                'rHL32': round(rfix + 0.06, 2),
                'rHL33': round(rfix + 0.07, 2),
                'rHL34': round(rfix + 0.08, 2),
                'rHL35': round(rfix + 0.09, 2),

            }
        elif self.player.rHL_3 == 26:
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
                round(rfix + 0.09, 2)]
            return {
                'rHL27': round(rfix + 0.01, 2),
                'rHL28': round(rfix + 0.02, 2),
                'rHL29': round(rfix + 0.03, 2),
                'rHL30': round(rfix + 0.04, 2),
                'rHL31': round(rfix + 0.05, 2),
                'rHL32': round(rfix + 0.06, 2),
                'rHL33': round(rfix + 0.07, 2),
                'rHL34': round(rfix + 0.08, 2),
                'rHL35': round(rfix + 0.09, 2),

            }

class Page_7a(Page):
    form_model = 'player'

    def vars_for_template(self):
        rHL_4 = self.player.rHL_4
        rHL27 = self.participant.vars['new_rfix3'][0]
        rHL28 = self.participant.vars['new_rfix3'][1]
        rHL29 = self.participant.vars['new_rfix3'][2]
        rHL30 = self.participant.vars['new_rfix3'][3]
        rHL31 = self.participant.vars['new_rfix3'][4]
        rHL32 = self.participant.vars['new_rfix3'][5]
        rHL33 = self.participant.vars['new_rfix3'][6]
        rHL34 = self.participant.vars['new_rfix3'][7]
        rHL35 = self.participant.vars['new_rfix3'][8]

        return {'rHL_4': rHL_4,
                'rHL27': rHL27,
                'rHL28': rHL28,
                'rHL29': rHL29,
                'rHL30': rHL30,
                'rHL31': rHL31,
                'rHL32': rHL32,
                'rHL33': rHL33,
                'rHL34': rHL34,
                'rHL35': rHL35,
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
        ra2_value = self.participant.vars['final_rfix'][self.session.vars['rHL_row2']-2]
        ra3_value = self.participant.vars['final_rfix'][self.session.vars['rHL_row3']-3]
        ra4_value = self.participant.vars['final_rfix'][self.session.vars['rHL_row4']-4]

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
                 Page_4a,
                 Page_5,
                 Page_5a,
                 Page_6,
                 Page_6a,
                 Page_7,
                 Page_7a,
                 Page_8
]
