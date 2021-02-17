import json

import pandas as pd


def evaluate_ranking(reference_df, df_under_test):
    reference_df["phrase"] = reference_df["phrase"].astype(str)
    df_under_test["token"] = df_under_test["token"].astype(str)
    df_under_test["token"].str.lower()

    res = pd.merge(
        reference_df, df_under_test, "left", left_on="phrase", right_on="token"
    )

    res["ranking_error"] = (
        abs(res["reference_difficulty"] - res["ranking"]) * res["reference_difficulty"]
    )

    corr = res["reference_difficulty"].corr(res["ranking"], method="pearson")
    drop = (res[(res["ranking"].isnull())]["reference_difficulty"] ** 2).sum() / (
        res[(res["ranking"].isnull())]["reference_difficulty"]
    ).count()

    return res, corr, drop


def get_dropped_histogram(df):
    df[(df["ranking"].isnull())]["reference_difficulty"].plot.hist(
        bins=21,
        x="reference difficulty",
        y="amount of dropped words",
        title="dropped words per difficulty bucket",
        figsize=(8, 6),
    )


def get_difficulty_scatter(df):
    df[(df["ranking"].notnull())].plot.scatter(
        x="reference_difficulty", y="ranking", figsize=(8, 6), style="x"
    )
