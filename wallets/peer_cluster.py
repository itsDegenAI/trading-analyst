
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class WalletCluster:
    def __init__(self):
        self.wallet_vectors = {}

    def add_wallet_profile(self, wallet, features):
        self.wallet_vectors[wallet] = np.array(features)

    def find_closest(self, target_wallet):
        target_vector = self.wallet_vectors.get(target_wallet)
        if not target_vector.any():
            return None
        similarities = {
            w: cosine_similarity([target_vector], [vec])[0][0]
            for w, vec in self.wallet_vectors.items() if w != target_wallet
        }
        return sorted(similarities.items(), key=lambda x: -x[1])
