# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker!")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity

    total_investment += investment

    print("Investment:", investment)

print("Total Investment:", total_investment)