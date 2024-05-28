"""
File contains corpus data required for the roby-related natural language understanding module.
"""

CIGARETTE_UNITS = {
    'en': [
        'smoke', 'a smoke', 'smokes',
        'puff', 'a puff', 'puffs',
        'cig', 'a cig', 'cigs',
        'e-cig', 'an e-cig', 'e-cigs',
        'cigarette', 'a cigarette', 'cigarettes',
        'e-cigarette', 'an e-cigarette', 'e-cigarettes',
        'box', 'a box', 'boxes',
        'pack', 'a pack', 'packs',
        'packet', 'a packet', 'packets',
        'package', 'a package', 'packages',
        'fag packet', 'a fag packet', 'fag packets',  # a british slang
        'carton', 'a carton', 'cartons',
        'times',
    ],
    'nl': [
        'rook', 'een rook', 'rookt', 'rookje', 'rookjes',
        'trek', 'een trekje', 'trekjes',
        'sigaret', 'een sigaret', 'sigaretten',
        'e-sig', 'een e-sig', 'e-sigs',
        'sigaret', 'een sigaret', 'sigaretten',
        'e-sigaret', 'een e-sigaret', 'e-sigaretten',
        'doos', 'een doos', 'dozen',
        'pakket', 'een pakket', 'pakketten',
        'pakketje', 'een pakketje', 'pakketjes',
        'karton', 'een doos', 'kartonen',
        'keer',
    ]
}

IS_SMOKER = {
    'en': {
        'smoker': ['smoke', 'smoking', 'smokng', 'smoker', 'smkr', 'smker'],
        'non-smoker': ['no', 'not', 'non', 'dont', 'nonsmoker', 'nosmoker', 'nosmoke']
    },
    'nl': {
        'smoker': ['rook', 'rok', 'roook', 'roken', 'rokn', 'rken', 'rokne',
                   'rooken', 'roker', 'rooker', 'rker', 'rokr', 'rokre'],
        'non-smoker': ['nee', 'geen', 'gee', 'ne', 'ex', 'niet', 'net', 'not', 'nit', 'nietroker',
                       'nitroker', 'nietroken', 'nieroker', 'nitroken', 'geenroker',
                       'exroker', 'ex roker', 'exrokr', 'exrker']
    }
}

IF_THEN_REG = {
    'en': r'.*if.*then.*',
    'nl': r'.*als.*dan.*'
}
