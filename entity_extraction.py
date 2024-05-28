"""
File contains the roby-related entity extraction functions.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from .corpus import CIGARETTE_UNITS
from common.entity_extraction import extract_units


def extract_cigarette_units(user_input, language):
    return extract_units(user_input, CIGARETTE_UNITS[language], language)
