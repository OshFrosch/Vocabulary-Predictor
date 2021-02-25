from setuptools import find_packages, setup

setup(
    name="vocabulary_extraction",
    version="0.0.1",
    zip_safe=False,
    packages=find_packages(
        include=[
            "vocabulary_extraction",
            "vocabulary_extraction.utils",
            "vocabulary_extraction.utils.*",
            "vocabulary_extraction.pipeline",
            "vocabulary_extraction.pipeline.*",
        ]
    ),
    install_requires=[
        "beautifulsoup4>=4.9.3,<5.0.0",
        # "en-core-web-lg",
        "nltk>=3.5,<4.0.0",
        "numpy>=1.20.1,<2.0.0",
        "pandas>=1.2.2<2.0.0",
        "pdfminer.six==20201018",
        "spacy>=2.3.5,<3.0.0",
        "wordfreq>=2.4.2,<3.0.0",
        "matplotlib>=3.3.4,<4.0.0",
        "yake>=0.4.4,<1.0.0",
    ],
    # dependency_links=[
    #     "https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.3.1/en_core_web_lg-2.3.1.tar.gz#egg=en_core_web_lg"
    # ],
)
