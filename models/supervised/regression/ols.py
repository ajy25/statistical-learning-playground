import numpy as np
import numpy.linalg as la
import pandas as pd

class OLS():
    """Ordinary Least Squares with L1 and L2 regularization"""

    def __init__(self, add_constant = False, regularization = 'none'):
        """
        OLS model
        @args
        - add_constant: adds bias term if True
        - regularization: either {'none', 'ridge', 'lasso'}
        """
        self.add_constant = add_constant
        self.regularization = regularization
        self.beta = None
        self.X = None
        self.y = None
        self.stats = {}
            
    def fit(self, X: np.ndarray, y: np.ndarray, add_constant: bool = None, 
            regularization: str = None):
        """
        Re-fit the model on the training data (X, y)
        @args
        - X: np.array ~ (N, p)
        - y: np.array ~ (N) or (N, 1)
        - add_constant: adds a constant if True
        - regularization: either {'none', 'ridge', 'lasso'}
        """
        assert len(X.shape) == 2
        assert len(y.shape) in (1, 2)
        assert X.shape[0] == y.shape[0]
        if add_constant is not None: self.add_constant = add_constant
        if regularization is not None: self.regularization = regularization
        if self.add_constant:
            X = np.hstack((np.ones((X.shape[0], 1)), X))
        if y.shape == 2:
            assert y.shape[1] == 1
            y = y.squeeze()
        self.X = X
        self.y = y
        self.beta = la.inv(self.X.T @ self.X) @ self.X.T @ self.y
    
    def fit_from_df():
        pass

    def metrics(self): 
        """
        Detailed metrics related to the model fit
        """

    def forward(self, X: np.ndarray):
        """
        @args
        - X: np array ~ (n, p)
        """
        assert len(X.shape) == 2
        assert X.shape[1] == self.X.shape[1]
        if self.add_constant:
            X = np.hstack(np.ones((X.shape[0], 1)), X)
        return X @ self.beta 
    
    def _detect_and_transform_full_rank(X):
        
        return X

    





