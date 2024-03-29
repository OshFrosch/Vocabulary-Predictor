from yake import KeywordExtractor


def check_keyphrases(doc):
    """
    extracting keywords out of the text and assigning a keyword score with YAKE!
    :param doc: spaCy Doc
    :return: spaCy Doc
    """

    kw_extractor = KeywordExtractor(lan="en", n=1, top=500)
    kw = dict(kw_extractor.extract_keywords(doc.text))

    for token in doc:
        if not token._.is_excluded:
            if token.lemma_ in kw.keys():
                token._.keyword_score = 1 - kw[token.lemma_]

    return doc
