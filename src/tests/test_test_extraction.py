from src.utils.text_extraction import extract_from_file

text = extract_from_file("testdata/text.txt")
print(text)

text = extract_from_file("testdata/Paper_u-net.pdf")
print(text)

text = extract_from_file("testdata/image.png")
print(text)