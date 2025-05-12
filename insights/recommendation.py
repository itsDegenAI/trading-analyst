
class RecommendationEngine:
    def generate(self, trades, patterns):
        insights = []
        for trade in trades:
            if trade["score"] < 0.5:
                insights.append(f"Poor entry on {trade['token']} — consider avoiding FOMO.")
            elif trade["duration"] > 5:
                insights.append(f"Late exit on {trade['token']} — reassess holding threshold.")
        clusters = {t['pattern'] for t in patterns}
        if len(clusters) > 1:
            insights.append("Detected mixed pattern clusters — refine strategy consistency.")
        return insights
