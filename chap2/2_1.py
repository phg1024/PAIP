import random

def valid_items(a):
    return [x for x in a if x]

def sentence():
    return ' '.join(valid_items([noun_phrase(), verb_phrase()]))

def noun_phrase():
    return ' '.join(valid_items([article(), adj_star(), noun(), pp_star()]))

def verb_phrase():
    return ' '.join(valid_items([verb(), noun_phrase()]))

def article():
    return random.choice(['the', 'a'])

def noun():
    return random.choice(['man', 'ball', 'woman', 'table'])

def verb():
    return random.choice(['hit', 'took', 'saw', 'liked'])

def adj():
    return random.choice(['big', 'little', 'blue', 'green', 'adiabatic'])

def prep():
    return random.choice(['to', 'in', 'by', 'with', 'on'])

def pp():
    return ' '.join(valid_items([prep(), noun_phrase()]))

def adj_star():
    if random.choice([0, 1]) == 0:
        return ''
    else:
        return ' '.join(valid_items([adj(), adj_star()]))

def pp_star():
    if random.choice([0, 1]) == 0:
        return ''
    else:
        return ' '.join(valid_items([pp(), pp_star()]))

for i in range(5):
    print i, sentence()
