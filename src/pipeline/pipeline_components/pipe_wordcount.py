import logging

logger = logging.getLogger(__name__)


def wordcount(doc):
    """gives an overall word count"""

    for token in doc:
        if token.is_alpha:
            doc._.wordcount += 1

    logger.info(f"{doc._.wordcount} words in document")

    return doc
