from wordfreq import zipf_frequency

from src.utils.pipeline_utils.syllable_counter import syllable_count


def get_difficulty(doc):
    """sets the token attribute ._.difficulty according to
    its rareness and syllable count"""

    for token in doc:
        if not token._.is_excluded:
            lemma = token.lemma_
            readability = zipf_frequency(lemma, "en")  # score of 1-8
            syl = syllable_count(lemma)
            if syl > 1 and readability != 0:
                readability -= 0  # (syl - 2)/2
            token._.difficulty = round(8 - readability, 2)

    return doc
