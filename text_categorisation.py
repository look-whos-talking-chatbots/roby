"""
File contains the text classification functions for roby-based chatbots.
"""

import re
import spacy

from .settings import CLASSIFIER_PATHS
from .corpus import IS_SMOKER, IF_THEN_REG


def base_intent_spacy(user_input, classifier_name, threshold):

    label = None

    classifier = spacy.load(CLASSIFIER_PATHS.format(classifier_name))

    predictions = classifier(user_input).cats

    pred = max(predictions.items(), key=lambda x: x[1])

    if pred and pred[1] > threshold:
        label = pred[0]

    return label


def intent_quit_whynot(user_input, language):
    user_input = user_input.lower()

    classifier_names = {
        'en': 'quit-why-not-en-roby-v2',
        'nl': 'quit-why-not-nl-roby-v1'
    }

    if language not in classifier_names:
        # TODO: LOGGER.warning('There is no classifier for this language')
        return None

    label = base_intent_spacy(user_input,
                              classifier_names[language],
                              threshold=0.3)

    return label


def intent_quitting_reason(user_input, language):
    user_input = user_input.lower()

    classifier_names = {
        'en': 'quitting-reasons-en-roby-v2',
        'nl': 'quitting-reasons-nl-roby-v1'
    }

    if language not in classifier_names:
        return None

    label = base_intent_spacy(user_input,
                              classifier_names[language],
                              threshold=0.4)

    return label


def intent_starting_reason(user_input, language):
    user_input = user_input.lower()

    classifier_names = {
        'en': 'starting-reason-en-roby-v1',
        'nl': 'starting-reason-nl-roby-v1'
    }

    if language not in classifier_names:
        return None

    label = base_intent_spacy(user_input,
                              classifier_names[language],
                              threshold=0.25)

    return label


def intent_smoking_opinion(user_input, language):
    user_input = user_input.lower()

    classifier_names = {
        'en': 'smoking-opinion-en-roby-v1',
        'nl': 'smoking-opinion-nl-roby-v1'
    }

    if language not in classifier_names:
        return None

    label = base_intent_spacy(user_input,
                              classifier_names[language],
                              threshold=0.25)

    return label


def intent_sentiment(user_input, language):
    user_input = user_input.lower()

    classifier_names = {
        'nl': 'sentiment-nl-roby-v1'
    }

    if language not in classifier_names:
        # TODO: LOGGER.warning('There is no classifier for this language')
        return None

    label = base_intent_spacy(user_input,
                              classifier_names[language],
                              threshold=0.4)

    # Note: For this classifier, the default label should be False.
    #       So this function should return True, only when user says "I don't know".
    if label is None or label == 'false':
        label = False

    return label


def intent_is_smoker(user_input, language):
    user_input = user_input.lower().replace('\'', '').replace('-', ' ')

    label = None

    for condition in ['smoker', 'non-smoker']:
        if any(word in user_input.split() for word in IS_SMOKER[language][condition]):
            label = 'yes' if condition == 'smoker' else 'no'

    return label


def intent_is_if_then(user_input, language):
    return bool(re.match(IF_THEN_REG[language], user_input.lower()))
