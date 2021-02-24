import json
import os
import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import spacy
from bs4 import BeautifulSoup

from vocabulary_extraction.pipeline.create_pipeline import create_pipeline
from vocabulary_extraction.utils.input_utils.text_extraction import extract_from_file
from vocabulary_extraction.utils.output_utils.create_df_from_doc import (
    create_df_from_doc,
)

nlp = spacy.load("en_core_web_lg")


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
    plot_df = df[(df[column].notnull())].copy()
    plot_df["color"] = np.where(plot_df[column] == 8, "Red", "DarkBlue")

    plot_df.plot.scatter(
        x="reference_difficulty", y=column, c="color", figsize=(8, 6), style="x"
    )


def get_keywords(path):

    with open(path, "rt") as file:
        keywords = []
        soup = BeautifulSoup(file.read(), features="html.parser")
        keyword_tag = soup.find("meta", attrs={"name": "keywords"})
        if keyword_tag:
            doc = nlp(keyword_tag["content"].lower().replace("\n", " "))

            for token in doc:
                if not token.is_punct:
                    keywords.append(token.text)

    return keywords


def get_keyword_results(path):
    keywords = get_keywords(path)

    if len(keywords) > 0:
        pipeline = create_pipeline()
        text = extract_from_file(path)
        doc = pipeline(text)
        df = create_df_from_doc(doc)

        return df[df["token"].astype("string").isin(keywords)]
    return None


def plot_relevancy(df):
    relevancy = df.loc[:, "keyword score"]
    plt.scatter(relevancy.index, relevancy)
    plt.show()


def get_mean_relevancy(df):
    relevancy = df.loc[:, "keyword score"]
    return relevancy.mean()


def get_all_files(basepath):
    files = []
    directories = []

    for r, d, f in os.walk(basepath, followlinks=True):

        for directory in d:
            directories.append(os.path.join(r, directory))
        for file in f:
            if ".html" in file:
                files.append(os.path.join(r, file))

    return files


def process_keywords(files, amount_of_docs, SEED=43):
    docs = 0
    random.seed(SEED)
    result_dfs = []

    while docs < amount_of_docs:
        try:
            filepath = random.sample(files, 1)[0]
        except ValueError:
            break

        df = get_keyword_results(filepath)

        if df is not None:
            docs += 1
            result_dfs.append(df)

    merged = pd.concat(result_dfs).reset_index()
    return merged
