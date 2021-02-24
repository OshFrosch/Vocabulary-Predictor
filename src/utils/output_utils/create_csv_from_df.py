from nltk.corpus import wordnet


def create_csv_from_df(
    df, filename="output/results.csv", limit=50, limit_examples=5, limit_definitions=5
):
    df = df[["token", "example phrase"]].head(limit)
    df.columns = ["word", "example sentence"]

    synonyms_definitions_examples = [
        get_infos(str(word), limit_examples, limit_definitions) for word in df["word"]
    ]

    df["Synonyms, Definition and Examples"] = synonyms_definitions_examples
    df = df.set_index("word")
    df.to_csv(filename, header=False)


def get_infos(word, limit_definitions, limit_examples):
    synonyms = get_synonyms(word)
    definitions, examples = get_definitions_and_examples(
        word, limit_definitions, limit_examples
    )

    results = []
    if len(synonyms) > 0:
        results.append("Synonyms: " + synonyms)
    if len(definitions) > 0:
        results.append("Definitions: \n" + definitions)
    if len(examples) > 0:
        results.append("Examples: \n" + examples)

    results_as_string = "\n\n".join(results)

    return results_as_string


def get_synonyms(word):
    syns = wordnet.synsets(word)
    synonyms = [syn.lemmas()[0].name() for syn in syns]
    synonyms = set(synonyms)
    if word in synonyms:
        synonyms.remove(word)
    synonyms = ", ".join(synonyms)
    return synonyms


def get_definitions_and_examples(word, limit_examples, limit_definitions):
    syns = wordnet.synsets(word)

    definitions = []
    examples = []

    for syn in syns:
        if syn.lemmas()[0].name() == word:
            definitions.append(syn.definition())
            examples.append(", ".join(syn.examples()))

    limit_examples = min(limit_examples, len(examples))
    limit_definitions = min(limit_definitions, len(definitions))

    definitions = "\n".join(definitions[0:limit_examples])
    examples = "\n".join(examples[0:limit_definitions])

    return definitions, examples
