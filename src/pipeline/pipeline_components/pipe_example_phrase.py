def get_example_phrase(doc):
    """providing an example sentence for every vocab"""

    for token in doc:
        if not token._.is_excluded:
            token._.example_phase = "example"
    return doc
