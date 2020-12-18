import os

from pipeline.create_pipeline import create_pipeline
from utils.output_utils.create_df_from_doc import create_df_from_doc

from src.utils.text_extraction import extract_from_file

if __name__ == "__main__":
    text = extract_from_file("data/kafka.txt")

    pipeline = create_pipeline()
    print(pipeline.pipe_names)

    doc = pipeline(text)
    df = create_df_from_doc(doc)

    print(df.head(20))
