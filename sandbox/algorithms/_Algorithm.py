"""Base class for all algorithms."""
class Algorithm:
    """Base class for all algorithms. All algorithms should inherit from this class."""

    def fit(self, X, y):
        """Fit the model to the training data."""
        raise NotImplementedError('fit method not implemented')

    def predict(self, X):
        """Predict the target variable for the test data."""
        raise NotImplementedError('predict method not implemented')
