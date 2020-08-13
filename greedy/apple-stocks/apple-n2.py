# O(n^2) solution
import sys


def best_profit(prices):
    maxi = - sys.maxsize

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > maxi:
                maxi = profit

    return maxi




if __name__ == "__main__":
    prices = [int(a) for a in input().split()]
    print(best_profit(prices))
