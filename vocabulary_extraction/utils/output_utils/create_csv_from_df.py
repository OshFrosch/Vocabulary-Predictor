def create_csv_from_df(df, filename="output/results.csv", sep=","):
    """
    creates a CSV out of a given pandas dataframe
    :param df: pandas dataframe
    :param filename: name of the resulting file
    :param sep: seperator for the CSV
    """
    df = df.set_index("word")
    if sep:
        df.to_csv(filename, header=True, sep=sep)
    else:
        df.to_csv(filename, header=True, sep=",")
