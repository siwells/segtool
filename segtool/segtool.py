# coding: utf-8

import pprint
pp = pprint.PrettyPrinter(indent=4)

coefficients = {
    '1':[2.925, 2.797, 3.336, 1.402, 0.0, 4.972, 1.438, 3.087, 1.993, 3.065, 4.101, 2.625, 4.579, 1.449, 2.761, 4.598, 3.428],
    '2':[2.73, 2.745, 2.799, 1.322, 0.0, 3.465, 2.141, 2.78, 2.445, 4.292, 3.555, 2.969, 5.385, 1.192, 3.772, 4.868, 3.157],
    '3':[1.9, 2.028, 2.454, 0.933, 0.0, 4.589, 1.987, 3.121, 2.387, 3.6, 3.389, 2.774, 5.067, 0.858, 2.621, 4.676, 2.752],
    '4':[1.406, 1.815, 1.99, 0.793 , 0.0, 3.01, 2.181, 2.629, 3.147, 4.549, 3.174, 3.074, 5.499, 0.622, 4.045, 5.479, 2.279],
    '5':[1.995, 1.854, 2.578, 0.533, 0.0, 2.893, 1.103, 2.373, 3.049, 4.252, 3.458, 1.841, 5.367, 0.846, 4.151, 4.806, 2.688],
    '6':[0.0, 0.0, 0.0, 0.0, 2.344, 3.83, 1.074, 2.9, 1.831, 4.113, 3.141, 1.995, 3.843, 1.777, 1.91, 4.45, 3.123],
    '7':[0.0, 0.0, 0.0, 0.0, 1.079, 4.977, 0.727, 3.318, 1.796, 2.94, 2.707, 2.603, 4.341, 1.613, 1.555, 4.637, 3.026],
    '8':[0.0, 0.0, 0.0, 0.0, 1.322, 3.223, 1.187, 2.568, 2.631, 4.437, 2.787, 2.424, 4.39, 1.71, 2.637, 4.834, 2.549]
    }

constants = {
    '1': 82.797,
    '2': 85.85,
    '3': 70.394,
    '4': 77.747,
    '5': 70.288,
    '6': 57.12,
    '7': 56.903,
    '8': 61.695
    }

descriptions = {
    '1': {
        'title': 'Devoted Drivers',
        'description': 'You prefer to use a car than any other mode of transport and you are not interested in reducing your car use. You do not believe there are realistic alternatives to most of the journeys you make and you do not see yourself as a bus user or a cyclist anyway. Other modes are too slow and often stressful with few, if any, advantages over the car. It has probably been a while since you have been on a bus or a bike and you use a car most days. You tend to think successful people use cars and driving is a way to express yourself. You are not particularly motivated by using your travel time to get fit by using the bike or walking, and you are also not particularly motivated by reducing your emissions of greenhouse gases. You believe that people should be able to use their cars as much as they like with little restriction on this and you would like to see more roads built to reduce congestion.'
        },
     '2': {
        'title': 'Image Improvers',
        'description': 'You like to drive and consequently you do not want your ability to drive to be restricted, but you also recognize that it would be good for the planet if we all reduced our car use a little. The main reason you do not want to reduce your car use is largely practical but you also feel that car driving is part of who you are and your identity. You do not relate to bus users but you are likely to see cycling as a form of self-expression and have been interested and committed to keeping slim and fit. You are also likely to think you should walk more and leave the car at home but everything takes so much longer when you walk. You are not entirely convinced about the scientific evidence on global warming and your motivation to act is not high, but at the same time you want to do the right thing.'
     },
     '3': {
        'title': 'Malcontented Motorists',
        'description': 'You drive a lot but find it increasingly stressful. You want to cut down your car use but find that there are a lot of practical problems and issues with using alternative modes. For instance, you are likely to feel that bus provision in your area is inadequate or would take too long to do all you need to do. Although you can see that it might be beneficial to your health, cycling is not something you feel comfortable doing. You walk sometimes, but only when it is more convenient than driving and for practical rather than fitness reasons. You might make more effort to walk more in the future though. Environmental issues are something you are aware of and know a little bit about, but you do not feel it is practical to make decisions about your travel based on these issues.'
     },
     '4': {
        'title': 'Active Inspirers',
        'description': 'You feel that you drive more than you should and you would like to cut down. You feel particularly guilty when you use your car on short journeys. But you do not see the bus as a solution - even though it can sometimes be quicker - because it is not always practical for carrying things or travelling with children. Your most preferred alternatives are walking and cycling. You walk a lot already because it is healthy and you enjoy it and are likely to try and fit it into your daily routine as much as possible. Cycling is also something you already do or consider to offer freedom, speed and fitness. You are likely to be motivated by environmental issues and this gives you some extra impetus to leave the car at home when you can.'
     },
     '5': {
        'title': 'Practical Travellers',
        'description': 'You regard the car merely as a practical means of getting from A-B and largely use it only when necessary. But you also see other modes as equally or more practical in certain circumstances. You walk and/or cycle a lot as you believe these modes can often be superior to the car in terms of speed, cost and general convenience. The bus, however, is something you feel is often inferior because of the time penalty it involves. You do not tend to walk or cycle specifically because it helps you to be fitter, but fitness is important to you and you are likely to be fit already. You would not change much about how you currently travel as you feel you are already making optimum choices given your commitments and what you have available to you.'
     },
     '6': {
        'title': 'Car Contemplators',
        'description': 'You do not have a car at the moment but would like one at some point in the not so distant future. You are likely to not be able to afford a car at the moment or acknowledge that it would be a hassle or an unnecessary drain on your resources in your current circumstances. However, you aspire to own a car as you believe it is a sign of being successful and will provide much desired independence and freedom. Cycling is not something you want to do more of and you believe it is a rather impractical and stressful mode. You see walking as practical sometimes, good for fitness and something you intend to do more of, but generally limited as a mode of transport. You see even more problems with using the bus and whilst you might use it a lot at the moment, you would like to use the car more.'
     },
     '7': {
        'title': 'PT Dependents',
        'description': 'Although you are not against cars in any way and think people should be allowed to use them freely, you don\'t like driving very much. You are frustrated, though, that you do not get to travel by car a bit more often as you are fed up with the bus being slow so much of time, particularly when it gets caught up in congestion. You do not see yourself as a cyclist, but you don\'t mind walking and would like to do more of it, particularly for fitness. You have very little interest in environmental issues and do not think they concern you very much, although local pollution and congestion is a concern.'
     },
     '8': {
        'title': 'Car-Free Choosers',
        'description': 'You are not keen on driving and believe that cars and their impacts are something that need to be urgently addressed. You are committed to using other more healthy modes of transport instead. You can see benefits of travelling by walking, cycling and using the bus. If you take the bus you find it enjoyable and relaxing. If you walk you see it as healthy and would like do more of it. If you cycle, you like the sense of freedom it gives you and feel it says something about who you are and how you feel about protecting the environment.'
     }

    }

