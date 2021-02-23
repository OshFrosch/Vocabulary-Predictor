import argparse
import pathlib

from pipeline.create_pipeline import create_pipeline
from utils.input_utils.text_extraction import extract_html, extract_pdf, extract_raw
from utils.output_utils.create_df_from_doc import create_df_from_doc
from utils.output_utils.predict_output_size import predict_outputsize

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    input_args = parser.add_argument_group("Input arguments")
    input_type_args = input_args.add_mutually_exclusive_group(required=False)

    input_type_args.add_argument(
        "--raw",
        help="Input file is raw text (default)",
        action="store_true",
        default=True,
    )
    input_type_args.add_argument(
        "--html", help="Input file is HTML (e.g. arXMLiv document)", action="store_true"
    )
    input_type_args.add_argument("--pdf", help="Input file is PDF", action="store_true")
    input_args.add_argument(
        "input_file_path", help="Path to input file", type=pathlib.Path
    )

    output_args = parser.add_argument_group("Output arguments")
    output_args.add_argument(
        "--to_csv",
        metavar="file_path",
        help="Export as CSV file (optional)",
        type=pathlib.Path,
    )
    output_args.add_argument(
        "--to_excel",
        metavar="file_path",
        help="Export as Excel file (optional)",
        type=pathlib.Path,
    )

    args = parser.parse_args()

    if args.raw:
        text = extract_raw(args.input_file_path)
    elif args.html:
        text = extract_html(args.input_file_path)
    elif args.pdf:
        text = extract_pdf(args.input_file_path)

    pipeline = create_pipeline()
    print("Executing the following pipeline steps\n{0}.".format(pipeline.pipe_names))

    doc = pipeline(text)
    df = create_df_from_doc(doc)
    df = predict_outputsize(df)

    if args.to_csv:
        df.to_csv(args.to_csv, index=False)
    elif args.to_excel:
        df.to_excel(args.to_excel, index=False)
