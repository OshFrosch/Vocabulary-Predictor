

def elim_dup(doc):
    """eliminates all duplicates and counts the appearance of the included words"""

    already_appeared = {}

    for token in doc:
        if not token._.is_excluded:
            if token.lemma_ in already_appeared.keys():
                already_appeared[token.lemma_] += 1
                token._.is_excluded = True
            else:
                already_appeared[token.lemma_] = 1

    for token in doc:
        if not token._.is_excluded:
            token._.appearance = already_appeared[token.lemma_]

    return doc