def create_csv_from_df(df, filename="output/results.csv", sep=","):
    df = df.set_index("word")
    if sep:
        df.to_csv(filename, header=True, sep=sep)
    else:
        df.to_csv(filename, header=True, sep=",")
