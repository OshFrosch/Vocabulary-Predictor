from pdfminer.high_level import extract_text


def extract_from_file(filepath):
    """
    returns text from a given file (PDF or txt)
    :param file: input-file
    :return: text as string
    """

    # TODO: if file is PDF
    if True:
        text = extract_text(filepath)

    # TODO: if file is txt, extract text from txt file
    # TODO: add additional file types like images

    return text
