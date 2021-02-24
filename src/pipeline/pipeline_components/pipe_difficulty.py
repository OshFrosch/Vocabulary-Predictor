from utils.pipeline_utils.syllable_counter import syllable_count
from wordfreq import zipf_frequency


def syl_weight(n):
    w = 0
    for i in range(n):
        w += 0.5 ** (i + 1)
    return w


def get_difficulty(doc):
    """sets the token attribute ._.difficulty according to
    its rareness and syllable count"""

    for token in doc:
        if not token._.is_excluded:
            lemma = token.lemma_
            difficulty = 8 - zipf_frequency(lemma, "en")  # score of 0-8
            difficulty += syl_weight(syllable_count(lemma))  # now score of 0-9
            token._.difficulty = round(difficulty / 9, 3)  # normalised to 0-1

    return doc
