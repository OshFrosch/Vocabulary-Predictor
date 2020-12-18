import regex as re


def get_entities(doc):
    """returns all entities of a text split into single words"""

    entities = []

    for ent in doc.ents:
        ents = re.findall(r"[a-zA-Z]+", ent.text)
        entities.extend(ents)

    return entities
