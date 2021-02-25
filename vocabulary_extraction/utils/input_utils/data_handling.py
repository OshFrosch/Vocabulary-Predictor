import os
import random

from vocabulary_extraction.utils.input_utils.text_extraction import extract_from_file


def preprocess_html_files(number: int, input: str, output: str):
    """
    Passes html-files from the input directory
    to the extract_from_file-function and stores
    the result in the output directory

    Args:
        number (integer): number of documents to process
        input (str): absolute path to the input directory
        output (str): absolute path to the output directory
    """

    files = []
    directories = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(input, followlinks=True):

        for directory in d:
            directories.append(os.path.join(r, directory))
        for file in f:
            if ".html" in file:
                files.append(os.path.join(r, file))

    SEED = 42
    random.seed(SEED)
    chosen_files = random.sample(files, number)

    if not os.path.exists(output):
        os.makedirs(output)

    new_ending = ".txt"
    for file in chosen_files:
        filename = os.path.split(file)[1]
        new_path = os.path.join(output, filename + new_ending)
        text_file = open(new_path, "w")
        text_file.write(extract_from_file(file))
        text_file.close()

    return


if __name__ == "__main__":
    raw = os.path.abspath("../../data/no_problem/")
    data = os.path.abspath("../../data/text_files/")
    preprocess_html_files(number=1000, input=raw, output=data)
