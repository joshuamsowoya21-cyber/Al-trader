# AITrader Market Data Module

class MarketData:
    def __init__(self):
        self.symbol = "XAUUSD"
        self.price = 0.0

    def update_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

# Example
market = MarketData()
market.update_price(3350.25)

print("Symbol:", market.symbol)
print("Current Price:", market.get_price())
