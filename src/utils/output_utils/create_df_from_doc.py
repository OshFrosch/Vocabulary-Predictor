import pandas as pd


def create_df_from_doc(doc):
    data = []
    for token in doc:
        if not token._.is_excluded:
            data.append((token, token.lemma_, token._.appearance, token._.difficulty, token._.relative_freq))
    df = pd.DataFrame(data, columns=['token', 'lemma', 'appearance', 'difficulty', 'relative frequency'])

    return df
