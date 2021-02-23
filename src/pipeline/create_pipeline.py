import numpy as np
import spacy
from pipeline.pipeline_components.pipe_difficulty import get_difficulty
from pipeline.pipeline_components.pipe_eliminate_duplicates import elim_dup
from pipeline.pipeline_components.pipe_example_phrase import get_example_phrase
from pipeline.pipeline_components.pipe_filter_tokens import filter_tokens
from pipeline.pipeline_components.pipe_keywords import check_keyphrases
from pipeline.pipeline_components.pipe_relative_frequency import relative_freq
from pipeline.pipeline_components.pipe_wordcount import wordcount
from spacy.tokens import Doc, Token


def create_pipeline():
    """creates a spacy pipeline containing all
    steps to extract vocabularies from a text"""

    nlp = spacy.load('en_core_web_lg')

    ## Preprocessing
    # wordcount
    Doc.set_extension('wordcount', default=0, force=True)
    nlp.add_pipe(wordcount)

    # filter tokens
    Doc.set_extension('included_wordcount', default=0, force=True)
    Token.set_extension('is_excluded', default=False, force=True)
    nlp.add_pipe(filter_tokens)

    # eliminate dublicates
    Token.set_extension('appearance', default=np.nan, force=True)
    nlp.add_pipe(elim_dup)

    ## Word difficulty
    # difficulty
    Token.set_extension('difficulty', default=0, force=True)
    nlp.add_pipe(get_difficulty)

    ## Word Relevance
    # relative frequency
    Token.set_extension('relativ_freq', default=np.nan, force=True)
    nlp.add_pipe(relative_freq)

    # keywordscore
    Doc.set_extension('keywords', default=[], force=True)
    Token.set_extension('is_keyword', default=False, force=True)
    Token.set_extension('keyword_score', default=0, force=True)
    nlp.add_pipe(check_keyphrases)

    ## Output
    Token.set_extension("example_phrase", default=[], force=True)
    nlp.add_pipe(get_example_phrase)

    return nlp
