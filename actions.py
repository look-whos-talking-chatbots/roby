"""
File contains the generic and custom action functions for roby bots.
"""


def append_quitting_reason(user):
    try:
        variable = user['params']['quitting']['reasons']['last']
    except:
        variable = None

    try:
        variable_list = user['params']['quitting']['reasons']['list']
    except:
        variable_list = []

    if variable is not None and variable not in variable_list:
        variable_list.append(variable)

    return variable_list


def count_quitting_reason(user):
    count = 0

    try:
        count = len(user['params']['quitting']['reasons']['list'])
    except:
        pass

    return count


def process_norm_answer(user):
    user_answer = None
    actual_smokers = 5  # Default to prevent crash

    try:
        user_estimate = user['params']['norm']['user']['estimate']
        user_age = user['age']

        if user_age <= 20:
            actual_smokers = 21.2
        elif 20 < user_age <= 25:
            actual_smokers = 24
        elif 25 < user_age <= 30:
            actual_smokers = 27.2
        elif 30 < user_age <= 35:
            actual_smokers = 21.7
        elif 35 < user_age <= 40:
            actual_smokers = 29.4
        elif 40 < user_age <= 45:
            actual_smokers = 26.4
        elif 45 < user_age <= 50:
            actual_smokers = 20.4
        elif 50 < user_age:
            actual_smokers = 21.6

        if actual_smokers + 5 < user_estimate:
            user_answer = 'over-estimate'
        elif user_estimate < actual_smokers - 5:
            user_answer = 'under-estimate'
        else:
            user_answer = 'correct'
    except:
        pass

    return user_answer


def is_longer_1day(user):
    is_longer = None

    try:
        duration_number = user['params']['stoppedBefore']['stopDuration']['number']
    except:
        duration_number = None

    try:
        duration_str = user['params']['stoppedBefore']['stopDuration']['frequency']
        is_longer = not any(word in duration_str.split() for word in ['hours', 'hour', 'hrs', 'hr'])
        if is_longer and any(word in duration_str.split() for word in ['day', 'dy']) and type(duration_number) == int:
            is_longer = duration_number > 1
    except:
        pass

    return is_longer


def calculate_nicotine_dependency(user):
    nic_dep_score = 0
    nicotine_dependency = ''

    try:
        # The question: How soon after waking up do you smoke your first cigarette?
        # results:      a) Within 5 minutes = 3 | b) 6-30 minutes = 2
        #               c) 31-60 minutes = 1    | d) After 60 minutes = 0
        first_cigarette = user['params']['smoking']['firstcig']
        if first_cigarette == 'a':
            nic_dep_score += 3
        elif first_cigarette == 'b':
            nic_dep_score += 2
        elif first_cigarette == 'c':
            nic_dep_score += 1
    except:
        pass

    try:
        # The question: Is the first smoke in the morning the one that you would most hate to give up?
        # results:      yes = 1 | no = 0
        if user['params']['smoking']['mosthard'] == 'yes':
            nic_dep_score += 1
    except:
        pass

    try:
        # The question: Do you smoke more during the first hours after waking up?
        # results:      yes = 1 | no = 0
        if user['params']['smoking']['moreAfterWaking'] == 'yes':
            nic_dep_score += 1
    except:
        pass

    try:
        # The question: Do you find it difficult to not smoke in places where you're not allowed to?
        # results:      yes = 1 | no = 0
        if user['params']['smoking']['prohibitedPlaces'] == 'yes':
            nic_dep_score += 1
    except:
        pass

    try:
        # The question: Do you smoke if you are so ill that you spend most of the day in bed?
        # results:      yes = 1 | no = 0
        if user['params']['smoking']['whenIll'] == 'yes':
            nic_dep_score += 1
    except:
        pass

    # Cigarette number calculation with taking different the unit and frequency mentions into account
    cigarette_number = None
    try:
        cigarette_number = user['params']['smoking']['perDay']['number']
    except:
        pass

    if cigarette_number is not None:
        try:
            cigarette_unit = user['params']['smoking']['perDay']['unit']
            if cigarette_unit is not None:
                if 'box' in cigarette_unit or 'pack' in cigarette_unit:
                    cigarette_number *= 20
                elif 'carton' in cigarette_unit:
                    cigarette_number *= 200
        except:
            pass

        try:
            cigarette_frequency = user['params']['smoking']['perDay']['frequency']
            if cigarette_frequency is not None:
                if 'week' in cigarette_frequency:
                    cigarette_number /= 7
                elif 'month' in cigarette_frequency:
                    cigarette_number /= 30
                elif 'year' in cigarette_frequency:
                    cigarette_number /= 365
        except:
            pass

    # The question: How many cigarette/day do you smoke?
    # results:      10 or less = 0 | 11-20 = 1 | 21-30 = 2 | 31 or more = 3
    if cigarette_number is not None:
        if 11 <= cigarette_number <= 20:
            nic_dep_score += 1
        elif 21 <= cigarette_number <= 30:
            nic_dep_score += 2
        elif 31 <= cigarette_number:
            nic_dep_score += 3

    if nic_dep_score < 2:
        nicotine_dependency = "low-dependence"
    elif 2 < nic_dep_score <= 7:
        nicotine_dependency = "moderate"
    elif 8 <= nic_dep_score:
        nicotine_dependency = "high"

    return nicotine_dependency
