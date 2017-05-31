import random

grammar = {
    'sentence': ('sentence', ['noun_phrase', 'verb_phrase']),
    'noun_phrase': ('noun_phrase', ['article', 'noun']),
    'verb_phrase': ('verb_phrase', ['verb', 'noun_phrase']),
    'article': ('article', ['the', 'a']),
    'noun': ('noun', ['man', 'ball', 'woman', 'table']),
    'verb': ('verb', ['hit', 'saw', 'took', 'liked'])
}

print grammar.items()

def rule_lhs(rule):
    return rule[0]

def rule_rhs(rule):
    return rule[1]

def rewrites(category):
    rhs = rule_rhs(grammar[category])
    can_rewrite = any([(x in grammar) for x in rhs])
    return can_rewrite, rhs

def generate(phrase):
    can_rewrite, rewrite_rules = rewrites(phrase)
    #print can_rewrite, rewrite_rules
    if can_rewrite:
        return ' '.join([(generate(x) if x in grammar else random.choice(x)) for x in rewrite_rules])
    else:
        return random.choice(rewrite_rules)

print generate('noun_phrase')
print generate('verb_phrase')
print generate('sentence')
print generate('sentence')
