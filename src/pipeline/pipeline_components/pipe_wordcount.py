

def wordcount(doc):
    """gives an overall word count"""

    word_count: int = 0

    for token in doc:
        if token.is_alpha:
            word_count += 1

    doc._.wordcount = word_count

    print(f'{word_count} overall words')

    return doc