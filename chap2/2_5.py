import random

grammar = {
    'sentence': ('sentence', [('noun_phrase', 'verb_phrase')]),
    'noun_phrase': ('noun_phrase', [['article', 'adj_star', 'noun', 'pp_star'], ['name'], ['pronoun']]),
    'verb_phrase': ('verb_phrase', [['verb', 'noun_phrase', 'pp_star']]),
    'pp_star': ('pp_star', [[''], ['pp', 'pp_star']]),
    'adj_star': ('adj_star', [[''], ['adj', 'adj_star']]),
    'pp': ('pp', [['prep', 'noun_phrase']]),
    'prep': ('prep', [['to', 'in', 'by', 'with', 'on']]),
    'adj': ('adj', [['big', 'little', 'blue', 'green', 'adiabatic']]),
    'article': ('article', [['the', 'a']]),
    'name': ('name', [['Pat', 'Kim', 'Lee', 'Terry', 'Robin']]),
    'noun': ('noun', [['man', 'ball', 'woman', 'table']]),
    'verb': ('verb', [['hit', 'saw', 'took', 'liked']]),
    'pronoun': ('pronoun', [['he', 'she', 'it', 'these', 'those', 'that']])
}

print grammar.items()

def valid_items(a):
    return [x for x in a if x]

def rule_lhs(rule):
    return rule[0]

def rule_rhs(rule):
    return rule[1]

def rewrites(category):
    return rule_rhs(grammar[category])

def generate(phrase):
    rewrite_rules = rewrites(phrase)
    rule = random.choice(rewrite_rules)
    #print 'rule:', rule

    rewritable = any([(x in grammar) for x in rule])
    #print rewritable
    if rewritable:
        return ' '.join(valid_items([(generate(x) if x in grammar else random.choice(x)) for x in rule]))
    else:
        return random.choice(rule)

print 'noun_phrase:', generate('noun_phrase')
print 'verb_phrase:', generate('verb_phrase')
print 'sentence:', generate('sentence')
print 'sentence:', generate('sentence')
