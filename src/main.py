from pipeline.create_pipeline import create_pipeline
from utils.input_utils.text_extraction import extract_from_file
from utils.output_utils.create_df_from_doc import create_df_from_doc
from utils.output_utils.predict_output_size import predict_outputsize

if __name__ == "__main__":
    text = extract_from_file("src/data/kafka.txt")

    pipeline = create_pipeline()
    print(pipeline.pipe_names)

    doc = pipeline(text)
    df = create_df_from_doc(doc)
    df = predict_outputsize(df)

    print(df.head(20))
