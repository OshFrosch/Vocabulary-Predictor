def create_csv_from_df(
    df,
    filename="output/results.csv",
):

    df = df.set_index("word")
    df.to_csv(filename, header=True)
