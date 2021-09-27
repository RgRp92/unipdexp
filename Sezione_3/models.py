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
Sezione 3
"""


class Constants(BaseConstants):
    name_in_url = 'Sezione_3'
    players_per_group = None
    num_rounds = 1

    fix = [round(22.00,2),
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

    fix2 = [round(24.00, 2),
           round(26.00, 2),
           round(28.00, 2),
           round(30.00, 2),
           round(32.00, 2),
           round(34.00, 2)]


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['HL_row'] = random.randint(1, 30)

        self.session.vars['HL_random'] = random.randint(1, 30)

        self.session.vars['HL_scenario'] = random.randint(1, 100)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    HL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_8 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_9 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_10 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_11 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_12 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    HL_13 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_14 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_15 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_16 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_17 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_18 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_19 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_20 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_21 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)

    HL_22 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_23 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_24 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_25 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_26 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_27 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_28 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_29 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_30 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)


    def set_payoff_HL(self):

        choices = [self.HL_1,self.HL_2,self.HL_3,self.HL_4,self.HL_5,self.HL_6,self.HL_7,self.HL_8,self.HL_9,self.HL_10,
                   self.HL_11,self.HL_12,self.HL_13,self.HL_14,self.HL_15,self.HL_16,self.HL_17,self.HL_18,self.HL_19,
                   self.HL_20,self.HL_21,self.HL_22,self.HL_23,self.HL_24,self.HL_25,self.HL_26,self.HL_27,self.HL_28,
                   self.HL_29,self.HL_30]

        self.participant.vars['choices'] = choices[self.session.vars['HL_row'] - 1]

        # *******************************************
        # Compute here the payoffs
        # *******************************************
        if self.session.vars['HL_row'] <= 12:
            if self.session.vars['HL_scenario'] <= 30:
            # if the random number is smaller equal than the random row
                if self.participant.vars['choices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.fix[self.session.vars['HL_row'] - 1]
                # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[0]
            elif self.session.vars['HL_scenario'] > 30 and self.session.vars['HL_scenario'] <= 54:
            # if the random number is larger than the random row
                if self.participant.vars['choices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.fix[self.session.vars['HL_row'] - 1]
                # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[1]
            elif self.session.vars['HL_scenario'] > 54 and self.session.vars['HL_scenario'] <= 73:
            # if the random number is larger than the random row
                if self.participant.vars['choices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.fix[self.session.vars['HL_row'] - 1]
                # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[2]
            elif self.session.vars['HL_scenario'] > 73 and self.session.vars['HL_scenario'] <= 88:
            # if the random number is larger than the random row
                if self.participant.vars['choices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.fix[self.session.vars['HL_row'] - 1]
                # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[3]
            elif self.session.vars['HL_scenario'] > 88 and self.session.vars['HL_scenario'] <= 90:
            # if the random number is larger than the random row
                if self.participant.vars['choices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.fix[self.session.vars['HL_row'] - 1]
                # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[4]
            elif self.session.vars['HL_scenario'] > 90 and self.session.vars['HL_scenario'] <= 100:
            # if the random number is larger than the random row
                if self.participant.vars['choices'] == 1:  # A
                # if the choice was A
                    self.participant.vars['payoff_HL'] = Constants.fix[self.session.vars['HL_row'] - 1]
                # because HL_row is the same as p in the MPL
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[5]
        elif self.session.vars['HL_row'] > 12 and self.session.vars['HL_row'] <= 21:
            if self.session.vars['HL_scenario'] <= 30:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[0]
            elif self.session.vars['HL_scenario'] > 30 and self.session.vars['HL_scenario'] <= 54:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[1]
            elif self.session.vars['HL_scenario'] > 54 and self.session.vars['HL_scenario'] <= 73:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][
                        self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[2]
            elif self.session.vars['HL_scenario'] > 73 and self.session.vars['HL_scenario'] <= 88:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][
                        self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[3]
            elif self.session.vars['HL_scenario'] > 88 and self.session.vars['HL_scenario'] <= 90:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][
                        self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[4]
            elif self.session.vars['HL_scenario'] > 90 and self.session.vars['HL_scenario'] <= 100:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][
                        self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[5]
        elif self.session.vars['HL_row'] > 21 and self.session.vars['HL_row'] <= 30:
            if self.session.vars['HL_scenario'] <= 30:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[0]
            elif self.session.vars['HL_scenario'] > 30 and self.session.vars['HL_scenario'] <= 54:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[1]
            elif self.session.vars['HL_scenario'] > 54 and self.session.vars['HL_scenario'] <= 73:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[2]
            elif self.session.vars['HL_scenario'] > 73 and self.session.vars['HL_scenario'] <= 88:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][
                        self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[3]
            elif self.session.vars['HL_scenario'] > 88 and self.session.vars['HL_scenario'] <= 90:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][
                        self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[4]
            elif self.session.vars['HL_scenario'] > 90 and self.session.vars['HL_scenario'] <= 100:
                if self.participant.vars['choices'] == 1:
                    self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][
                        self.session.vars['HL_row'] - 1]
                else:
                    self.participant.vars['payoff_HL'] = Constants.fix2[5]


        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff