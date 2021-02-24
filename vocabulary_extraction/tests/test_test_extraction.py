import os

from vocabulary_extraction.utils.input_utils.text_extraction import (
    extract_html,
    extract_pdf,
    extract_raw,
)

path = os.path.join(os.path.dirname(__file__))

text = extract_raw("{0}/testdata/text.txt".format(path))
print(text)

text = extract_pdf("{0}/testdata/Paper_u-net.pdf".format(path))
print(text)

text = extract_html("{0}/testdata/astro-ph0001007.html".format(path))
print(text)
