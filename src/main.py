import argparse
import logging
import pathlib
import sys

from pipeline.create_pipeline import create_pipeline
from utils.input_utils.text_extraction import extract_html, extract_pdf, extract_raw
from utils.output_utils.add_infos_to_df import add_infos_to_df
from utils.output_utils.create_csv_from_df import create_csv_from_df
from utils.output_utils.create_df_from_doc import create_df_from_doc
from utils.output_utils.predict_output_size import predict_outputsize


def main(args):
    logger = logging.getLogger(__name__)
    if args.debug:
        logger.setLevel(logging.INFO)

    if args.raw:
        text = extract_raw(args.input_file_path)
    elif args.html:
        text = extract_html(args.input_file_path)
    elif args.pdf:
        text = extract_pdf(args.input_file_path)

    pipeline = create_pipeline()
    if args.debug:
        logger.info(
            "Executing the following pipeline steps\n{0}.".format(pipeline.pipe_names)
        )

    doc = pipeline(text)
    df = create_df_from_doc(doc)

    if args.all:
        output_size = None
    elif args.interactive:
        output_size = predict_outputsize(df)
    elif args.size:
        output_size = args.size

    df_final = add_infos_to_df(df, limit=output_size)

    if args.to_csv:
        create_csv_from_df(df_final, args.to_csv)
    else:
        create_csv_from_df(df_final, sys.stdout)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="vocabulary-extraction gives you the most relevant vocabulary to learn before reading texts a language that you are not a native speaker of (currently only English is supported). You can use raw text, html or pdf files as input and generate a vocabulary list of the most relevant words. The output is a comma seperated file with the colums `word`, `example sentence` and `Synonyms Definition and Examples`",
        epilog="Save time in reading difficult texts and improve your language skills along the way!",
    )
    input_args = parser.add_argument_group("Input")
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
        "input_file_path",
        metavar="INPUT_FILE_PATH",
        help="Path to input file",
        type=pathlib.Path,
    )

    mode_args = parser.add_argument_group("Mode").add_mutually_exclusive_group(
        required=False
    )
    mode_args.add_argument(
        "-a",
        "--all",
        help="Output is complete vocabulary",
        action="store_true",
        default=True,
    )
    mode_args.add_argument(
        "-s", "--size", help="Specify max. vocabulary size", type=int
    )
    mode_args.add_argument(
        "-i",
        "--interactive",
        help="Determine vocabulary size by interactive feedback",
        action="store_true",
    )

    output_args = parser.add_argument_group("Output")
    output_args.add_argument(
        "--to_csv",
        metavar="FILE_PATH",
        help="Write output to file path instead of STDOUT (optional)",
        type=pathlib.Path,
    )

    parser.add_argument(
        "-v", "--verbose", help="Log extended information", action="store_true"
    )

    args = parser.parse_args()

    main(args)
