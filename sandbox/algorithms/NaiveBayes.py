# pylint: disable=fixme, line-too-long, invalid-name, superfluous-parens, trailing-whitespace
import torch

from algorithms._Algorithm import Algorithm

class NaiveBayes(Algorithm):
    """Naive Bayes class. Inherits from Algorithm."""

    def __init__(self):
        """Initialise the algorithm."""
        # super().__init__()

    def fit(self, X, classProbabilityTable, k: float = 0.5):
        """Fit the model to the training data."""
        self.probabilityTable = X
        self.classProbabilityTable = classProbabilityTable
        self.k = k

    def predict(self, X):
        """Predict the class of the data"""

        probabilities = torch.zeros(len(self.classProbabilityTable))

        for wordIndex in X:
            for classIndex in range(len(self.classProbabilityTable)):
                pClassGivenWord = self.calculateClassProbGivenWord(wordIndex, classIndex)
                probabilities[classIndex] += torch.log(pClassGivenWord).item() # log-likelihood

        return torch.argmax(probabilities).item()

    def calculateClassProbGivenWord(self, wordIndex: int, classIndex: int):
        """Calculate the probability of a class given a word."""

        pClass = self.classProbabilityTable[classIndex] # P(class)

        pWordIntersectClass = self.probabilityTable[wordIndex][classIndex] * pClass # P(word|class) * P(class)
        pWordIntersectNotClass = 0

        for index, _ in enumerate(self.classProbabilityTable):
            if (index == classIndex):
                continue
            pWordIntersectNotClass += self.probabilityTable[wordIndex][index] * self.classProbabilityTable[index] # P(word|¬class) * P(¬class)

        pClassGivenWord = (pWordIntersectClass) / (pWordIntersectClass + pWordIntersectNotClass) # P(class|word)

        return pClassGivenWord
