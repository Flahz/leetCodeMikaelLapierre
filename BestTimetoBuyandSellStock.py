def maxProfit(prices):
    profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit




print(maxProfit([7,6,4,3,1]))
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([2,4,1]))