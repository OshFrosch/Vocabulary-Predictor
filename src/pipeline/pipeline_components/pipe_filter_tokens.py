from src.utils.pipeline_utils.get_entities import get_entities


def filter_tokens(doc):
    """filters all tokens"""

    entities = get_entities(doc)

    for token in doc:
        # filter stopwords
        if not token.is_alpha or token.is_stop:
            token._.is_excluded = True
        # filter part-of-speech
        if token.pos_ not in ['NOUN', 'VERB', 'ADJ', 'ADV']:  # ADV?
            token._.is_excluded = True
        # filter entities
        if token.text in entities:
            token._.is_excluded = True

    return doc