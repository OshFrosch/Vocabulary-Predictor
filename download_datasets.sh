#!/bin/sh

python -m nltk.downloader cmudict
python -m nltk.downloader wordnet
python -m spacy download en_core_web_lg
