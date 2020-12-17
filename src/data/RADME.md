# arXMLiv 08.2018 - An HTML5 dataset for arXiv.org

We are primarily using the [arXMLiv 08.2018](https://sigmathling.kwarc.info/resources/arxmliv-dataset-082018/) data set. 
This dataset is a large collection of HTML5 scientific papers provided by the he [KWARC](https://kwarc.info/) research group.

For our purposes the `arXMLiv_08_2018_no_problem.zip` is sufficient, as in the first project iteration we expect the input corpora to be well formatted without any conversion errors.  

Please place the dataset directly in the /src/data folder:
```
unzip arXMLiv_08_2018_no_problem.zip -d ${REPO_ROOT}/src/data
mv ./data/datasets/dataset-arXMLiv-08-2018/* .
rm -r data
```
