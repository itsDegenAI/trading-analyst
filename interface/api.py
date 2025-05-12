
from fastapi import FastAPI
from core.orchestrator import DegenCore

app = FastAPI()

@app.get("/analyze")
async def analyze_wallet(wallet: str):
    engine = DegenCore(wallet)
    results = await engine.run_full_analysis()
    return {"wallet": wallet, "insights": results}
