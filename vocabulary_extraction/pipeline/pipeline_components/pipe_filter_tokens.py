import logging

logger = logging.getLogger(__name__)


def filter_tokens(doc):
    """
    filters all tokens by stopwords, P-O-S and entities
    :param doc: spaCy Doc
    :return: spaCy Doc
    """

    for token in doc:
        # filter stopwords
        if not token.is_alpha or token.is_stop:
            token._.is_excluded = True

        # filter part-of-speech
        elif token.pos_ not in ["NOUN", "VERB", "ADJ"]:
            token._.is_excluded = True

        # filter entities
        elif token.ent_type != 0:
            token._.is_excluded = True

        # count included words
        else:
            doc._.included_wordcount += 1

    logger.info(f"{doc._.included_wordcount} words in vocabulary")

    return doc
