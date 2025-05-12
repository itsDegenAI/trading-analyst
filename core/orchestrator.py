
import asyncio
import logging
from strategy.pattern_model import PatternModel
from analysis.trade_context import TradeAnalyzer
from insights.recommendation import RecommendationEngine

class DegenCore:
    def __init__(self, wallet_address):
        self.wallet = wallet_address
        self.analyzer = TradeAnalyzer(wallet_address)
        self.recommender = RecommendationEngine()
        self.model = PatternModel()

    async def run_full_analysis(self):
        logging.info("Running full analysis pipeline...")
        trades = await self.analyzer.fetch_and_score_trades()
        patterns = self.model.detect(trades)
        insights = self.recommender.generate(trades, patterns)
        logging.info("Analysis complete.")
        return insights

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    wallet = "So1anaTestWallet9xxxxx"
    core = DegenCore(wallet)
    asyncio.run(core.run_full_analysis())
