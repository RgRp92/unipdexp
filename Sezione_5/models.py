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
Sezione 5
"""


class Constants(BaseConstants):
    name_in_url = 'Sezione_5'
    players_per_group = None
    num_rounds = 1

    # Colors picked with a good pallete
    hex_colors = ["#F8766D", "#00BFC4"]


class Subsession(BaseSubsession):
    def creating_session(self):
        farm_dat_new = pd.read_csv("farmdata/data.csv")
        self.session.vars["beliefs_farm_dat_new"] = farm_dat_new
        self.session.vars["beliefs_hex_colors"] = ["#ff9933", "#00BFC4"]



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    labelset = models.IntegerField(default=0)

    final_payment = models.StringField()

    nbin1 = models.IntegerField(initial=0)
    nbin2 = models.IntegerField(initial=0)
    nbin3 = models.IntegerField(initial=0)
    nbin4 = models.IntegerField(initial=0)
    nbin5 = models.IntegerField(initial=0)
    nbin6 = models.IntegerField(initial=0)
    nbin7 = models.IntegerField(initial=0)
    nbin8 = models.IntegerField(initial=0)

    nw_amt = models.FloatField(default=0,min=0,label="")

    def set_winning_bin(self):
            self.participant.vars['nw_bin'] = "4"