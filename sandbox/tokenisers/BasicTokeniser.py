# pylint: disable=fixme, line-too-long, invalid-name, superfluous-parens, trailing-whitespace
from tokenisers._Tokeniser import Tokeniser

class BasicTokeniser(Tokeniser):
    """Basic tokeniser class. Simple index of vocabulary."""

    def __init__(self, granularity: str) -> None:
        """Initialise the tokeniser"""
        super().__init__()
        self.granularity = granularity

    def setVocabulary(self, vocabulary: list[str]) -> None:
        """Set the vocabulary for the tokeniser"""
        self.stoi = { word: i for i, word in enumerate(vocabulary) }
        self.itos = { i: word for i, word in enumerate(vocabulary) }

    def encode(self, text: str | list) -> list[int]:
        """Encode the text"""
        if (isinstance(text, str)):
            return [self.stoi[word] for word in text.split()]
        return [self.stoi[word] for word in text]

    def decode(self, encodedText: list[int]) -> str:
        """Decode the encoded text"""
        return self.granularity.join([self.itos[i] for i in encodedText])
