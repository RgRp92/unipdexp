from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

author = 'RR'

doc = """
Beliefs Task
"""
# To read from the CSV file
import pandas as pd
import random


author = 'Ruggiero Rippo'

doc = """
Sezione 2
"""


class Constants(BaseConstants):
    name_in_url = 'Sezione_2'
    players_per_group = None
    num_rounds = 1

    # Colors picked with a good pallete
    hex_colors = ["#F8766D", "#00BFC4"]



class Subsession(BaseSubsession):
    def creating_session(self):
        farm_dat = pd.read_csv("farmdata/data.csv")
        self.session.vars["beliefs_farm_dat"] = farm_dat
        self.session.vars["beliefs_hex_colors"] = ["#ff9933", "#00BFC4"]

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    labelset = models.IntegerField(default=0)

    final_payment = models.StringField()

    bin1 = models.IntegerField(initial=0)
    bin2 = models.IntegerField(initial=0)
    bin3 = models.IntegerField(initial=0)
    bin4 = models.IntegerField(initial=0)
    bin5 = models.IntegerField(initial=0)
    bin6 = models.IntegerField(initial=0)
    bin7 = models.IntegerField(initial=0)
    bin8 = models.IntegerField(initial=0)

    w_amt = models.FloatField(default=0,min=0,label="")

    def set_winning_bin(self):
        self.participant.vars['nw_bin'] = "4"