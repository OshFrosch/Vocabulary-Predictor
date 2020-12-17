from pdfminer.high_level import extract_text


def extract_from_file(filepath):
    """
    returns text from a given file (PDF or txt)
    :param file: input-file
    :return: text as string
    """

    # PDF-file
    if filepath.endswith(".pdf"):
        text = extract_text(filepath)
        return text

    # txt-file
    if filepath.endswith(".txt"):
        file = open(filepath, "rt")
        text = file.read()
        file.close()
        return text


    # TODO: if file is txt, extract text from txt file
    # TODO: add additional file types like images

    else:
        print("file name does not end with eiter .pdf, .txt, .HTML or .image")
        return None
