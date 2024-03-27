"""Base class for all tokenisers."""
class Tokeniser:
    """Base class for all tokenisers. All tokenisers should inherit from this class."""

    def __init__(self):
        """Initialise the tokeniser"""
        self.vocabulary = []
        self.stoi = {}
        self.itos = {}

        self.categories = []
        self.ctoi = {}
        self.itoc = {}

    def setVocabulary(self, vocabulary):
        """Set the vocabulary for the tokeniser"""
        raise NotImplementedError('setVocabulary method not implemented')

    def encode(self, text):
        """Encode the text"""
        raise NotImplementedError('encode method not implemented')

    def decode(self, encodedText):
        """Decode the encoded text"""
        raise NotImplementedError('decode method not implemented')

    def setCategories(self, categories: list[str]) -> None:
        """Set the categories for the tokeniser"""
        self.ctoi = { category: i for i, category in enumerate(categories) }
        self.itoc = { i: category for i, category in enumerate(categories) }

    def encodeCategory(self, category: str) -> int:
        """Encode the category"""
        return self.ctoi[category]

    def decodeCategory(self, encodedCategory: int) -> str:
        """Decode the encoded category"""
        return self.itoc[encodedCategory]
