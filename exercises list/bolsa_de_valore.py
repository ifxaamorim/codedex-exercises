stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

# que encontra o preço em um determinado dia x.
def price_at(day):
    if 1 <= day <= len(stock_prices):
        return stock_prices[day - 1]
    else:
        return "Invalid day"
print(price_at(20))  

# que encontra o preço máximo do dia a ao dia b.
def max_price(a, b):
    if 1 <= a <= len(stock_prices) and 1 <= b <= len(stock_prices) and a <= b:
        return max(stock_prices[a-1:b])
    else:
        return "Invalid range"
print(max_price(1, 10))

# que encontra o preço mínimo do dia a ao dia b.
def min_price(a, b):
    if 1 <= a <= len(stock_prices) and 1 <= b <= len(stock_prices) and a <= b:
        return min(stock_prices[a-1:b])
    else:
        return "Invalid range"
print(min_price(1, 20))
