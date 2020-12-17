from src.pipeline.create_pipeline import create_pipeline
from src.utils.output_utils.create_df_from_doc import create_df_from_doc

if __name__ == "__main__":

    with open("data/kafka.txt", "r") as f:
        text = f.read()

    pipeline = create_pipeline()
    print(pipeline.pipe_names)

    doc = pipeline(text)
    df = create_df_from_doc(doc)

    print(df.head(20))
