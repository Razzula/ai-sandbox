# pylint: disable=fixme, line-too-long, invalid-name, superfluous-parens, trailing-whitespace
"""Base class for all vectorisers."""
class Vectoriser:
    """Base class for all vectorisers. All vectorisers should inherit from this class."""

    def fitTransform(self, corpus):
        """Fit the model to the training data."""
        raise NotImplementedError('fitTransform method not implemented')
