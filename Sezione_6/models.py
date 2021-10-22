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
           round(26.00,2),
           round(30.00,2),
           round(34.00,2),
           round(38.00,2),
           round(42.00,2),
           round(46.00,2),
           round(50.00,2),
           round(54.00,2)]

    rfix2 = [round(36.00, 2)]


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['rHL_row'] = random.randint(1,9)
        self.session.vars['rHL_row2'] = random.randint(10,13)
        self.session.vars['rHL_row3'] = random.randint(14,23)
        self.session.vars['rHL_row4'] = random.randint(24,33)

        self.session.vars['rHL_random'] = random.randint(1,4)


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    rHL_1 = models.IntegerField(choices=[[1, ''],
                                        [2, ''],
                                        [3, ''],
                                        [4, ''],
                                        [5, ''],
                                        [6, ''],
                                        [7, ''],
                                        [8, ''],
                                        [9, '']],widget=widgets.RadioSelect ,blank=True, initial=1)
    rHL_2 = models.IntegerField(choices=[[10, ''],
                                        [11, ''],
                                        [12, ''],
                                        [13, ''],
                                        ], widget=widgets.RadioSelect, blank=True, initial=10)
    rHL_3 = models.IntegerField(choices=[[14, ''],
                                        [15, ''],
                                        [16, ''],
                                        [17, ''],
                                        [18, ''],
                                        [19, ''],
                                        [20, ''],
                                        [21, ''],
                                        [22, ''],
                                        [23, '']], widget=widgets.RadioSelect, blank=True,initial=14)
    rHL_4 = models.IntegerField(choices=[[24, ''],
                                        [25, ''],
                                        [26, ''],
                                        [27, ''],
                                        [28, ''],
                                        [29, ''],
                                        [30, ''],
                                        [31, ''],
                                        [32, ''],
                                        [33, ''],], widget=widgets.RadioSelect, blank=True,initial=24)

    def set_row2(self):
        if self.session.vars['rHL_random'] == 1:
            self.participant.vars["w_rrow"] = self.session.vars["rHL_row"]
        elif self.session.vars['rHL_random'] == 2:
            self.participant.vars["w_rrow"] = self.session.vars["rHL_row2"]
        elif self.session.vars['rHL_random'] == 3:
            self.participant.vars["w_rrow"] = self.session.vars["rHL_row3"]
        else:
            self.participant.vars["w_rrow"] = self.session.vars["rHL_row4"]

        rchoices = [self.rHL_1,self.rHL_2,self.rHL_3,self.rHL_4]

        self.participant.vars['rchoices'] = rchoices

    def set_payoff_HLr(self):

        rchoices = [self.rHL_1,self.rHL_2,self.rHL_3,self.rHL_4]

        self.participant.vars['rchoices'] = rchoices
        # *******************************************
        # Compute here the payoffs
        # *******************************************
        if self.session.vars['rHL_random'] == 1:
            # if the random number is smaller equal than the random row
            if self.participant.vars['rchoices'][0] <= self.participant.vars['w_rrow']:  # A
                # if the choice was A
                self.participant.vars['payoff_HLr'] = Constants.rfix[self.participant.vars['w_rrow']-1]
                # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HLr'] = Constants.rfix2[0]
        elif self.session.vars['rHL_random'] == 2:
            if self.participant.vars['rchoices'][1] <= self.participant.vars['w_rrow']:
                self.participant.vars['payoff_HLr'] = self.participant.vars['final_rfix'][self.participant.vars['w_rrow']-1]
            else:
                self.participant.vars['payoff_HLr'] = Constants.rfix2[0]
        elif self.session.vars['rHL_random'] == 3:
            if self.participant.vars['rchoices'][2] <= self.participant.vars['w_rrow']:
                self.participant.vars['payoff_HLr'] = self.participant.vars['final_rfix'][self.participant.vars['w_rrow']-1]
            else:
                self.participant.vars['payoff_HLr'] = Constants.rfix2[0]
        elif self.session.vars['rHL_random'] == 4:
            if self.participant.vars['rchoices'][3] <= self.participant.vars['w_rrow']:
                self.participant.vars['payoff_HLr'] = self.participant.vars['final_rfix'][self.participant.vars['w_rrow']-1]
            else:
                self.participant.vars['payoff_HLr'] = Constants.rfix2[0]


        self.payoff = self.participant.vars['payoff_HLr']
        # write the payoff to player.payoff