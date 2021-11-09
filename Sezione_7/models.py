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
Sezione 7
"""


class Constants(BaseConstants):
    name_in_url = 'Sezione_7'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    year = models.IntegerField(label='1. Anno di nascita', min=1900, max=2013)

    year_azienda = models.IntegerField(label='2. Anno di insediamento aziendale', min=1900)

    gender = models.StringField(
        choices=[['1', 'M'], ['2', 'F']],
        label='3. Genere',
        widget=widgets.RadioSelect,
    )
    istruzione = models.StringField(
        choices=[['1', 'Scuola elementare'], ['2', 'Scuola media'],
                 ['3', 'Scuola secondaria'], ['4', 'Laurea'], ['5', 'Formazione post-laura']],
        label='4. Livello di istruzione più alto',
        widget=widgets.RadioSelect,
    )
    area = models.IntegerField(label='5. Numero ettari (di proprietà e in affitto) gestiti dalla tua azienda',
                               min=1)
    areagrain = models.IntegerField(label='6. Numero ettari coltivati a grano duro',
                               min=1)
    title = models.StringField(
        choices=[['1', 'Coltivatore diretto'], ['2', 'IAP (imprenditore agricolo professionale'],
                 ['3', 'Altro (specificare)']],
        label='7. A che titolo svolgi la tua attività agricola',
        widget=widgets.RadioSelect,
    )
    status = models.StringField(
        choices=[['1', 'Azienda individuale'], ['2', 'Società di persone'],
                 ['3', 'Società di capitali'],['4', 'Altro']],
        label='8. Forma giuridica della tua azienda',
        widget=widgets.RadioSelect,
    )
    businesstype = models.StringField(
        choices=[['1', 'Specializzata in seminativi'], ['2', 'Mista colture'],
                 ['3', 'Mista colture e allevamento']],
        label='9. Tipologia della tua azienda',
        widget=widgets.RadioSelect,
    )
    revenue = models.StringField(
        choices=[['1', 'Meno di 4.000 €'],
                 ['2 ', 'Da 4.000 € a meno di 8.000 €'],
                 ['3', 'Da 8.000 € a meno di 25.000 €'],
                 ['4', 'Da 25.000 € a meno di 50.000 €'],
                 ['5', 'Da 50.000 € a meno di 100.000 €'],
                 ['6', 'Da 100.000 € a meno di 500.000 €'],
                 ['7', 'Da 500.000 € a meno di 1.000.000 €']],
        label='10. Fatturato medio annuo della tua azienda',
        widget=widgets.RadioSelect)
    q11 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='11. Nella tua azienda, hai già fatto uso di contratti di coltivazione nel corso degli ultimi '
              '5 anni?',
        widget=widgets.RadioSelect)
    q12 = models.StringField(
        choices=[['1', 'Meno di 5 anni'],
                 ['2', 'Da 5 a 15 anni'],
                 ['3', 'Più di 15 anni']],
        label='12. Da quanti anni è presente la attuale conduzione aziendale?',
        widget=widgets.RadioSelect,
    )
    q13 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='13. Prevedi che la tua azienda possa cambiare gestione nell arco dei prossimi anni?',
        widget=widgets.RadioSelect)

    q14 = models.StringField(
        choices=[['1', 'Sarà venduta a terzi'], ['2', 'Sarà gestita da un altro membro della famiglia (successione)']],
        label='14. SE SI, prevedi che la tua azienda',
        widget=widgets.RadioSelect)

    q15 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='15. Hai mai fatto INVESTIMENTI IN AZIENDA (ammodernamento parco macchine, attrezzi, strutture aziendali'
              ') in passato?',
        widget=widgets.RadioSelect)
    q16 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='16. Intendi farlo in futuro?',
        widget=widgets.RadioSelect)
    q17 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='17. Hai mai STIPULATO CONTRATTI DI PRODUZIONE in passato?',
        widget=widgets.RadioSelect)
    q18 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='18. Intendi farlo in futuro?',
        widget=widgets.RadioSelect)
    q19 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='19. Hai mai CONTRATTO DEBITI (es. prestiti bancari) per la gestione dell azienda?',
        widget=widgets.RadioSelect)
    q20 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='20. Intendi farlo in futuro?',
        widget=widgets.RadioSelect)
    q21 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='21. Hai mai fatto ACCANTONAMENTI FINANZIARI nella tua azienda?',
        widget=widgets.RadioSelect)
    q22 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='22. Intendi farlo in futuro?',
        widget=widgets.RadioSelect)
    q23 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='23. Hai mai INTRODOTTO VARIETÀ INNOVATIVE in azienda in passato?',
        widget=widgets.RadioSelect)
    q24 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='24. Intendi farlo in futuro?',
        widget=widgets.RadioSelect)
    q25 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='25. Hai mai ADOTTATO L\' ASSICURAZIONE AGRICOLA in passato?',
        widget=widgets.RadioSelect)
    q26 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='26. Intendi farlo in futuro?',
        widget=widgets.RadioSelect)
    q27 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='27. Hai mai PRATICATO LA DIVERSIFICAZIONE (produttiva, attività connesse es. agriturismo,'
              'vendita aziendale) in azienda in passato?',
        widget=widgets.RadioSelect)
    q28 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='28. Intendi farlo in futuro?',
        widget=widgets.RadioSelect)
    q29 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='29. Hai mai fatto USO DI SISTEMI DI IRRIGAZIONE in azienda in passato?',
        widget=widgets.RadioSelect)
    q30 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='30. Intendi farlo in futuro?',
        widget=widgets.RadioSelect)
    q31 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='31. Hai mai ADOTTATO LA PRODUZIONE BIOLOGICA in azienda?',
        widget=widgets.RadioSelect)
    q32 = models.StringField(
        choices=[['1', 'SI'], ['2', 'NO']],
        label='32. Intendi farlo in futuro?',
        widget=widgets.RadioSelect)

    likert1 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert4 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert5 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert6 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert7 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert8 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert9 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )

    likert10 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert11 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert12 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert13 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )

    likert14 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert15 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert16 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert17 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert18 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert19 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert20 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert21 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert22 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert23 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
    likert24 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', '']],
        label='',
        widget=widgets.RadioSelectHorizontal,
    )
