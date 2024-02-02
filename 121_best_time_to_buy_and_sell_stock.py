def maxProfit(prices: list[int]) -> int:
  profit = 0
  buy = prices[0]

  for sell in prices[1:]:
    if sell > buy:
      profit = max(profit, sell - buy)
    else:
      buy = sell

  return profit

  # for i, price in enumerate(prices):
  #   # print(f"index={i}, price={price}, list{prices [i+1:]}")
  #   remainingPrices = prices[i+1:]
  #   for remainingPrice in remainingPrices:
  #     if price < remainingPrice and greatestDifference < (remainingPrice - price):
  #       greatestDifference = remainingPrice - price

prices = [7,1,5,3,6,4]

result = maxProfit(prices)

print(result)