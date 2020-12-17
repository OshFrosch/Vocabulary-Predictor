import os

from src.utils.text_extraction import extract_from_file

path = os.path.join(os.path.dirname(__file__))

text = extract_from_file("{0}/testdata/text.txt".format(path))
print(text)

text = extract_from_file("{0}/testdata/Paper_u-net.pdf".format(path))
print(text)

text = extract_from_file("{0}/testdata/image.png".format(path))
print(text)
