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

### Team Members
* Lukas Ballweg (lukas.ballweg@riseup.net)
* Lukas Bockstaller (lukas.bockstaller@posteo.de)
* Joshua Kraft (nathan.joshua.kraft@gmx.de)
* Philipp Walz (philipp@walz.tech)

### Libraries / Existing Code Fragements
The main processing steps are performed with the help of space, nltk, regex and wordfreq. 
For a complete list of project dependencies look at the [requirements.txt](requirements.txt)

Apart from that no other existing code fragments were used.


## Project State
<!-- TODO: Hier pro Subgoal die Einzel-Tasks (z.B. die pipeline steps) 
auflisten und für die fertigen einen Haken setzen Kommentare mit `>` um zu Zusatzinfos zu geben-->

**For now we mainly focused on two main tasks:**
* retrieving the Dataset and preparing data driven approaches
* building a first general data independent pipeline to solve our subtasks  


### Planning State and Future Planning

In this Section we will give a overview over our **general pipeline addressing our proposed subgoals**.
We will focus on the retrieval of the data in the subsection [Data Analysis](#data-analysis).

#### Subgoal 1: Text extraction
> First of all, we do need all words included in the given user input. Therefore our first subgoal is to create a vocabulary list based on the text of the PDF. This will include **Lemmatization** to grasp related words as one. We think of using **Part of Speech** to classify the words to be able to drop non-useful words like pronouns or entities etc. Additionally, we will add the frequency of the words for further ranking down the pipeline.

> **Goal:** The list should contain each noun, verb, and adjective of the text in its root form and should not have duplicates or closely related words.

As a little bonus we already implemented the
[extraction of text](/src/utils/text_extraction.py) regarding these channels:
- [x] HTML-raw text extraction
- [x] PDF-raw text extraction
- [x] Image-raw text extraction

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

### Future Planning:

#### Reflecting
As one can see we were able to almost completely **finish subtask 1-3** on a general level.
This is given to the fact, that we chose to start with a rather general approach to approximate the topic of interest.
Which means, that we do not tune our pipeline components according to a dataset.
(Which especially made sense as long as we did not have access to a comprehensive dataset)
This left us with a working pipeline providing us with reasonable good results on a arbitrary text.
At this state of the project we have a few ways to go next:

#### 1. Key Phrase Extraction (subtask 4)
As we did not include this part in our pipeline yet, this leaves us with great room for improvement.
The latent goal behind this subtask is to estimate the words which carry the most meaning of the text and
are therefore most relevant to know and comprehend. Which means we still can get creative on how to solve 
this problem best. Besides Key Phrase Extractions we want to try out other related approaches to solve this 
subtask as good as possible. Some of our ideas are: 

* Clustering wordvectors and weight the vocabs on the size of each cluster. Words beeing part of a big cluster an therefore a dominant topic of the text will be more relevant for the user. 
* Using SVD on input parts to get the relationship of word to their topics and the topics of the input text.
* Key Phrase Extraction of the given input

#### 2. Data driven approach
Since we have a dataset to work with, we can tune our pipeline according to this dataset. This will hopefully
provide us with a proof of concept, that we can improve our results, if we focus on a given domain. The goal
would be to solve data specific tasks and optimise our results on the data with approaches which can be 
generalized on other domains. This tasks could include:

* Tuning parameters including frequency, weights etc. on a given dataset
* Training an entity in spacy on technical terms on a given dataset with rule based annotations
* Using SVD on corpus to get the relationship of word to their topics and the topics of the input text.


### High-level Architecture Description
<!-- TODO: Hier muss die Ordnerstruktur und die Zusammensetzung der Processing Pipeline erklärt werden -->

##Data-Analysis
### The arXMLiv 08.2018 dataset

We are primarily using the [arXMLiv 08.2018](https://sigmathling.kwarc.info/resources/arxmliv-dataset-082018/) data set. 
This dataset is a large collection of HTML5 scientific papers provided by the he [KWARC](https://kwarc.info/) research group.

For our purposes the `arXMLiv_08_2018_no_problem.zip` is sufficient, as in the first project iteration we expect the input corpora to be well formatted without any conversion errors.  

Please place the dataset in the `src/data` folder:
```
unzip arXMLiv_08_2018_no_problem.zip -d ${REPO_ROOT}/src/data
```
<Hier hab ich mal alles bezüglich des Datensets hingemacht>
- [x] Choosing the dataset
- [ ] Dataset retrieval
