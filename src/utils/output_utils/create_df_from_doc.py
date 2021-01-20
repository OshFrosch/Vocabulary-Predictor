import pandas as pd


def create_df_from_doc(doc):
    """creates a df with of all included tokens
    with their attributes of the vocabulary list"""

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
                    token._.ranking,
                )
            )
    df = pd.DataFrame(
        data,
        columns=[
            "token",
            "lemma",
            "appearance",
            "difficulty",
            "rel. frequency",
            "ranking",
        ],
    )

    return df.sort_values("ranking", ascending=False)
