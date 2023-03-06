stock_ticker = ['XYZ1', 'XYZ2', 'XYZ3', 'XYZ4']
stock_price = [34.12, 56.87, 12.45, 78.23]
stock_prices = {}
stock_prices['stock_ticker'] = stock_ticker

stock_prices['stock_price'] = stock_price
print(stock_prices)
print(stock_prices['stock_ticker'][0])
stock_prices['stock_price'][1] = 45.67
stock_ticker.append('XYZ5')
stock_price.append(99.99)
print(stock_prices)
