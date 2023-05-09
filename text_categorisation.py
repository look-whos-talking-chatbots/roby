"""
File contains the text classification functions for roby-based chatbots.
"""

import spacy

from src.settings import CLASSIFIER_PATHS


def intent_quit_whynot(user_input):
    user_input = user_input.lower()

    label = None
    threshold = 0.5

    nlp = spacy.load(CLASSIFIER_PATHS.format('quit-why-not-en-roby-v2'))

    predictions = nlp(user_input).cats

    pred = max(predictions.items(), key=lambda x: x[1])

    if pred and pred[1] > threshold:
        label = pred[0]

    return label


def intent_quitting_reason(user_input):
    user_input = user_input.lower()

    label = None
    threshold = 0.45
    nlp = spacy.load(CLASSIFIER_PATHS.format('quitting-reasons-en-roby-v2'))

    predictions = nlp(user_input).cats

    pred = max(predictions.items(), key=lambda x: x[1])

    if pred and pred[1] > threshold:
        label = pred[0]

    return label
