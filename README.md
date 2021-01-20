# vocabulary-extraction
Find the vocabulary you need to learn to understand some article or book.

## How to use
1. Install pipenv
`pip install pipenv`
2. Create an empty .env file
`touch .env`
3. Install pip dependencies
`pip install -r requirements.txt`
4. Download nltk and spacy datasets
`. ./download_datasets.sh`
5. Run
`pipenv run main`
6. Test
`pipenv run test`
7. Place the dataset in the `src/data` folder:
```
unzip arXMLiv_08_2018_no_problem.zip -d ${REPO_ROOT}/src/data
```
8. Preprocess a part of the dataset
```
cd src/utils/input_utils
python data_handling.py
```



### Team Members
* Lukas Ballweg (lukas.ballweg@riseup.net)
* Lukas Bockstaller (lukas.bockstaller@posteo.de)
* Joshua Kraft (nathan.joshua.kraft@gmx.de)
* Philipp Walz (philipp@walz.tech)

### Libraries / Existing Code Fragements
The main processing steps are performed with the help of spaCy, nltk, regex and wordfreq.
For a complete list of project dependencies look at the [requirements.txt](requirements.txt)

Apart from that no other existing code fragments were used.


## Project State
<!-- TODO: Hier pro Subgoal die Einzel-Tasks (z.B. die pipeline steps)
auflisten und für die fertigen einen Haken setzen Kommentare mit `>` um zu Zusatzinfos zu geben-->

**For now we mainly focused on two main tasks:**
* retrieving the Dataset and preparing data driven approaches
* building a first general data independent pipeline to solve our subtasks

We haven't started creating an approach for evaluating our pipeline. This is part of the upcomming work in January, now that we have an overview over our first baseline pipeline and it's components.

### Planning State and Future Planning

