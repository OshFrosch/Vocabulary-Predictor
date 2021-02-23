def create_csv_from_df(df, filename="output/results.csv", limit=100):
    if limit is None:
        df = df[["token", "example phrase"]]
    else:
        df = df[["token", "example phrase"]].head(limit)

    df.to_csv(filename)
