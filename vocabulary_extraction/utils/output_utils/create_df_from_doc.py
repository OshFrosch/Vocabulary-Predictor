import pandas as pd


def create_df_from_doc(doc):
    """
    creates a df with of all included tokens with their attributes created in the pipeline of the vocabulary list
    :param doc: spaCy Doc from pipeline instance
    :return df: sorted pandas.DataFrame
    """

    data = []
    for token in doc:
        if not token._.is_excluded:
            data.append(
                (
                    token,
                    token.lemma_,
                    token._.appearance,
                    token._.difficulty,
                    token._.relative_freq,
                    token._.keyword_score,
                    token._.example_phrase,
                )
            )

    df = pd.DataFrame(
        data,
        columns=[
            "token",
            "lemma",
            "appearance",
            "difficulty",
            "relative frequency",
            "keyword score",
            "example phrase",
        ],
    )

    df["overall_ranking"] = (
        3 * df["difficulty"] + df["relative frequency"] + df["keyword score"]
    )

    return df.sort_values(by=["overall_ranking"], ascending=False)
