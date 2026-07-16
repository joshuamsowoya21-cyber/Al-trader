# AITrader AI Analyzer v1.0

from strategy.scalping import generate_signal

class AIAnalyzer:

    def analyze(self, price, ema_fast, ema_slow, rsi):
        signal = generate_signal(price, ema_fast, ema_slow, rsi)

        print("========== AI ANALYSIS ==========")
        print(f"Price: {price}")
        print(f"EMA Fast: {ema_fast}")
        print(f"EMA Slow: {ema_slow}")
        print(f"RSI: {rsi}")
        print(f"Signal: {signal}")

        return signal


# Example
bot = AIAnalyzer()
bot.analyze(
    price=3350.20,
    ema_fast=3352.10,
    ema_slow=3348.40,
    rsi=28
)
