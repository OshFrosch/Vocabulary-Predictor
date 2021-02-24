import logging

logger = logging.getLogger(__name__)


def elim_dup(doc):
    """eliminates all duplicates and counts the appearance of the included words"""

    already_appeared = {}

    for token in doc:
        if not token._.is_excluded:
            if token.lemma_ in already_appeared.keys():
                already_appeared[token.lemma_]._.appearance += 1
                token._.is_excluded = True
                doc._.included_wordcount -= 1
            else:
                token._.appearance = 1
                already_appeared[token.lemma_] = token

    logger.info(f"{doc._.included_wordcount} words in vocabulary without duplicates")

    return doc
