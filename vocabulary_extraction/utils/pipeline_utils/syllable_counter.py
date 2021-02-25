from nltk.corpus import cmudict

phoneme_dict = dict(cmudict.entries())


def syllable_count(word):
    """
    function that counts a syllable in a word if found in dict
    :param word: string
    :return: number of syllables of the word
    """

    if word not in phoneme_dict:
        return 0
    syllables = phoneme_dict[word]
    count = len([syllable for syllable in syllables if syllable[-1].isdigit()])

    return count
