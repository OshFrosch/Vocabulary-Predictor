import json

import pandas as pd


def evaluate_ranking(reference_df, df_under_test, column="difficulty"):
    reference_df["phrase"] = reference_df["phrase"].astype(str)
    df_under_test["token"] = df_under_test["token"].astype(str)
    df_under_test["token"].str.lower()

    res = pd.merge(
        reference_df, df_under_test, "left", left_on="phrase", right_on="token"
    )

    res["ranking_error"] = (
        abs(res["reference_difficulty"] - res[column]) * res["reference_difficulty"]
    )

    corr = res["reference_difficulty"].corr(res[column], method="pearson")
    drop = (res[(res[column].isnull())]["reference_difficulty"] ** 2).sum() / (
        res[(res[column].isnull())]["reference_difficulty"]
    ).count()

    return res, corr, drop


def get_dropped_histogram(df, column="difficulty"):
    df[(df[column].isnull())]["reference_difficulty"].plot.hist(
        bins=21,
        x="reference difficulty",
        y="amount of dropped words",
        title="dropped words per difficulty bucket",
        figsize=(8, 6),
    )


def get_difficulty_scatter(df, column="difficulty"):
    df[(df[column].notnull())].plot.scatter(
        x="reference_difficulty", y=column, figsize=(8, 6), style="x"
    )
