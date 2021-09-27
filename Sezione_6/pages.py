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
    form_fields = ['rHL_1', 'rHL_2', 'rHL_3', 'rHL_4', 'rHL_5', 'rHL_6',
                   'rHL_7','rHL_8','rHL_9','rHL_10','rHL_11','rHL_12']

    def vars_for_template(self):
        rfix = Constants.rfix

        return {
            'rHL1': rfix[0],
            'rHL2': rfix[1],
            'rHL3': rfix[2],
            'rHL4': rfix[3],
            'rHL5': rfix[4],
            'rHL6': rfix[5],
            'rHL7': rfix[6],
            'rHL8': rfix[7],
            'rHL9': rfix[8],
            'rHL10': rfix[9],
            'rHL11': rfix[10],
            'rHL12': rfix[11],

        }

class Page_5(Page):
    form_model = 'player'
    form_fields = ['rHL_13', 'rHL_14', 'rHL_15', 'rHL_16', 'rHL_17', 'rHL_18', 'rHL_19','rHL_20','rHL_21']

    def vars_for_template(self):
        if self.player.rHL_1 == 1:
            self.participant.vars['new_rfix']=[
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
                'rHL13': 21.10,
                'rHL14': 21.20,
                'rHL15': 21.30,
                'rHL16': 21.40,
                'rHL17': 21.50,
                'rHL18': 21.60,
                'rHL19': 21.70,
                'rHL20': 21.80,
                'rHL21': 21.90,
            }
        elif self.player.rHL_2 == 1:
            rfix = Constants.rfix[0]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_3 == 1:
            rfix = Constants.rfix[1]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_4 == 1:
            rfix = Constants.rfix[2]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_5 == 1:
            rfix = Constants.rfix[3]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_6 == 1:
            rfix = Constants.rfix[4]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_7 == 1:
            rfix = Constants.rfix[5]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_8 == 1:
            rfix = Constants.rfix[6]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_9 == 1:
            rfix = Constants.rfix[7]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_10 == 1:
            rfix = Constants.rfix[8]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_11 == 1:
            rfix = Constants.rfix[9]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_12 == 1:
            rfix = Constants.rfix[10]
            self.participant.vars['new_rfix']=[
                round(rfix + 0.10, 2),
                round(rfix + 0.20, 2),
                round(rfix + 0.30, 2),
                round(rfix + 0.40, 2),
                round(rfix + 0.50, 2),
                round(rfix + 0.60, 2),
                round(rfix + 0.70, 2),
                round(rfix + 0.80, 2),
                round(rfix + 0.90, 2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
        elif self.player.rHL_12 == 2:
            rfix = Constants.rfix[11]
            self.participant.vars['new_rfix']=[
                                              round(rfix + 0.10,2),
                                              round(rfix + 0.20,2),
                                              round(rfix + 0.30,2),
                                              round(rfix + 0.40,2),
                                              round(rfix + 0.50,2),
                                              round(rfix + 0.60,2),
                                              round(rfix + 0.70,2),
                                              round(rfix + 0.80,2),
                                              round(rfix + 0.90,2)]
            return {
                'rHL13': rfix + 0.10,
                'rHL14': rfix + 0.20,
                'rHL15': rfix + 0.30,
                'rHL16': rfix + 0.40,
                'rHL17': rfix + 0.50,
                'rHL18': rfix + 0.60,
                'rHL19': rfix + 0.70,
                'rHL20': rfix + 0.80,
                'rHL21': rfix + 0.90,
            }
class Page_6(Page):
    form_model = 'player'
    form_fields = ['rHL_22', 'rHL_23', 'rHL_24', 'rHL_25', 'rHL_26', 'rHL_27', 'rHL_28', 'rHL_29', 'rHL_30']

    def vars_for_template(self):
        if self.player.rHL_13 == 1:
            rfix = self.participant.vars['new_rfix'][0]
            self.participant.vars['new_rfix2']=[
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
                'rHL22': round(rfix - 0.09, 2),
                'rHL23': round(rfix - 0.08, 2),
                'rHL24': round(rfix - 0.07, 2),
                'rHL25': round(rfix - 0.06, 2),
                'rHL26': round(rfix - 0.05, 2),
                'rHL27': round(rfix - 0.04, 2),
                'rHL28': round(rfix - 0.03, 2),
                'rHL29': round(rfix - 0.02, 2),
                'rHL30': round(rfix - 0.01, 2),
            }
        elif self.player.rHL_14 == 1:
            rfix = self.participant.vars['new_rfix'][0]
            self.participant.vars['new_rfix2'] = [
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
                'rHL22': round(rfix + 0.01,2),
                'rHL23': round(rfix + 0.02,2),
                'rHL24': round(rfix + 0.03,2),
                'rHL25': round(rfix + 0.04,2),
                'rHL26': round(rfix + 0.05,2),
                'rHL27': round(rfix + 0.06,2),
                'rHL28': round(rfix + 0.07,2),
                'rHL29': round(rfix + 0.08,2),
                'rHL30': round(rfix + 0.09,2),
            }
        elif self.player.rHL_15 == 1:
            rfix = self.participant.vars['new_rfix'][1]
            self.participant.vars['new_rfix2'] = [
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
                'rHL22': round(rfix + 0.01, 2),
                'rHL23': round(rfix + 0.02, 2),
                'rHL24': round(rfix + 0.03, 2),
                'rHL25': round(rfix + 0.04, 2),
                'rHL26': round(rfix + 0.05, 2),
                'rHL27': round(rfix + 0.06, 2),
                'rHL28': round(rfix + 0.07, 2),
                'rHL29': round(rfix + 0.08, 2),
                'rHL30': round(rfix + 0.09, 2),
            }
        elif self.player.rHL_16 == 1:
            rfix = self.participant.vars['new_rfix'][2]
            self.participant.vars['new_rfix2'] = [
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
                'rHL22': round(rfix + 0.01, 2),
                'rHL23': round(rfix + 0.02, 2),
                'rHL24': round(rfix + 0.03, 2),
                'rHL25': round(rfix + 0.04, 2),
                'rHL26': round(rfix + 0.05, 2),
                'rHL27': round(rfix + 0.06, 2),
                'rHL28': round(rfix + 0.07, 2),
                'rHL29': round(rfix + 0.08, 2),
                'rHL30': round(rfix + 0.09, 2),
            }
        elif self.player.rHL_17 == 1:
            rfix = self.participant.vars['new_rfix'][3]
            self.participant.vars['new_rfix2'] = [
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
                'rHL22': round(rfix + 0.01, 2),
                'rHL23': round(rfix + 0.02, 2),
                'rHL24': round(rfix + 0.03, 2),
                'rHL25': round(rfix + 0.04, 2),
                'rHL26': round(rfix + 0.05, 2),
                'rHL27': round(rfix + 0.06, 2),
                'rHL28': round(rfix + 0.07, 2),
                'rHL29': round(rfix + 0.08, 2),
                'rHL30': round(rfix + 0.09, 2),
            }
        elif self.player.rHL_18 == 1:
            rfix = self.participant.vars['new_rfix'][4]
            self.participant.vars['new_rfix2'] = [
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
                'rHL22': round(rfix + 0.01, 2),
                'rHL23': round(rfix + 0.02, 2),
                'rHL24': round(rfix + 0.03, 2),
                'rHL25': round(rfix + 0.04, 2),
                'rHL26': round(rfix + 0.05, 2),
                'rHL27': round(rfix + 0.06, 2),
                'rHL28': round(rfix + 0.07, 2),
                'rHL29': round(rfix + 0.08, 2),
                'rHL30': round(rfix + 0.09, 2),
            }
        elif self.player.rHL_19 == 1:
            rfix = self.participant.vars['new_rfix'][5]
            self.participant.vars['new_rfix2'] = [
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
                'rHL22': round(rfix + 0.01, 2),
                'rHL23': round(rfix + 0.02, 2),
                'rHL24': round(rfix + 0.03, 2),
                'rHL25': round(rfix + 0.04, 2),
                'rHL26': round(rfix + 0.05, 2),
                'rHL27': round(rfix + 0.06, 2),
                'rHL28': round(rfix + 0.07, 2),
                'rHL29': round(rfix + 0.08, 2),
                'rHL30': round(rfix + 0.09, 2),
            }
        elif self.player.rHL_20 == 1:
            rfix = self.participant.vars['new_rfix'][6]
            self.participant.vars['new_rfix2'] = [
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
                'rHL22': round(rfix + 0.01, 2),
                'rHL23': round(rfix + 0.02, 2),
                'rHL24': round(rfix + 0.03, 2),
                'rHL25': round(rfix + 0.04, 2),
                'rHL26': round(rfix + 0.05, 2),
                'rHL27': round(rfix + 0.06, 2),
                'rHL28': round(rfix + 0.07, 2),
                'rHL29': round(rfix + 0.08, 2),
                'rHL30': round(rfix + 0.09, 2),
            }
        elif self.player.rHL_21 == 1:
            rfix = self.participant.vars['new_rfix'][7]
            self.participant.vars['new_rfix2'] = [
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
                'rHL22': round(rfix + 0.01, 2),
                'rHL23': round(rfix + 0.02, 2),
                'rHL24': round(rfix + 0.03, 2),
                'rHL25': round(rfix + 0.04, 2),
                'rHL26': round(rfix + 0.05, 2),
                'rHL27': round(rfix + 0.06, 2),
                'rHL28': round(rfix + 0.07, 2),
                'rHL29': round(rfix + 0.08, 2),
                'rHL30': round(rfix + 0.09, 2),
            }
        elif self.player.rHL_21 == 2:
            rfix = self.participant.vars['new_rfix'][8]
            self.participant.vars['new_rfix2'] = [
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
                'rHL22': round(rfix + 0.01, 2),
                'rHL23': round(rfix + 0.02, 2),
                'rHL24': round(rfix + 0.03, 2),
                'rHL25': round(rfix + 0.04, 2),
                'rHL26': round(rfix + 0.05, 2),
                'rHL27': round(rfix + 0.06, 2),
                'rHL28': round(rfix + 0.07, 2),
                'rHL29': round(rfix + 0.08, 2),
                'rHL30': round(rfix + 0.09, 2),
            }
    def before_next_page(self):
        self.participant.vars['final_rfix'] = Constants.rfix + self.participant.vars['new_rfix'] + self.participant.vars['new_rfix2']
        self.player.set_payoff_rHL()

class Page_7(Page):

    def vars_for_template(self):
       ra1_value = self.participant.vars['final_rfix'][self.session.vars['rHL_row'] - 1]
       self.participant.vars['ra1_value'] = ra1_value

       return{
            'rpayoff_HL': self.player.participant.vars['rpayoff_HL'],#payoff
            'rrow': self.player.session.vars['rHL_row'], # randomly chosen row
            'rvalue': self.session.vars['rHL_random'],# randomly chosen value to define outcome
            'rvalue2': self.session.vars['rHL_scenario'],
            'rchoice': self.participant.vars['rchoices'],# actual choice
            # outcomes of the selected row
            'ra1_value': ra1_value,
            'rp_A_1': self.session.vars['rHL_row'],
            'rp_A_2': 10-self.session.vars['rHL_row'],
            'rp_B_1': self.session.vars['rHL_row'],
            'rp_B_2': 10-self.session.vars['rHL_row'],
            }


page_sequence = [Page_0,
                 Page_1,
                 Page_2,
                 Page_3,
                 Page_4,
                 Page_5,
                 Page_6,
                 Page_7
]
