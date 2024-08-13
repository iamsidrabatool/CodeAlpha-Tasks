import yfinance as yf

class Stock:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares
        self.current_price = 0
        self.total_value = 0

    def update_price(self):
        stock_info = yf.Ticker(self.symbol)
        self.current_price = stock_info.history(period="1d")['Close'].iloc[-1]
        self.total_value = self.shares * self.current_price

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol].shares += shares
        else:
            self.stocks[symbol] = Stock(symbol, shares)
        self.stocks[symbol].update_price()

    def remove_stock(self, symbol, shares):
        if symbol in self.stocks:
            if self.stocks[symbol].shares > shares:
                self.stocks[symbol].shares -= shares
            else:
                del self.stocks[symbol]

    def update_portfolio(self):
        for stock in self.stocks.values():
            stock.update_price()

    def display_portfolio(self):
        self.update_portfolio()
        print("Stock\tShares\tCurrent Price\tTotal Value")
        for stock in self.stocks.values():
            print(f"{stock.symbol}\t{stock.shares}\t{stock.current_price:.2f}\t{stock.total_value:.2f}")

    def total_value(self):
        self.update_portfolio()
        return sum(stock.total_value for stock in self.stocks.values())

# Example usage
portfolio = Portfolio()
portfolio.add_stock("AAPL", 10)
portfolio.add_stock("GOOGL", 5)
portfolio.display_portfolio()
print(f"Total Portfolio Value: {portfolio.total_value():.2f}")

portfolio.remove_stock("AAPL", 5)
portfolio.display_portfolio()
print(f"Total Portfolio Value: {portfolio.total_value():.2f}")