In this Section we will give a overview over our **general pipeline addressing our proposed subgoals**.
We will focus on the retrieval of the data in the subsection [Data Analysis](#data-analysis).

#### Subgoal 1: Text extraction
> First of all, we do need all words included in the given user input. Therefore our first subgoal is to create a vocabulary list based on the text of the PDF. This will include **Lemmatization** to grasp related words as one. We think of using **Part of Speech** to classify the words to be able to drop non-useful words like pronouns or entities etc. Additionally, we will add the frequency of the words for further ranking down the pipeline.

> **Goal:** The list should contain each noun, verb, and adjective of the text in its root form and should not have duplicates or closely related words.

As a little bonus we already implemented the
[extraction of text](/src/utils/input_utils/text_extraction.py) regarding these channels:
- [x] HTML-raw text extraction
- [x] PDF-raw text extraction
- [ ] Image-raw text extraction

We used spacy to implement our [pipeline processing the input](/src/pipeline/create_pipeline.py).
In the first step we already implemented:
- [x] [filter for P-O-S, Entities and stopwords](/src/pipeline/pipeline_components/pipe_filter_tokens.py)
- [x] [deduplication of the vocabulary list](/src/pipeline/pipeline_components/pipe_eliminate_duplicates.py)


#### Subgoal 2: Word difficulty / rareness estimation
> Second, we want to filter the vocabulary based on their difficulty. In most cases, the difficulty of a word strongly correlates with its frequency in the given language. We plan to use a pre-existing API/Corpora which leverages this fact and therefore provides us with a ranking.

> **Goal:** Having a numerical difficulty estimation for each word.

We choose to use the lib [wordfreq](https://pypi.org/project/wordfreq/) to implement this subtask.
The difficulty of the words is based on their overall frequency in the given language and the syllable count.

- [x] [numerical difficulty estimation](/src/pipeline/pipeline_components/pipe_difficulty.py)
- [ ] hyperparameter tuning of the ranking algorithm (data driven)

#### Subgoal 3: Identification of heavily used words
> Rare words by nature tend to be important if they are still heavily used. We can identify which words occur above their average, by using a **Bag of Words** or other **statistical** approach. For Example: If **Goalkeeper** has a 1:x appearance in the text but a 1:y overall appearance and x << y then we can infer that this word is relevant in this text.

> **Goal:** Having a weighted numerical score representing relative frequency

Our pipeline already includes a relative frequency rating based on an overall frequency
of the word in the given language. This metric seems to be promising for further estimation:

- [x] [weighted numerical score representing relative frequency](/src/pipeline/pipeline_components/pipe_relative_frequency.py)

#### Subgoal 4: Identification of relevant words
> In this step, we want to extract the vocabulary the user needs to understand the main concepts of the text. This would include words in key phrases of the text which are also in our ranked vocabulary list. This could be solved with an **Key Phrase Extraction**, which hopefully will be presented in the lecture. We want to create a list of all Key Phrases of the text. Next, we want to cross-check these phrases with our existing vocabulary list.

> **Goal:** Having a mark on each vocabulary in the list contained in a Key Phrase.

We did not tackle subgoal 4 yet:
- [ ] Key phrase detection

#### Overall ranking
We implemented a basic overall ranking that is calculated from the difficulty and the relative frequency with one weighting factor for each of them.

### Future Planning:

#### Reflecting
As one can see we were able to almost completely **finish subtask 1-3** on a general level.
This is given to the fact, that we chose to start with a rather general approach to approximate the topic of interest.
Which means, that we do not tune our pipeline components according to a dataset.
(Which especially made sense as long as we did not have access to a comprehensive dataset)
This left us with a working pipeline providing us with reasonable good results on a arbitrary text.
At this state of the project we have a few options to proceed:

#### 1. Key Phrase Extraction (subtask 4)
As we did not include this part in our pipeline yet, this leaves us with great room for improvement.
The latent goal behind this subtask is to estimate the words which carry the most meaning of the text and
are therefore most relevant to know and comprehend. Which means we still can get creative on how to solve
this problem best. Besides Key Phrase Extractions we want to try out other related approaches to solve this
subtask as good as possible. Some of our ideas are:

* Clustering wordvectors and weight the vocabs on the size of each cluster. Words being part of a big cluster an therefore a dominant topic of the text will be more relevant for the user.
* Using SVD on input parts to get the relationship of word to their topics and the topics of the input text.
* Key Phrase Extraction of the given input (data driven?)

#### 2. Data driven approach
Since we have a dataset to work with, we can tune our pipeline according to this dataset. This will hopefully
provide us with a proof of concept, that we can improve our results, if we focus on a given domain. The goal
would be to solve data specific tasks and optimise our results on the data with approaches which can be
generalized on other domains. This tasks could include:

* Tuning parameters including frequency, weights etc. on a given dataset
* Training an entity in spacy on technical terms on a given dataset with rule based annotations
* Using SVD on corpus to get the relationship of word to their topics and the topics of the input text.
* Using word vector distances to the keywords (keyword section) of our dataset (dataset specific and therefore not generalizable but still fun)

### High-level Architecture Description
Our architecture does only consists of our [pipeline](src/pipeline) our [utils](src/utils) for input/output etc.
and our [tests](src/tests). The data exploration and the running first pipeline can also be found in our [jupyter
notebooks](src/notebooks).

The current [pipeline](src/pipeline) should be relatively clear at this point, but has this overview:

* input: [text_extraction.py](src/utils/input_utils/text_extraction.py)
* pipeline: [create_pipeline.py](src/pipeline/create_pipeline.py)
    * [pipe_wordcount.py](src/pipeline/pipeline_components/pipe_wordcount.py)
    * [pipe_filter_tokens.py](src/pipeline/pipeline_components/pipe_filter_tokens.py)
    * [pipe_eliminate_duplicates.py](src/pipeline/pipeline_components/pipe_eliminate_duplicates.py)
    * [pipe_relative_frequency.py](src/pipeline/pipeline_components/pipe_relative_frequency.py)
    * [pipe_difficulty.py](src/pipeline/pipeline_components/pipe_difficulty.py)
* output: [create_df_from_doc.py](src/utils/output_utils/create_df_from_doc.py)



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


