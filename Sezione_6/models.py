from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
author = 'Ruggiero Rippo'

doc = """
Sezione 6
"""


class Constants(BaseConstants):
    name_in_url = 'Sezione_6'
    players_per_group = None
    num_rounds = 1

    rfix = [round(22.00,2),
           round(23.00,2),
           round(24.00,2),
           round(25.00,2),
           round(26.00,2),
           round(27.00,2),
           round(28.00,2),
           round(29.00,2),
           round(30.00,2),
           round(31.00,2),
           round(32.00,2),
           round(33.00,2)]

    rfix2 = [round(24.00, 2),
            round(26.00, 2),
            round(28.00, 2),
            round(30.00, 2),
            round(32.00, 2),
            round(34.00, 2)]

class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['rHL_row'] = random.randint(1, 30)

        self.session.vars['rHL_random'] = random.randint(1, 30)

        self.session.vars['rHL_scenario'] = random.randint(1, 100)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rHL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_8 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_9 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_10 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_11 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_12 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    rHL_13 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_14 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_15 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_16 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_17 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_18 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_19 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_20 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_21 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    rHL_22 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_23 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_24 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_25 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_26 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_27 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_28 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_29 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_30 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)


    def set_payoff_rHL(self):
        rchoices = [self.rHL_1,self.rHL_2,self.rHL_3,self.rHL_4,self.rHL_5,self.rHL_6,self.rHL_7,self.rHL_8,self.rHL_9,self.rHL_10,
                   self.rHL_11,self.rHL_12,self.rHL_13,self.rHL_14,self.rHL_15,self.rHL_16,self.rHL_17,self.rHL_18,self.rHL_19,
                   self.rHL_20,self.rHL_21,self.rHL_22,self.rHL_23,self.rHL_24,self.rHL_25,self.rHL_26,self.rHL_27,self.rHL_28,
                   self.rHL_29,self.rHL_30]

        self.participant.vars['rchoices'] = rchoices[self.session.vars['rHL_row'] - 1]

        if self.session.vars['rHL_row'] <= 12:
            if self.session.vars['rHL_scenario'] <= 30:
            # if the random number is smaller equal than the random row
                if self.participant.vars['rchoices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rfix[self.session.vars['rHL_row'] - 1]
                # because rHL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[0]
            elif self.session.vars['rHL_scenario'] > 30 and self.session.vars['rHL_scenario'] <= 54:
            # if the random number is larger than the random row
                if self.participant.vars['rchoices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rfix[self.session.vars['rHL_row'] - 1]
                # because rHL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[1]
            elif self.session.vars['rHL_scenario'] > 54 and self.session.vars['rHL_scenario'] <= 73:
            # if the random number is larger than the random row
                if self.participant.vars['rchoices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rfix[self.session.vars['rHL_row'] - 1]
                # because rHL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[2]
            elif self.session.vars['rHL_scenario'] > 73 and self.session.vars['rHL_scenario'] <= 88:
            # if the random number is larger than the random row
                if self.participant.vars['rchoices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rfix[self.session.vars['rHL_row'] - 1]
                # because rHL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[3]
            elif self.session.vars['rHL_scenario'] > 88 and self.session.vars['rHL_scenario'] <= 90:
            # if the random number is larger than the random row
                if self.participant.vars['rchoices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rfix[self.session.vars['rHL_row'] - 1]
                # because rHL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[4]
            elif self.session.vars['rHL_scenario'] > 90 and self.session.vars['rHL_scenario'] <= 100:
            # if the random number is larger than the random row
                if self.participant.vars['rchoices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['rpayoff_HL'] = Constants.rfix[self.session.vars['rHL_row'] - 1]
                # because rHL_row is the same as p in the MPL
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[5]
        elif self.session.vars['rHL_row'] > 12 and self.session.vars['rHL_row'] <= 21:
            if self.session.vars['rHL_scenario'] <= 30:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[0]
            elif self.session.vars['rHL_scenario'] > 30 and self.session.vars['rHL_scenario'] <= 54:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[1]
            elif self.session.vars['rHL_scenario'] > 54 and self.session.vars['rHL_scenario'] <= 73:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][
                        self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[2]
            elif self.session.vars['rHL_scenario'] > 73 and self.session.vars['rHL_scenario'] <= 88:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][
                        self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[3]
            elif self.session.vars['rHL_scenario'] > 88 and self.session.vars['rHL_scenario'] <= 90:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][
                        self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[4]
            elif self.session.vars['rHL_scenario'] > 90 and self.session.vars['rHL_scenario'] <= 100:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][
                        self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[5]
        elif self.session.vars['rHL_row'] > 21 and self.session.vars['rHL_row'] <= 30:
            if self.session.vars['rHL_scenario'] <= 30:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[0]
            elif self.session.vars['rHL_scenario'] > 30 and self.session.vars['rHL_scenario'] <= 54:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[1]
            elif self.session.vars['rHL_scenario'] > 54 and self.session.vars['rHL_scenario'] <= 73:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[2]
            elif self.session.vars['rHL_scenario'] > 73 and self.session.vars['rHL_scenario'] <= 88:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][
                        self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[3]
            elif self.session.vars['rHL_scenario'] > 88 and self.session.vars['rHL_scenario'] <= 90:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][
                        self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[4]
            elif self.session.vars['rHL_scenario'] > 90 and self.session.vars['rHL_scenario'] <= 100:
                if self.participant.vars['rchoices'] == 1:
                    self.participant.vars['rpayoff_HL'] = self.participant.vars['final_rfix'][
                        self.session.vars['rHL_row'] - 1]
                else:
                    self.participant.vars['rpayoff_HL'] = Constants.rfix2[5]


        self.payoff = self.participant.vars['rpayoff_HL']
        # write the payoff to player.payoff