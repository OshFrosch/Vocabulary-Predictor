import os

import spacy
from pipeline.create_pipeline import create_pipeline
from spacy.matcher import PhraseMatcher
from utils.input_utils.text_extraction import extract_from_file
from utils.output_utils.create_df_from_doc import create_df_from_doc

if __name__ == "__main__":
    print(os.getcwd())
    text = extract_from_file("src/data/kafka.txt")

    pipeline = create_pipeline()
    print(pipeline.pipe_names)

    doc = pipeline(text)
    df = create_df_from_doc(doc)

    print(df.head(20))
