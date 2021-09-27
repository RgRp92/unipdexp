from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import pandas as pd
import random
import json
from random import choices

def get_beldat_new(page_obj):

    farm_dat_new = page_obj.session.vars["beliefs_farm_dat_new"]

    nbin_labels = [str(farm_dat_new["alt" + str(b)].iloc[0]) for b in range(1,7) if str(farm_dat_new["alt" + str(b)].iloc[0]) != "nan"]
    alt_labels = [str(farm_dat_new["alt" + str(b)].iloc[0]) for b in range(1,7) if str(farm_dat_new["alt" + str(b)].iloc[0]) != "nan"]

    # If nbin_button is empty, don't show the button to toggle alt labels
    nbin_button = str(farm_dat_new["bin_button"].iloc[0]).strip()
    nbin_button = nbin_button if nbin_button != "nan" else ""
    pay_by = str(farm_dat_new["pay_by"].iloc[0]).strip()

    beldat_new = {
        "tokens": int(farm_dat_new["tokens"].iloc[0]),
        "alpha": float(farm_dat_new["alpha"].iloc[0]),
        "delta": float(farm_dat_new["delta"].iloc[0]),
        "currency": str(farm_dat_new["currency"].iloc[0]),
        "text": str(farm_dat_new["text"].iloc[0]),
        "alt_text": str(farm_dat_new["alt_text"].iloc[0]),
        "nbin_button": nbin_button,
        "alt_button": str(farm_dat_new["alt_button"].iloc[0]),
        "pay_by": pay_by,
        "nbin_labels": nbin_labels,
        "alt_labels": alt_labels,
        "num_nbins": len(nbin_labels),
    }

    # Store this data in the round data
    page_obj.participant.vars["beliefs_round_data"].append(beldat_new)
    return(beldat_new)

def set_beliefs_data(page_obj):
    nrounds = [1]
    nrounds = len(nrounds)
    page_obj.participant.vars["beliefs_num_rounds"] = nrounds


class Page_0(Page):
    pass
class Page_1(Page):
    pass
class Page_2(Page):
    pass
class Page_3(Page):
    def vars_for_template(self):
        # Set the belief data for the participant
        set_beliefs_data(self)

    def is_displayed(self):
        return self.round_number == 1


class Page_4(Page):
    form_model = "player"

    def initial_values(self):
        rnum = self.round_number
        # Randomize the data if we're in the first round
        if rnum == 1 and "beldat_new_is_set" not in self.participant.vars:
            self.participant.vars["beldat_new_is_set"] = True
            # Record the choices for every round here
            self.participant.vars["beliefs_choice"] = []
            # Record the data for each choice
            self.participant.vars["beliefs_round_data"] = []

    def get_form_fields(self):
        # Set initial values for this participant
        self.initial_values()
        # The belief data
        beldat_new = get_beldat_new(self)
        # Add the labelset val as wel
        form_fields = ["nbin" + str(i) for i in range(1, len(beldat_new["nbin_labels"]) + 1)] + ["labelset"]
        return (form_fields)

    def vars_for_template(self):
        # Set initial values for this participant

        self.initial_values()

        # The lottery data for this row
        beldat_new = get_beldat_new(self)

        nbeliefs = {"round_number": self.round_number,
                   "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
                   "hex_colors": self.session.vars["beliefs_hex_colors"],
                   "beldat_new": beldat_new,
                   "tokens": beldat_new["tokens"],
                   "currency": beldat_new["currency"],
                   "task_number": 1,
                   }

        return {
            "nbeliefs": nbeliefs,
        }

    def before_next_page(self):
        choice = [getattr(self.player, "nbin" + str(b)) for b in range(1, 7)]
        self.participant.vars["beliefs_choice"].append(choice)

    def is_displayed(self):
        return self.round_number <= self.participant.vars["beliefs_num_rounds"]

class Page_5(Page):
    form_model = "player"

    def vars_for_template(self):
        self.player.set_winning_bin()
        # Select a round at random for payment
        if "beliefs_pay_round" not in self.participant.vars:
            pay_round = self.round_number
            self.participant.vars["beliefs_pay_round"] = pay_round
        else:
            pay_round = self.participant.vars["beliefs_pay_round"]

        prev_player = self.player.in_round(pay_round)

        if self.participant.vars['nw_bin'] == "1":
            self.participant.vars['np_bin'] = prev_player.nbin1
        if self.participant.vars['nw_bin'] == "2":
            self.participant.vars['np_bin'] = prev_player.nbin2
        if self.participant.vars['nw_bin'] == "3":
            self.participant.vars['np_bin'] = prev_player.nbin3
        if self.participant.vars['nw_bin'] == "4":
            self.participant.vars['np_bin'] = prev_player.nbin4
        if self.participant.vars['nw_bin'] == "5":
            self.participant.vars['np_bin'] = prev_player.nbin5
        if self.participant.vars['nw_bin'] == "6":
            self.participant.vars['np_bin'] = prev_player.nbin6


        self.player.nw_amt = (12.5) + \
                            12.5 * ((2 * self.participant.vars['np_bin'] / 100) - (1 / 10000) * (
                prev_player.nbin1 ** 2 + prev_player.nbin2 ** 2 + prev_player.nbin3 ** 2 +
                prev_player.nbin4 ** 2 + prev_player.nbin5 ** 2 + prev_player.nbin6 ** 2))

        nw_amt = round(self.player.nw_amt, 2)

        nchoices_made = self.participant.vars["beliefs_choice"]

        pay_nchoices = nchoices_made[0]

        # The saved choices made by the subject


        # The lottery data for this row
        beldat_new = self.participant.vars["beliefs_round_data"][0]

        # Not really used anywhere
        final_payment = {
            "currency": beldat_new["currency"],
            "amounts": [],
            "when": [beldat_new["pay_by"]],
            "nchoices": pay_nchoices,
        }
        self.participant.vars["beliefs_final_payment"] = final_payment
        setattr(self.player, "final_payment", json.dumps(final_payment))

        nbeliefs_results = {
            "round_number": self.round_number,
            "number_of_rounds": self.participant.vars["beliefs_num_rounds"],
            "hex_colors": self.session.vars["beliefs_hex_colors"],
            "beldat_new": beldat_new,
            "tokens": beldat_new["tokens"],
            "currency": beldat_new["currency"],
            "task_number": 6,
            "pay_round": pay_round,
            "pay_nchoices": pay_nchoices,
            "final_payment": final_payment,
        }
        # Save this data for use in the final results page
        self.participant.vars["nbeliefs_results"] = nbeliefs_results

        return {
            "nbeliefs": nbeliefs_results,
            "nw_amt": round(nw_amt, 2),
            "nw": self.participant.vars["nw_bin"],
            "var": self.session.vars["variation"],
            "pbin": self.participant.vars["np_bin"]

        }

    def before_next_page(self):
        self.participant.vars["nw_amt"] = round(self.player.nw_amt, 2)


page_sequence = [Page_0,
                 Page_1,
                 Page_2,
                 Page_3,
                 Page_4,
                 Page_5
]
