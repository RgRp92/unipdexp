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
    pass

class Page_17(Page):
    form_model = 'player'
    form_fields = ['HL_1', 'HL_2', 'HL_3', 'HL_4', 'HL_5', 'HL_6', 'HL_7','HL_8','HL_9','HL_10','HL_11','HL_12']

    def vars_for_template(self):
        fix = Constants.fix

        return {
            'HL1': fix[0],
            'HL2': fix[1],
            'HL3': fix[2],
            'HL4': fix[3],
            'HL5': fix[4],
            'HL6': fix[5],
            'HL7': fix[6],
            'HL8': fix[7],
            'HL9': fix[8],
            'HL10': fix[9],
            'HL11': fix[10],
            'HL12': fix[11],

        }



class Page_18(Page):
    form_model = 'player'
    form_fields = ['HL_13', 'HL_14', 'HL_15', 'HL_16', 'HL_17', 'HL_18', 'HL_19','HL_20','HL_21']

    def vars_for_template(self):
        if self.player.HL_1 == 1:
            self.participant.vars['new_fix']=[
                round(21.10 , 2),
                round(21.20, 2),
                round(21.30, 2),
                round(21.40, 2),
                round(21.50, 2),
                round(21.60, 2),
                round(21.70, 2),
                round(21.80, 2),
                round(21.90, 2)]
            return {
                'HL13': 21.10,
                'HL14': 21.20,
                'HL15': 21.30,
                'HL16': 21.40,
                'HL17': 21.50,
                'HL18': 21.60,
                'HL19': 21.70,
                'HL20': 21.80,
                'HL21': 21.90,
            }
        elif self.player.HL_2 == 1:
            fix = Constants.fix[0]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_3 == 1:
            fix = Constants.fix[1]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_4 == 1:
            fix = Constants.fix[2]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_5 == 1:
            fix = Constants.fix[3]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_6 == 1:
            fix = Constants.fix[4]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_7 == 1:
            fix = Constants.fix[5]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_8 == 1:
            fix = Constants.fix[6]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_9 == 1:
            fix = Constants.fix[7]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_10 == 1:
            fix = Constants.fix[8]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_11 == 1:
            fix = Constants.fix[9]
            self.participant.vars['new_fix']=[
                round(fix + 0.10, 2),
                round(fix + 0.20, 2),
                round(fix + 0.30, 2),
                round(fix + 0.40, 2),
                round(fix + 0.50, 2),
                round(fix + 0.60, 2),
                round(fix + 0.70, 2),
                round(fix + 0.80, 2),
                round(fix + 0.90, 2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_12 == 1:
            fix = Constants.fix[10]
            self.participant.vars['new_fix']=[
                                              round(fix + 0.10,2),
                                              round(fix + 0.20,2),
                                              round(fix + 0.30,2),
                                              round(fix + 0.40,2),
                                              round(fix + 0.50,2),
                                              round(fix + 0.60,2),
                                              round(fix + 0.70,2),
                                              round(fix + 0.80,2),
                                              round(fix + 0.90,2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }
        elif self.player.HL_12 == 2:
            fix = Constants.fix[11]
            self.participant.vars['new_fix']=[
                                              round(fix + 0.10,2),
                                              round(fix + 0.20,2),
                                              round(fix + 0.30,2),
                                              round(fix + 0.40,2),
                                              round(fix + 0.50,2),
                                              round(fix + 0.60,2),
                                              round(fix + 0.70,2),
                                              round(fix + 0.80,2),
                                              round(fix + 0.90,2)]
            return {
                'HL13': fix + 0.10,
                'HL14': fix + 0.20,
                'HL15': fix + 0.30,
                'HL16': fix + 0.40,
                'HL17': fix + 0.50,
                'HL18': fix + 0.60,
                'HL19': fix + 0.70,
                'HL20': fix + 0.80,
                'HL21': fix + 0.90,
            }

class Page_19(Page):
    form_model = 'player'
    form_fields = ['HL_22', 'HL_23', 'HL_24', 'HL_25', 'HL_26', 'HL_27', 'HL_28', 'HL_29', 'HL_30']

    def vars_for_template(self):
        if self.player.HL_13 == 1:
            fix = self.participant.vars['new_fix'][0]
            self.participant.vars['new_fix2']=[
                                              round(fix - 0.09,2),
                                              round(fix - 0.08,2),
                                              round(fix - 0.07,2),
                                              round(fix - 0.06,2),
                                              round(fix - 0.05,2),
                                              round(fix - 0.04,2),
                                              round(fix - 0.03,2),
                                              round(fix - 0.02,2),
                                              round(fix - 0.01,2)]
            return {
                'HL22': round(fix - 0.09,2),
                'HL23': round(fix - 0.08,2),
                'HL24': round(fix - 0.07,2),
                'HL25': round(fix - 0.06,2),
                'HL26': round(fix - 0.05,2),
                'HL27': round(fix - 0.04,2),
                'HL28': round(fix - 0.03,2),
                'HL29': round(fix - 0.02,2),
                'HL30': round(fix - 0.01,2),
            }
        elif self.player.HL_14 == 1:
            fix = self.participant.vars['new_fix'][0]
            self.participant.vars['new_fix2'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2)]
            return {
                'HL22': round(fix + 0.01,2),
                'HL23': round(fix + 0.02,2),
                'HL24': round(fix + 0.03,2),
                'HL25': round(fix + 0.04,2),
                'HL26': round(fix + 0.05,2),
                'HL27': round(fix + 0.06,2),
                'HL28': round(fix + 0.07,2),
                'HL29': round(fix + 0.08,2),
                'HL30': round(fix + 0.09,2),
            }
        elif self.player.HL_15 == 1:
            fix = self.participant.vars['new_fix'][1]
            self.participant.vars['new_fix2'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2)]
            return {
                'HL22': round(fix + 0.01,2),
                'HL23': round(fix + 0.02,2),
                'HL24': round(fix + 0.03,2),
                'HL25': round(fix + 0.04,2),
                'HL26': round(fix + 0.05,2),
                'HL27': round(fix + 0.06,2),
                'HL28': round(fix + 0.07,2),
                'HL29': round(fix + 0.08,2),
                'HL30': round(fix + 0.09,2),
            }
        elif self.player.HL_16 == 1:
            fix = self.participant.vars['new_fix'][2]
            self.participant.vars['new_fix2'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2)]
            return {
                'HL22': round(fix + 0.01,2),
                'HL23': round(fix + 0.02,2),
                'HL24': round(fix + 0.03,2),
                'HL25': round(fix + 0.04,2),
                'HL26': round(fix + 0.05,2),
                'HL27': round(fix + 0.06,2),
                'HL28': round(fix + 0.07,2),
                'HL29': round(fix + 0.08,2),
                'HL30': round(fix + 0.09,2),
            }
        elif self.player.HL_17 == 1:
            fix = self.participant.vars['new_fix'][3]
            self.participant.vars['new_fix2'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2)]
            return {
                'HL22': round(fix + 0.01,2),
                'HL23': round(fix + 0.02,2),
                'HL24': round(fix + 0.03,2),
                'HL25': round(fix + 0.04,2),
                'HL26': round(fix + 0.05,2),
                'HL27': round(fix + 0.06,2),
                'HL28': round(fix + 0.07,2),
                'HL29': round(fix + 0.08,2),
                'HL30': round(fix + 0.09,2),
            }
        elif self.player.HL_18 == 1:
            fix = self.participant.vars['new_fix'][4]
            self.participant.vars['new_fix2'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2)]
            return {
                'HL22': round(fix + 0.01,2),
                'HL23': round(fix + 0.02,2),
                'HL24': round(fix + 0.03,2),
                'HL25': round(fix + 0.04,2),
                'HL26': round(fix + 0.05,2),
                'HL27': round(fix + 0.06,2),
                'HL28': round(fix + 0.07,2),
                'HL29': round(fix + 0.08,2),
                'HL30': round(fix + 0.09,2),
            }
        elif self.player.HL_19 == 1:
            fix = self.participant.vars['new_fix'][5]
            self.participant.vars['new_fix2'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2)]
            return {
                'HL22': round(fix + 0.01,2),
                'HL23': round(fix + 0.02,2),
                'HL24': round(fix + 0.03,2),
                'HL25': round(fix + 0.04,2),
                'HL26': round(fix + 0.05,2),
                'HL27': round(fix + 0.06,2),
                'HL28': round(fix + 0.07,2),
                'HL29': round(fix + 0.08,2),
                'HL30': round(fix + 0.09,2),
            }
        elif self.player.HL_20 == 1:
            fix = self.participant.vars['new_fix'][6]
            self.participant.vars['new_fix2'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2)]
            return {
                'HL22': round(fix + 0.01,2),
                'HL23': round(fix + 0.02,2),
                'HL24': round(fix + 0.03,2),
                'HL25': round(fix + 0.04,2),
                'HL26': round(fix + 0.05,2),
                'HL27': round(fix + 0.06,2),
                'HL28': round(fix + 0.07,2),
                'HL29': round(fix + 0.08,2),
                'HL30': round(fix + 0.09,2),
            }
        elif self.player.HL_21 == 1:
            fix = self.participant.vars['new_fix'][7]
            self.participant.vars['new_fix2'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2)]
            return {
                'HL22': round(fix + 0.01,2),
                'HL23': round(fix + 0.02,2),
                'HL24': round(fix + 0.03,2),
                'HL25': round(fix + 0.04,2),
                'HL26': round(fix + 0.05,2),
                'HL27': round(fix + 0.06,2),
                'HL28': round(fix + 0.07,2),
                'HL29': round(fix + 0.08,2),
                'HL30': round(fix + 0.09,2),
            }
        elif self.player.HL_21 == 2:
            fix = self.participant.vars['new_fix'][8]
            self.participant.vars['new_fix2'] = [
                round(fix + 0.01, 2),
                round(fix + 0.02, 2),
                round(fix + 0.03, 2),
                round(fix + 0.04, 2),
                round(fix + 0.05, 2),
                round(fix + 0.06, 2),
                round(fix + 0.07, 2),
                round(fix + 0.08, 2),
                round(fix + 0.09, 2)]
            return {
                'HL22': round(fix + 0.01,2),
                'HL23': round(fix + 0.02,2),
                'HL24': round(fix + 0.03,2),
                'HL25': round(fix + 0.04,2),
                'HL26': round(fix + 0.05,2),
                'HL27': round(fix + 0.06,2),
                'HL28': round(fix + 0.07,2),
                'HL29': round(fix + 0.08,2),
                'HL30': round(fix + 0.09,2),
            }

    def before_next_page(self):
        self.participant.vars['final_fix'] = Constants.fix + self.participant.vars['new_fix'] + self.participant.vars['new_fix2']
        self.player.set_payoff_HL()


class Page_20(Page):

    def vars_for_template(self):
       a1_value = self.participant.vars['final_fix'][self.session.vars['HL_row'] - 1]
       self.participant.vars['a1_value'] = a1_value

       return{
            'payoff_HL': self.player.participant.vars['payoff_HL'],#payoff
            'row': self.player.session.vars['HL_row'], # randomly chosen row
            'value': self.session.vars['HL_random'],# randomly chosen value to define outcome
            'value2': self.session.vars['HL_scenario'],
            'choice': self.participant.vars['choices'],# actual choice
            'a1_value': a1_value,
            'p_A_1': self.session.vars['HL_row'],
            'p_A_2': 10-self.session.vars['HL_row'],
            'p_B_1': self.session.vars['HL_row'],
            'p_B_2': 10-self.session.vars['HL_row'],
            }



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
                 Page_12,
                 Page_13,
                 Page_14,
                 Page_15,
                 Page_16,
                 Page_17,
                 Page_18,
                 Page_19,
                 Page_20]
