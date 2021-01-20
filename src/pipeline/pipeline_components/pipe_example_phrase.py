import spacy
from spacy.matcher import PhraseMatcher


def get_example_phrase(doc):
    """providing an example sentence for every vocab"""

    nlp = spacy.load(
        "en_core_web_lg"
    )  # TODO: can this be used from the create_pipeline.py file?

    for token in doc:
        if not token._.is_excluded:

            pattern = token.text
            phrase_matcher = PhraseMatcher(nlp.vocab)
            phrase_matcher.add(pattern, None, nlp(pattern))

            # go through all sentences and add sentences including the word to the token attribute 'example_phrase'
            for sent in doc.sents:
                for match_id, start, end in phrase_matcher(nlp(sent.text)):
                    if nlp.vocab.strings[match_id] in [pattern]:
                        token._.example_phase.append(sent.text)
                        # TODO: ranking for sentences

            """
            # More efficient approach, just go through doc once
            # create token-dict
            for sent in doc.sents:
                # calculate sentence-ranking
                sentence_difficulty = 0
                for token in sent:
                    if not token._.is_excluded:
                        sentence_difficulty += token._.difficulty
                        # add to token-dict with sentence and sentence-ranking
                        pass
                    elif token.text in token-dict:
                        # add sentence and sentence-ranking to token-dict
                        pass
            """
    return doc
