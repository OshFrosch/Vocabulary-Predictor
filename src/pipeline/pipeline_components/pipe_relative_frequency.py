from wordfreq import word_frequency


def relative_freq(doc):
    """calculating the relativ frequency of a included word"""

    maw = 20  # maximal appearance weight

    for token in doc:
        if not token._.is_excluded:
            text_freq = min(maw, token._.appearance) / doc._.wordcount
            overall_freq = word_frequency(token.lemma_, "en")
            if overall_freq != 0:
                token._.relative_freq = text_freq ** 2 / overall_freq

    return doc
