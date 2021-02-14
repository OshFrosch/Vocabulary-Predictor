from gensim.summarization import keywords


def check_keyphrases(doc):
    """extracting keywords out of the text and assigning each token
    a keyword score based on the simalarity"""

    kw = keywords(doc.text, split=True)

    keywords_token = []
    already_in_list = []
    for token in doc:
        if token.text in kw:
            token._.is_keyword = True
            if token.text not in already_in_list:
                keywords_token.append(token)
                already_in_list.append(token.text)
    doc._.keywords = keywords_token

    # assign keyword score
    for token in doc:
        for kw in keywords_token:
            kw_score = token.similarity(kw)
            if kw_score > token._.keyword_score:
                token._.keyword_score = kw_score

    return doc
