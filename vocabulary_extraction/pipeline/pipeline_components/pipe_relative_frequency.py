from wordfreq import word_frequency

from vocabulary_extraction.utils import tf_values, total_tf_values
from vocabulary_extraction.utils.util_classes.Maximum import Maximum
from vocabulary_extraction.utils.util_classes.Minimum import Minimum


def relative_freq(doc):
    """
    calculating the  frequency of a included word relative to the frequency in the english language
    :param doc: spaCy Doc
    :return: spaCy Doc
    """

    calculate_last = []
    min_freq = Minimum(1)
    max_score = Maximum(0)

    def calc_rel_freq(word_freq, token):
        return round(((token._.appearance / doc._.wordcount) ** 2) / word_freq, 3)

    for token in doc:
        if not token._.is_excluded:
            overall_word_freq = word_frequency(token.lemma_, "en")

            if overall_word_freq == 0:
                calculate_last.append(token)
            else:
                min_freq.update_minimum(overall_word_freq)
                token._.relative_freq = calc_rel_freq(overall_word_freq, token)
                max_score.update_maximum(token._.relative_freq)

    for token in calculate_last:
        token._.relative_freq = calc_rel_freq(min_freq.value, token)
        max_score.update_maximum(token._.relative_freq)

    for token in doc:
        if not token._.is_excluded:
            token._.relative_freq /= max_score.value

    return doc
