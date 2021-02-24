from yake import KeywordExtractor


def check_keyphrases(doc):
    """extracting keywords out of the text and assigning each token
    a keyword score based on the simalarity"""

    kw_extractor = KeywordExtractor(lan="en", n=1, top=500)
    kw = dict(kw_extractor.extract_keywords(doc.text))

    keywords_token = []
    already_in_list = []
    for token in doc:
        if not token._.is_excluded:
            if token.lemma_ in kw.keys():
                token._.keyword_score = 1 - kw[token.lemma_]

    return doc
