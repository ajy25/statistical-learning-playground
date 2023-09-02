import numpy as np
from ..model-base import 


class LinearRegression():

    def __init__(self, X_train: np.ndarray, y_train: np.ndarray, add_bias=True,
                 regularization='none'):
        """
        Constructs a linear model
        @args
        - X_train: np array ~ (m_train, p)
        - y_train: np array ~ (m_train)
        - add_bias: adds bias term if True
        - regularization: either {'none', 'ridge', 'lasso'}
        """
        self.X_train = X_train
        self.y_train = y_train
        self.fit(add_bias, regularization)
    
    def fit(self, add_bias=True, regularization='none'):
        """
        Re-fit the model on the training data
        @args
        - add_bias: adds bias term if True
        - regularization: either {'none', 'ridge', 'lasso'}
        """


    def forward(self, X: np.ndarray):
        """
        @args
        - X: np array ~ (m_test, p)
        """




