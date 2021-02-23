def create_csv_from_df(df, filename="output/results.csv", limit=50):
    df = df[["token", "example phrase"]].head(limit)
    df.columns = ["word", "example sentence"]
    df = df.set_index("word")
    df.to_csv(filename, header=False)
