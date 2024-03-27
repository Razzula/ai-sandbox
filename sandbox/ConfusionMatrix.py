import torch

class ConfusionMatrix:

    def __init__(self, categories: list | set):
        self.categories = categories
        self.matrix = torch.zeros(len(categories), len(categories))

    def increment(self, expected: int, predicted: int):
        self.matrix[expected][predicted] += 1

    def __str__(self):
        return str(self.matrix)

    def getAccuracy(self):
        return torch.trace(self.matrix) / torch.sum(self.matrix)

    def getPrecision(self, category: int):
        return self.matrix[category][category] / torch.sum(self.matrix[:, category])

    def getRecall(self, category: int):
        return self.matrix[category][category] / torch.sum(self.matrix[category])

    def getF1Score(self, category: int):
        precision = self.getPrecision(category)
        recall = self.getRecall(category)
        return 2 * (precision * recall) / (precision + recall)

    def getAverageF1Score(self):
        f1Score = 0
        for index, _ in enumerate(self.categories):
            f1Score += self.getF1Score(index)
        return f1Score / len(self.categories)
