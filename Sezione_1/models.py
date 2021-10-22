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


author = 'Ruggiero Rippo'

doc = """
Sezione_1
"""


class Constants(BaseConstants):
    name_in_url = 'Sezione_1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    tab_1 = models.BooleanField(blank=True)
    tab_2 = models.BooleanField(blank=True)
    tab_3 = models.BooleanField(blank=True)
    tab_4 = models.BooleanField(blank=True)
    tab_5 = models.BooleanField(blank=True)
    tab_6 = models.BooleanField(blank=True)
    tab_7 = models.BooleanField(blank=True)

