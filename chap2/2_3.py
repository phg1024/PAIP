import random

grammar = {
    'sentence': ('sentence', [['noun_phrase', 'verb_phrase']]),
    'noun_phrase': ('noun_phrase', [['article', 'noun']]),
    'verb_phrase': ('verb_phrase', [['verb', 'noun_phrase']]),
    'article': ('article', [['the', 'a']]),
    'noun': ('noun', [['man', 'ball', 'woman', 'table']]),
    'verb': ('verb', [['hit', 'saw', 'took', 'liked']])
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

print generate('noun_phrase')
print generate('verb_phrase')
print generate('sentence')
print generate('sentence')
