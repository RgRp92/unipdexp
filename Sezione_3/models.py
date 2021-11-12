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
           round(26.00,2),
           round(30.00,2),
           round(34.00,2),
           round(38.00,2),
           round(42.00,2),
           round(46.00,2),
           round(50.00,2),
           round(54.00,2)]

    fix2 = [round(36.00, 2)]


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['HL_row'] = random.randint(1,9)
        self.session.vars['HL_row2'] = random.randint(10,13)
        self.session.vars['HL_row3'] = random.randint(14,23)
        self.session.vars['HL_row4'] = random.randint(24,33)

        self.session.vars['HL_random'] = random.randint(1,4)


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    HL_1 = models.IntegerField(choices=[[1, ''],
                                        [2, ''],
                                        [3, ''],
                                        [4, ''],
                                        [5, ''],
                                        [6, ''],
                                        [7, ''],
                                        [8, ''],
                                        [9, ''],
                                        ],widget=widgets.RadioSelect ,blank=True, initial =1 )
    HL_2 = models.IntegerField(choices=[[10, ''],
                                        [11, ''],
                                        [12, ''],
                                        [13, ''],
                                        ], widget=widgets.RadioSelect, blank=True,initial =10)
    HL_3 = models.IntegerField(choices=[[14, ''],
                                        [15, ''],
                                        [16, ''],
                                        [17, ''],
                                        [18, ''],
                                        [19, ''],
                                        [20, ''],
                                        [21, ''],
                                        [22, ''],
                                        [23, '']], widget=widgets.RadioSelect, blank=True,initial =14)
    HL_4 = models.IntegerField(choices=[[24, ''],
                                        [25, ''],
                                        [26, ''],
                                        [27, ''],
                                        [28, ''],
                                        [29, ''],
                                        [30, ''],
                                        [31, ''],
                                        [32, ''],
                                        [33, ''],], widget=widgets.RadioSelect, blank=True,initial =24)

    def set_row(self):
        if self.session.vars['HL_random'] == 1:
            self.participant.vars["w_row"] = self.session.vars["HL_row"]
        elif self.session.vars['HL_random'] == 2:
            self.participant.vars["w_row"] = self.session.vars["HL_row2"]
        elif self.session.vars['HL_random'] == 3:
            self.participant.vars["w_row"] = self.session.vars["HL_row3"]
        else:
            self.participant.vars["w_row"] = self.session.vars["HL_row4"]


    def set_payoff_HL(self):

        choices = [self.HL_1,self.HL_2,self.HL_3,self.HL_4]

        self.participant.vars['choices'] = choices
       # *******************************************
        # Compute here the payoffs
        # *******************************************
        if self.session.vars['HL_random'] == 1:
            # if the random number is smaller equal than the random row
            if self.participant.vars['choices'][0] <= self.participant.vars['w_row']:  # A
                # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.fix[self.participant.vars['w_row']-1]
                # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = Constants.fix2[0]
        elif self.session.vars['HL_random'] == 2:
            if self.participant.vars['choices'][1] <= self.participant.vars['w_row']:
                self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][self.participant.vars['w_row']-1]
            else:
                self.participant.vars['payoff_HL'] = Constants.fix2[0]
        elif self.session.vars['HL_random'] == 3:
            if self.participant.vars['choices'][2] <= self.participant.vars['w_row']:
                self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][self.participant.vars['w_row']-1]
            else:
                self.participant.vars['payoff_HL'] = Constants.fix2[0]
        elif self.session.vars['HL_random'] == 4:
            if self.participant.vars['choices'][3] <= self.participant.vars['w_row']:
                self.participant.vars['payoff_HL'] = self.participant.vars['final_fix'][self.participant.vars['w_row']-1]
            else:
                self.participant.vars['payoff_HL'] = Constants.fix2[0]


        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff

