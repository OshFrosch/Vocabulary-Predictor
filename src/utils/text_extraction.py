from pdfminer.high_level import extract_text
import cv2
import pytesseract


def extract_from_file(filepath: str):
    """
    returns text from a given file (txt, PDF, HTML, image)
    :param filepath:
    :return: text as string
    """

    # txt-file
    if filepath.endswith(".txt"):
        file = open(filepath, "rt")
        text = file.read()
        file.close()
        return text

    # PDF-file
    if filepath.endswith(".pdf"):
        text = extract_text(filepath)
        return text

    # TODO: extract text from HTML file

    # TODO
    if filepath.endswith(".jpeg") or filepath.endswith(".jpg") or filepath.endswith(".png"):
        print("text can not be extracted from images yet")
        return None

    else:
        print("file name does not end with eiter .pdf, .txt, .HTML or .image")
        return None
