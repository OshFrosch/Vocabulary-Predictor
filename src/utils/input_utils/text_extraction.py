from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text


def extract_raw(filepath: str):
    """
    returns text from raw text file
    :param filepath:
    :return: text as string
    """
    file = open(filepath, "rt")
    text = file.read()
    file.close()
    return text


def extract_html(filepath: str):
    """
    returns text from a html file
    :param filepath:
    :return: text as string
    """
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


def extract_pdf(filepath: str):
    """
    returns text from a PDF file
    :param filepath:
    :return: text as string
    """
    text = extract_text(filepath)
    return text
