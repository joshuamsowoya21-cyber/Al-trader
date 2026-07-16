from ai.analyzer import AIAnalyzer
from risk.risk_manager import RiskManager

# Create objects
ai = AIAnalyzer()
risk = RiskManager()

# Example account
balance = 10
trades_today = 0

if risk.can_trade(trades_today):
    lot = risk.calculate_lot_size(balance)

    signal = ai.analyze(
        price=3350.20,
        ema_fast=3352.10,
        ema_slow=3348.40,
        rsi=28
    )

    print("---------------------")
    print("AITrader")
    print("Signal:", signal)
    print("Lot Size:", lot)
else:
    print("Daily trade limit reached.")
