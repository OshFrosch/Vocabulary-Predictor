from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text


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

    if filepath.endswith(".html"):
        with open(filepath, "rt") as file:
            soup = BeautifulSoup(file.read(), features="html.parser")

        # get text
        for script in soup(["math", "footer"]):
            script.extract()

        # get text
        text = soup.get_text()
        text = text.lower()
        text = text.replace("\n", " ")

        return text

    # TODO
    if (
        filepath.endswith(".jpeg")
        or filepath.endswith(".jpg")
        or filepath.endswith(".png")
    ):
        print("text can not be extracted from images yet")
        return None

    else:
        print("file name does not end with eiter .pdf, .txt, .HTML or .image")
        return None
