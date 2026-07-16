# AITrader Risk Manager

class RiskManager:

    def __init__(self):
        self.max_risk_percent = 1
        self.max_trades_per_day = 10

    def calculate_lot_size(self, balance):
        """
        Very simple placeholder calculation.
        We'll improve this later.
        """
        if balance < 100:
            return 0.01
        elif balance < 1000:
            return 0.05
        else:
            return 0.10

    def can_trade(self, trades_today):
        return trades_today < self.max_trades_per_day


# Example
risk = RiskManager()

print("Lot Size:", risk.calculate_lot_size(10))
print("Can Trade:", risk.can_trade(3))
