from wordfreq import zipf_frequency

from vocabulary_extraction.utils.pipeline_utils.syllable_counter import syllable_count


def syl_weight(n):
    """
    returns weigth for difficulty based on the syllable count
    :param n: syllable count
    :return: weigth
    """
    w = 0
    for i in range(n):
        w += 0.5 ** (i + 1)
    return w


def get_difficulty(doc):
    """
    sets the token attribute ._.difficulty based on rareness and syllable count
    :param doc: spaCy Doc
    :return: spaCy Doc
    """

    for token in doc:
        if not token._.is_excluded:
            lemma = token.lemma_
            difficulty = 8 - zipf_frequency(lemma, "en")  # score of 0-8
            difficulty += syl_weight(syllable_count(lemma))  # now score of 0-9
            token._.difficulty = round(difficulty / 9, 3)  # normalised to 0-1

    return doc