num_segments = len(coefficients)
num_coefficients = len(coefficients['1'])

def allocate_segment(car=False, segments=None):
    """
    Takes 2 inputs, a boolean value, 'car', and a segments dict, 
    e.g. segments = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}


    Returns the allocated segment, e.g the maximal value for the segments 
    dict, split on keys 1-5 for car=True and 6-8 for car=False.
    """   
    segment_allocation = 0
    keys = []

    if car is True:
        keys = ['1', '2', '3' ,'4', '5']
    else:
        keys = ['6', '7', '8']

    d = dict([(i, segments[i]) for i in keys if i in segments])
    segment_allocation = key_with_max_val( d )

    return segment_allocation


def calculate_segment(answers):
    """
    Takes a list of answers, e.g. [1, 1, 1, 1, ...]. 
    Each element of answers is a value between 1 & 5.

    Returns a segments dict containing the calculated 
    value for each segment based upon the supplied answers.
    """
    if len(answers) != num_coefficients:
        raise ValueError("The number of answers must be equal to the number of questions in the questionnaire")

    segments = {str(k):0 for k in range(1,9)}
    
    for segment in range(1, num_segments+1):
        segment = str(segment)

        for idx in range(num_coefficients):
            tmp = answers[idx] * coefficients[segment][idx]
            segments[segment] += tmp

        segments[segment] = segments[segment] - constants[segment]
    
    return segments


def get_segment(car, answers):
    """
    Helper function to combine usage of calculate_segment and allocate_segment into a single call
    """
    return allocate_segment(car, calculate_segment(answers) )


def get_segment_title(segment):
    """
    Return the title associated with the supplied segment
    """
    try:
        return descriptions[str(segment)]['title']
    except KeyError:
        return None


def get_segment_description(segment):
    """
    Return the description associated with the supplied segment
    """
    try:
        return descriptions[str(segment)]['description']
    except KeyError:
        return None


def key_with_max_val(d):
     """ 
     Create a list of keys and a list of values for the input dict.
     Get the list-index of the max value

     Return the key from the same list-index in the key list
     """  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]


if __name__ == "__main__":
    print "SEGTOOL"

    seg = get_segment(True, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) # Should return 3
    #print get_segment_title(seg)
    #print get_segment_description(seg)

    try:
        print calculate_segment([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) #GOOD
        print calculate_segment([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) #BAD
    except ValueError as e:
        print e

