import pickle
from pathlib import Path

tf_values = []

with open(
    str(Path(__file__).parent.absolute()) + "/tf_factors.pickle", "rb"
) as inputfile:
    c1 = pickle.load(inputfile)

tf_values = c1
total_tf_values = sum(c1.values())
