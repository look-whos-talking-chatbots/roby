"""
Contains the indices for the functions belong to this bot
"""

import os

from .actions import *
from .entity_extraction import *
from .text_categorisation import *

FLOWS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flows')

AGENT_INDEX = {
    '6oqxajidwbr': {
        'path': 'roby_mi',
        'generators': None
    },
    'ecx7ngmyk9': {
        'path': 'roby_cc',
        'generators': None
    },
    'xmk776m7f5l': {
        'path': 'robygen_mi',
        'generators': ['gpt35'],
    },
    'robygen-all': {
        'path': 'robygen_mi',
        'generators': ['all'],
    },
    'robygen-gpt': {
        'path': 'robygen_mi',
        'generators': ['gpt3'],
    },
    'robygen-dialogpt': {
        'path': 'robygen_mi',
        'generators': ['dialogpt'],
    },
}

CATEGORISATION_INDEX = {
    'quit_whynot': intent_quit_whynot,
    'quitting_reason': intent_quitting_reason,
}

ENTITY_EXTRACTION_INDEX = {
    'cigarette_units': extract_cigarette_units,
}

ACTION_INDEX = {
    'append_quitting_reason': append_quitting_reason,
    'count_quitting_reason': count_quitting_reason,
    'process_norm_answer': process_norm_answer,
    'calculate_nicotine_dependency': calculate_nicotine_dependency,
    'is_longer_1day': is_longer_1day,
}

GENERATION_INDEX = {}
