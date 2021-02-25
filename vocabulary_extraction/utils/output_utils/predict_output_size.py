def predict_outputsize(df):
    """
    Takes all ranked vocabularies and tries to predict the volume the user doesn't know by asking questions
    :param df: vocabulary df
    :return: reduced set of vocabulary df
    """

    def user_knows_vocab(s):
        response = input(f"Can you translate this word:   {s}   [y/n]  ")

        while response not in ["y", "n"]:
            response = input(
                "Unexpected input. Try again.\n"
                + f"Can you translate this word:   {s}   [y/n]  "
            )
        return response == "y"

    n = len(df)
    dict_word_known = {}
    result = False

    i = 1
    loc = 0
    offset = 0
    last = True
    last_loc = 0
    while loc <= n:

        print(f"Word position {loc}:")
        if loc in dict_word_known:
            result = dict_word_known[loc]
        else:
            result = user_knows_vocab(df.iloc[loc]["lemma"])
            dict_word_known[loc] = result

        if result:
            if last:
                break
            last = True
            offset = last_loc
            i = 0
        else:
            last = False

        i += 1
        last_loc = loc
        loc = (2 ** i) - 1 + offset

    return last_loc - 1
