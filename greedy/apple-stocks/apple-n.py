# O(n) solution
import sys

def best_profit(prices):
    maxi = -sys.maxsize
    mini = sys.maxsize
    max_profit = -sys.maxsize

    for i, price in enumerate(prices):
        if price > maxi:
            maxi = price

        if price < mini and i < len(prices)-1:
            maxi = prices[i+1]
            mini = price

        profit = maxi - mini
        if profit > max_profit:
            max_profit = profit

    return max_profit


if __name__ == "__main__":
    prices = [int(a) for a in input().split()]
    print(best_profit(prices))
