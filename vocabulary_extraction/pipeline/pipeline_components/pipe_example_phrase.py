def get_example_phrase(doc):
    """
    providing an example sentence from the doc for every vocab
    :param doc: spaCy Doc
    :return: spaCy Doc
    """

    token_sentences = {}
    for sentence in doc.sents:

        sentence_difficulty = calculate_sentence_ranking(sentence)

        for token in sentence:
            if not token._.is_excluded:
                token_sentences[token.text] = [(sentence.text, sentence_difficulty)]
            elif token.text in token_sentences:
                token_sentences[token.text].append((sentence.text, sentence_difficulty))

    for token in doc:
        if not token._.is_excluded:
            phrases = token_sentences[token.text]
            best_phrase = min(phrases, key=lambda item: (item[1]))[0]
            token._.example_phrase = best_phrase

    return doc


def calculate_sentence_ranking(sentence):
    """
    The ranking consits of the cumulated difficulty of non-excluded vocab words in the sentence
    :param sentence: sentence from spacy doc
    :return: sentence_difficulty
    """
    sentence_difficulty = 0
    for token in sentence:
        if not token._.is_excluded:
            sentence_difficulty += token._.difficulty
    return sentence_difficulty
