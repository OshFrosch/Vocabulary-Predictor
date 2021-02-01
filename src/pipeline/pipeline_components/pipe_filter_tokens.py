def filter_tokens(doc):
    """filters all tokens by stopwords, P-O-S and entities"""

    for token in doc:
        # filter stopwords
        if not token.is_alpha or token.is_stop:
            token._.is_excluded = True
        # filter part-of-speech
        elif token.pos_ not in ["NOUN", "VERB", "ADJ"]:  # ADV?
            token._.is_excluded = True
        # filter entities
        elif token.ent_type != 0:
            token._.is_excluded = True

    return doc
