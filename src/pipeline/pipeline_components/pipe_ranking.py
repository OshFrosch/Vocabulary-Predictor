def get_ranking(doc):
    """calculating the overall raking every vocabualry element"""

    # calculate maximun for frequency
    maximum_frequency = 0
    for token in doc:
        if not token._.is_excluded:
            if token._.relative_freq > maximum_frequency:
                maximum_frequency = token._.relative_freq

    # add ranking to each non-excluded token based on weights for difficulty and rel_frequency
    for token in doc:
        if not token._.is_excluded:
            if maximum_frequency != 0:
                # weights
                weight_rel_frequency = 1 / maximum_frequency
                weight_difficulty = 0.125  # max value for difficulty is 8
                ranking = (
                    weight_rel_frequency * token._.relative_freq
                    + weight_difficulty * token._.difficulty
                )
            token._.ranking = ranking
    return doc
