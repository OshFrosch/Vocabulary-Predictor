
# vocabulary-extraction
Find the vocabulary you need to learn to understand some article or book.

## Installation
1. Download vocabulary_extraction wheel from releases page:  
https://github.com/walzph/vocabulary-extraction/releases
2. Install vocabulary_extraction
`pip install vocabulary_extraction-0.0.2-py3-none-any.whl`
3. Download nltk and spacy datasets
`. ./download_datasets.sh`
5. Test installation
`python -m vocabulary_extraction --help`

## Usage
```
usage: __main__.py [-h] (--raw | --html | --pdf) [-a | -s SIZE | -i] [--to_csv FILE_PATH] [--csv_separator SEP] [-v]
                   INPUT_FILE_PATH

vocabulary-extraction gives you the most relevant vocabulary to learn before reading texts a language that you are not
a native speaker of (currently only English is supported). You can use raw text, html or pdf files as input and
generate a vocabulary list of the most relevant words. The output is a comma seperated file with the colums `word`,
`example sentence` and `Synonyms Definition and Examples`

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Log extended information

Input:
  --raw                 Input file is raw text (default)
  --html                Input file is HTML (e.g. arXMLiv document)
  --pdf                 Input file is PDF
  INPUT_FILE_PATH       Path to input file

Mode:
  -a, --all             Output is complete vocabulary
  -s SIZE, --size SIZE  Specify max. vocabulary size
  -i, --interactive     Determine vocabulary size by interactive feedback

Output:
  --to_csv FILE_PATH    Write output to file path instead of STDOUT (optional)
  --csv_separator SEP   Define a custom CSV separator (default: , )

Save time in reading difficult texts and improve your language skills along the way!
```

> **Example:**   
> Run on raw text input and write complete vocabulary list as comma-separated file to path:
> `python -m vocabulary_extraction --raw sample.txt --to_csv output.csv`


## How to setup the project for contribution?
1. Install pipenv
`pip install pipenv`
2. Install pip dependencies
`pipenv install --dev`
3. Download nltk and spacy datasets
`. ./download_datasets.sh`
4. Run
`pipenv run main --raw sample.txt`
5. Test
`pipenv run test`

### Other helpful commands:  
* Place the arXMLiv dataset in the `/data` folder:  
`unzip arXMLiv_08_2018_no_problem.zip -d ${REPO_ROOT}/data`
* Place the [Complex Word Identification Dataset](https://www.inf.uni-hamburg.de/en/inst/ab/lt/resources/data/complex-word-identification-dataset/cwishareddataset.zip) in the `/data`-folder 
* Install new dependencies via  
`pipenv install {{package name}}`  
or  
`pipenv install {{package name}}`
* Download spaCy model via  
`python -m spacy download en_core_web_lg`  



## Team Members
* Lukas Ballweg (lukas.ballweg@riseup.net)
* Lukas Bockstaller (lukas.bockstaller@posteo.de)
* Joshua Kraft (nathan.joshua.kraft@gmx.de)
* Philipp Walz (philipp@walz.tech)


## High-level Architecture Description
Our architecture consists out of our [main pipeline](vocabulary_extraction/pipeline), [utils](vocabulary_extraction/utils) for input/output etc.
and our [tests](vocabulary_extraction/tests). The data exploration and pipeline exploration can also be found in our [jupyter
notebooks](notebooks).

**Pipeline overview:**

* input: [text_extraction.py](vocabulary_extraction/utils/input_utils/text_extraction.py)
* pipeline: [create_pipeline.py](vocabulary_extraction/pipeline/create_pipeline.py)
    * [pipe_wordcount.py](vocabulary_extraction/pipeline/pipeline_components/pipe_wordcount.py)
    * [pipe_filter_tokens.py](vocabulary_extraction/pipeline/pipeline_components/pipe_filter_tokens.py)
    * [pipe_eliminate_duplicates.py](vocabulary_extraction/pipeline/pipeline_components/pipe_eliminate_duplicates.py)
    * [pipe_difficulty.py](vocabulary_extraction/pipeline/pipeline_components/pipe_difficulty.py)
    * [pipe_relative_frequency.py](vocabulary_extraction/pipeline/pipeline_components/pipe_relative_frequency.py)
    * [pip_keywords.py](vocabulary_extraction/pipeline/pipeline_components/pipe_keywords.py)
* ranking: [create_df_from_doc.py](vocabulary_extraction/utils/output_utils/create_df_from_doc.py)

**Output/Postprocessing:**
* interactive: [predict_output_size.py](vocabulary_extraction/utils/output_utils/predict_output_size.py)
* csv_export: [create_csv_from_df.py](vocabulary_extraction/utils/output_utils/create_csv_from_df.py)
* extra info: [add infos_to_df.py](vocabulary_extraction/utils/output_utils/add_infos_to_df.py)


## Evaluating the pipeline

These two notebooks can be used to evaluate the performance of our pipeline.

It is necessary to have the datasets in place before running these notebooks.

* [evaluate_relevancy.ipynb](notebooks/evaluate_relevancy.ipynb)
* [evaluate_difficulty.ipynb](notebooks/evaluate_difficulty.ipynb)



## Data-Analysis
### The arXMLiv 08.2018 dataset

We are primarily using the [arXMLiv 08.2018](https://sigmathling.kwarc.info/resources/arxmliv-dataset-082018/) data set.
This dataset is a large collection of HTML5 scientific papers provided by the he [KWARC](https://kwarc.info/) research group.

For our purposes the `arXMLiv_08_2018_no_problem.zip` is sufficient, as in the first project iteration we expect the input corpora to be well formatted without any conversion errors.


The dataset consists out of 150701 html-files stored in 337 folders and take up roughly 60GB of storage. The only useful metadata associated with these files is their [arXiv-Identifier](https://arxiv.org/help/arxiv_identifier) which is used as the filename. The old version of the arXiv-identifier might allow us to double check clustering by using the embedded scientific field name as second clustering method and check for similiarities. The new version doesn't allow this. Further analysis is needed.

Each HTML5 file contains a styled representation of the original scientific paper latex document excluding any original images. The conversion tool LateXML converted formulas into MathML-tags and added an additional footer.
Therefore it is necessary to drop all ```math```and ```footer```-tags before using ```BeautifulSoup4.get_text()``` to extract usable text. This text needs further postprocessing like lowercasing or duplicate-whitespace removal.

[An initial exploratory jupyter notebook](https://github.com/walzph/vocabulary-extraction/blob/develop/src/notebooks/explore_dataset.ipynb) implements these and additional simplification steps to get a better understanding of the dataset and it's size.
Initial estimations suggest that this dataset contains about 321,639,330 tokens from a set of 715,300 unique tokens. These estimates will vary widely depending on the used clean up, tokenizing and stemming functions.

### Accessing the dataset

The necessary preprocessing of these files takes a considerable amount of time. Applying the ```get_text(file)```-method of the exploratory notebook takes about 2 seconds per file. Rerunning this computation every time would take up a lot of development time. Fortunately this results in a string length reduction down to 10%-20% percent of the original raw text so a caching method is viable. [This Issue](https://github.com/walzph/vocabulary-extraction/issues/8) outlines such a caching dataset interface.


