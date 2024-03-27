# pylint: disable=fixme, line-too-long, invalid-name, superfluous-parens, trailing-whitespace
"""Bag of words vectoriser. Inherits from Vectoriser."""
import torch

from vectorisers._Vectoriser import Vectoriser
from tokenisers._Tokeniser import Tokeniser

class BagOfWords(Vectoriser):
    """Bag of words vectoriser. Inherits from Vectoriser."""

    def __init__(self, tokeniser: Tokeniser):
        """Initialise the vectoriser."""
        # super().__init__()
        self.tokeniser = tokeniser

    def fitTransform(self, corpus, vocabulary, categories, k: float = 0.5):
        """
        Fit the model to the training data.

        Return a matrix representing the P(word|class) for each word in the vocabulary.
        """

        frequencyTable = torch.zeros(len(vocabulary), len(categories))
        classFrequencyTable = torch.zeros(len(categories))

        # record frequencies of each word per category
        for _, entry in corpus.iterrows():
            encodedCategory = self.tokeniser.encodeCategory(entry['Category'])
            classFrequencyTable[encodedCategory] += 1 # record frequencies of each category

            simplifiedMessage = list(set(entry['Message'].split()))
            for encodedWord in self.tokeniser.encode(simplifiedMessage):
                frequencyTable[encodedWord][encodedCategory] += 1

        # convert to probability table, via normalisation
        probabilityTable = (frequencyTable + k) / (classFrequencyTable + (2 * k)) # P(word|class)

        classProbabilityTable = classFrequencyTable / classFrequencyTable.sum() # P(class)

        return probabilityTable, classProbabilityTable
