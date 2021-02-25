import collections

import nltk
import numpy as np

### This Pipeline step is archived and excluded


def cluster_words(doc):
    """
    cluster all words based on the word vectors into #log(wordcount) clusters
    :param doc: spaCy Doc
    :return: spaCy Doc
    """

    X = [tok.vector for tok in doc if not tok._.is_excluded]
    dist = nltk.cluster.util.cosine_distance
    k = int(round(np.log(doc._.wordcount), 0))  # prototype
    print(k)

    kclusterer = nltk.cluster.KMeansClusterer(k, distance=dist)
    assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
    clusters = iter(assigned_clusters)

    for token in doc:
        if not token._.is_excluded:
            token._.cluster = next(clusters)

    doc._.cluster_sizes = collections.Counter(assigned_clusters)

    return doc


def exclude_smallest_clusters(doc):
    """
    would exclude all words from the vocabulary belonging to the smallest third of all clusters
    :param doc: spaCy Doc
    :return: spaCy Doc
    """

    cluster_count = len(doc._.cluster_sizes)
    smallest_clusters = []
    for i in range(int(cluster_count * 2 / 3), cluster_count):
        c = doc._.cluster_sizes.most_common()[i][0]
        smallest_clusters.append(c)

    print(smallest_clusters)

    for token in doc:
        if not token._.is_excluded:
            if token._.cluster in smallest_clusters:
                token._.is_excluded = True

    return doc
