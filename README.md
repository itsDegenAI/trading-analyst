
<p align="center">
  <img src="image.png" alt="Degen AI Banner" />
</p>

# 🧠 Degen AI  
**Your personalized memecoin trading analyst, powered by machine learning and wallet forensics.**

---

## What is Degen AI?

Degen AI is a private AI system designed to evaluate and improve your Solana-based meme coin trading behavior.

It continuously monitors your wallet activity, analyzes every trade (entry + exit), detects hidden inefficiencies, and provides actionable alpha — *before you make the same mistake again*.

---

## 🔍 Core Capabilities

- 📈 Reverse-engineering your trading history  
- 🧠 Detecting behavioral patterns, FOMO loops, and exit delays  
- 🧮 Scoring each trade based on context and timing  
- 🧬 Comparing your behavior to top wallets across the chain  
- 📊 Suggesting optimizations to your risk-reward profile  

---

## 🧩 Modules

| Folder        | Description                                          |
|---------------|------------------------------------------------------|
| `core/`       | Degen AI orchestration and lifecycle control         |
| `strategy/`   | Pattern recognition, statistical modeling            |
| `analysis/`   | Trade analysis and contextual scoring                |
| `wallets/`    | Wallet profiling, peer clustering                    |
| `insights/`   | Insight generation and behavior summaries            |
| `data/`       | Raw market + token context builders                  |
| `interface/`  | Command-line and API access                          |

---

## 🧠 System Architecture

```mermaid
graph TD
A[Wallet Transactions] --> B[Trade Analyzer]
B --> C[Pattern Model]
C --> D[Insight Generator]
D --> E[API / CLI Output]
```

---

## 🧪 Example Output

```json
{
  "wallet": "9Fx...YsW",
  "entry_timing_score": 0.63,
  "avg_exit_delay": "4.7 blocks",
  "cluster_behavior": "Mid-tier sniper",
  "suggestion": "Reduce buys during green candle clusters. Typical PnL decays after initial entry."
}
```

---

## ⚙️ Installation

```bash
git clone https://github.com/degen-ai/engine.git
cd engine
pip install -r requirements.txt
```

---

## 🚀 Run the Engine

```bash
python3 core/orchestrator.py
```

---

## 🌐 API Mode

```bash
uvicorn interface.api:app --reload
```

---

## 🧪 Testing

To run unit tests:

```bash
pytest test/
```

Mock data and test wallets are available in `/test/fixtures/`.

---

## 📁 Project Structure

```
degen-ai/
├── core/
├── strategy/
├── analysis/
├── wallets/
├── insights/
├── data/
├── interface/
└── README.md
```

---

## 📜 License

MIT License. Use freely, but attribution is appreciated.
