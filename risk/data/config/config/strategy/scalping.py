# AITrader Scalping Strategy v1.0

def generate_signal(price, ema_fast, ema_slow, rsi):
    """
    Returns:
    BUY, SELL or HOLD
    """

    if ema_fast > ema_slow and rsi < 30:
        return "BUY"

    elif ema_fast < ema_slow and rsi > 70:
        return "SELL"

    else:
        return "HOLD"
