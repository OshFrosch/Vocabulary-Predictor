import numpy as np
import spacy
from spacy.tokens import Doc, Token

from src.pipeline.pipeline_components.pipe_difficulty import get_difficulty
from src.pipeline.pipeline_components.pipe_eliminate_duplicates import elim_dup
from src.pipeline.pipeline_components.pipe_filter_tokens import filter_tokens
from src.pipeline.pipeline_components.pipe_relative_frequency import relative_freq
from src.pipeline.pipeline_components.pipe_wordcount import wordcount


def create_pipeline():
    nlp = spacy.load("en_core_web_sm", disable=["parser"])

    Doc.set_extension("wordcount", default=0, force=True)
    nlp.add_pipe(wordcount)

    Token.set_extension("is_excluded", default=False, force=True)
    nlp.add_pipe(filter_tokens)

    Token.set_extension("appearance", default=np.nan, force=True)
    nlp.add_pipe(elim_dup)

    Token.set_extension("relative_freq", default=np.nan, force=True)
    nlp.add_pipe(relative_freq)

    Token.set_extension("difficulty", default=0, force=True)
    nlp.add_pipe(get_difficulty)

    return nlp
