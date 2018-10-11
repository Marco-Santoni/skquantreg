from sklearn.base import BaseEstimator, RegressorMixin
from statsmodels.regression.quantile_regression import QuantReg

import statsmodels.api as smapi

class QuantileRegressor(BaseEstimator, RegressorMixin):

    def __init__(self, q=0.5):
        self.q=q

    def fit(self, X, y):
        self.model_ = QuantReg(
            y,
            smapi.add_constant(X)
        )
        self.model_result_ = self.model_.fit(q=self.q)
        return self

    def predict(self, X):
        return self.model_result_.predict(
            smapi.add_constant(X)
        )
