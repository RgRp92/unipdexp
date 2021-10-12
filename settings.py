from os import environ

SESSION_CONFIGS = [
    dict(
        name='Test',
        display_name="Test",
        num_demo_participants=2,
        app_sequence=[ 'Sezione_6', 'FinalPayment']
    ),
    dict(
        name='Studio',
        display_name="Studio",
        num_demo_participants=1,
        app_sequence=['Intro', 'Sezione_1','Sezione_2','Sezione_3',
                      'Sezione_4','Sezione_5','Sezione_6','Sezione_7', 'FinalPayment']
    ),
    dict(
        name='Intro',
        display_name="Intro",
        num_demo_participants=1,
        app_sequence=['Intro']
    ),
    dict(
        name='Sezione_1',
        display_name="Sezione_1",
        num_demo_participants=1,
        app_sequence=['Sezione_1']
    ),
    dict(
        name='Sezione_2',
        display_name="Sezione_2",
        num_demo_participants=1,
        app_sequence=['Sezione_2']
    ),
    dict(
        name='Sezione_3',
        display_name="Sezione_3",
        num_demo_participants=1,
        app_sequence=['Sezione_3']
    ),
    dict(
        name='Sezione_4',
        display_name="Sezione_4",
        num_demo_participants=1,
        app_sequence=['Sezione_4']
    ),
    dict(
        name='Sezione_5',
        display_name="Sezione_5",
        num_demo_participants=1,
        app_sequence=['Sezione_5']
    ),
    dict(
        name='Sezione_6',
        display_name="Sezione_6",
        num_demo_participants=1,
        app_sequence=['Sezione_6']
    ),
    dict(
        name='Sezione_7',
        display_name="Sezione_7",
        num_demo_participants=1,
        app_sequence=['Sezione_7']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'a570(hnm-i+@6(d$kb6(ndac*6*9#u6ai3g+mr75tz66_5qr@u'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
ROOMS = [
    dict(
        name='pilot_1',
        display_name = 'Studio Pilota 1',
        participant_label_file='rooms/pilot1label.txt',
        use_secure_urls=True
    ),
    dict(
        name='pilot_2',
        display_name = 'Studio Pilota 2',
        participant_label_file='rooms/pilot2label.txt',
        use_secure_urls=True
    ),
    dict(
        name='pilot_3',
        display_name = 'Studio Pilota 3',
        participant_label_file='rooms/pilot3label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_1',
        display_name = 'Studio Giorno 1',
        participant_label_file='rooms/day1_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_2',
        display_name = 'Studio Giorno 2',
        participant_label_file='rooms/day2_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_3',
        display_name = 'Studio Giorno 3',
        participant_label_file='rooms/day3_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_4',
        display_name = 'Studio Giorno 4',
        participant_label_file='rooms/day4_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_5',
        display_name = 'Studio Giorno 5',
        participant_label_file='rooms/day5_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_6',
        display_name = 'Studio Giorno 6',
        participant_label_file='rooms/day6_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_7',
        display_name = 'Studio Giorno 7',
        participant_label_file='rooms/day7_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_8',
        display_name = 'Studio Giorno 8',
        participant_label_file='rooms/day8_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_9',
        display_name = 'Studio Giorno 9',
        participant_label_file='rooms/day9_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_10',
        display_name = 'Studio Giorno 10',
        participant_label_file='rooms/day10_label.txt',
        use_secure_urls=True
    )
]