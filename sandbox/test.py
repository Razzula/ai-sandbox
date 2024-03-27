# pylint: disable=fixme, line-too-long, invalid-name, superfluous-parens, trailing-whitespace
import re

import pandas as pd

from tokenisers.BasicTokeniser import BasicTokeniser
from vectorisers.BagOfWords import BagOfWords
from algorithms.NaiveBayes import NaiveBayes
from ConfusionMatrix import ConfusionMatrix

def formatData(message: str) -> str:
    return re.sub(r'[^\w\s]', '', message).lower()

# 0. Data

# Load
data = pd.read_csv('sandbox/spam.csv', encoding='latin-1')
data = data.rename(columns={'1': 'Category', '2': 'Message'})

# Format
data['Message'] = [ formatData(x) for x in data['Message'] ]

# Split
split = int(len(data) * 0.75)

trainingData = data[:split]
testingData = data[split:]

# 1. Pre-Processing

vocabulary = set()
for message in data['Message']:
    for word in message.split():
        vocabulary.add(word)

categories = set(data['Category'])

# Tokenisation
tokeniser = BasicTokeniser(granularity=' ') # word level
tokeniser.setVocabulary(sorted(vocabulary))
tokeniser.setCategories(sorted(categories))

# Vectorisation
vectoriser = BagOfWords(tokeniser)
probabilityTable, classProbabilityTable = vectoriser.fitTransform(trainingData, vocabulary, categories, k=0.5)

# 2. Processing
# In this case, training the algorithm is just a matter of storing the probability table and class probability table.

algorithm = NaiveBayes()
algorithm.fit(probabilityTable, classProbabilityTable, k=0.5)

# 3. Post-Processing
# Evaluation
confusionMatrix = ConfusionMatrix(categories)

for index, entry in testingData.iterrows():

    expected = tokeniser.encodeCategory(entry['Category'])
    predicted = algorithm.predict(tokeniser.encode(formatData(entry['Message'])))

    confusionMatrix.increment(expected, predicted)

print(confusionMatrix.getAverageF1Score())
