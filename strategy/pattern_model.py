
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class PatternModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)

    def train(self, X, y):
        self.model.fit(X, y)

    def detect(self, trades):
        features = [[t["score"], t["duration"]] for t in trades]
        predictions = self.model.predict(features)
        for i, trade in enumerate(trades):
            trade["pattern"] = predictions[i]
        return trades
