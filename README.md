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
The main processing steps are performed with the help of space, nltk, regex and wordfreq. For a complete list of project dependencies look at the [requirements.txt](requirements.txt)

Apart from that no other existing code fragments were used.


## Project State
<!-- TODO: Hier pro Subgoal die Einzel-Tasks (z.B. die pipeline steps) auflisten und für die fertigen einen Haken setzen Kommentare mit `>` um zu Zusatzinfos zu geben-->
This section gives a comprehensive overview of the current project state. For this, we break down the project into the same subgoals which we already defined in the project proposal.  
Here, for each subgoal we list the performed and outstanding tasks and give comments.

### Planning State and Future Planning

#### Subgoal 1: Text extraction
> First of all, we do need all words included in the given user input. Therefore our first subgoal is to create a vocabulary list based on the text of the PDF. This will include **Lemmatization** to grasp related words as one. We think of using **Part of Speech** to classify the words to be able to drop non-useful words like pronouns or entities etc. Additionally, we will add the frequency of the words for further ranking down the pipeline.

> **Goal:** The list should contain each noun, verb, and adjective of the text in its root form and should not have duplicates or closely related words.


- [x] Choosing the dataset
- [ ] Dataset retrieval
- [x] HTML-raw text extraction
- [ ] lemmatization
- [ ] deduplication


#### Subgoal 2: Word difficulty / rareness estimation
> Second, we want to filter the vocabulary based on their difficulty. In most cases, the difficulty of a word strongly correlates with its frequency in the given language. We plan to use a pre-existing API/Corpora\footnote{twinword API: https://www.twinword.com/api/language-scoring.php} which leverages this fact and therefore provides us with a ranking.

> **Goal:** Having a numerical difficulty estimation for each word.

- [ ] Word frequency
- [ ] :
- [ ] : 

### Subgoal 3: Identification of heavily used words
> Rare words by nature tend to be important if they are still heavily used. We can identify which words occur above their average, by using a **Bag of Words** or other **statistical** approach. For Example: If **Goalkeeper** has a 1:x appearance in the text but a 1:y overall appearance and x << y then we can infer that this word is relevant in this text.

> **Goal:** Having a weighted numerical score representing $\frac{text-appearance}{overall-appearance}$  

- [ ] bag of words approach 
- [ ] :
- [ ] : 

### Subgoal 4: Identification of relevant words
> In this step, we want to extract the vocabulary the user needs to understand the main concepts of the text. This would include words in key phrases of the text which are also in our ranked vocabulary list. This could be solved with an **Key Phrase Extraction**, which hopefully will be presented in the lecture. We want to create a list of all Key Phrases of the text. Next, we want to cross-check these phrases with our existing vocabulary list.


> **Goal:** Having a mark on each vocabulary in the list contained in a Key Phrase.

- [ ] Key phrase detection
- [ ] Abstract keywords word vector comparision
- [ ] :
- [ ] : 

## High-level Architecture Description
<!-- TODO: Hier muss die Ordnerstruktur und die Zusammensetzung der Processing Pipeline erklärt werden -->

## Data Analysis
### The arXMLiv 08.2018 dataset

We are primarily using the [arXMLiv 08.2018](https://sigmathling.kwarc.info/resources/arxmliv-dataset-082018/) data set. 
This dataset is a large collection of HTML5 scientific papers provided by the he [KWARC](https://kwarc.info/) research group.

For our purposes the `arXMLiv_08_2018_no_problem.zip` is sufficient, as in the first project iteration we expect the input corpora to be well formatted without any conversion errors.  

Please place the dataset in the `src/data` folder:
```
unzip arXMLiv_08_2018_no_problem.zip -d ${REPO_ROOT}/src/data
```
