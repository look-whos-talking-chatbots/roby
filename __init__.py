"""
Contains the indices for the functions belong to this bot
"""

import os

from .actions import *
from .entity_extraction import *
from .text_categorisation import *
from .generation_models import *

FLOWS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flows')

# TODO: AGENT INDEX could be another JSON object (list of lists) where each item represents a configuration of a bot
# TODO: CATEGORISATION, ENTITY EXTRACTION, and ACTION functions could just be automatically loaded into these JSON objects.

AGENT_INDEX = {
    '6oqxajidwbr': {
        'path': 'roby_mi',
        'generators': None,
        'onhold_duration': 500000,
    },
    '089kdpbq91yc': {
        'path': 'roby_mi_nl',
        'generators': None,
        'onhold_duration': 500000,
    },
    'ecx7ngmyk9': {
        'path': 'roby_cc',
        'generators': None
    },
    'roby-mi-gpt': {
        'path': 'robygen_mi',
        'generators': ['gpt35'],
    }
}

CATEGORISATION_INDEX = {
    'quit_whynot': intent_quit_whynot,
    'quitting_reason': intent_quitting_reason,
    'starting_reason': intent_starting_reason,
    'smoking_opinion': intent_smoking_opinion,
    'is_smoker': intent_is_smoker,
    'is_if_then': intent_is_if_then,
    'sentiment_roby': intent_sentiment,
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
    'is_in_1week': is_in_1week,
    'is_in_2weeks': is_in_2weeks,
}

GENERATION_INDEX = {}
