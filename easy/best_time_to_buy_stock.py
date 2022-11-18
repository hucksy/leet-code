from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_tuple = tuple(prices)
        max_profit = 0
        max_buyin = 0
        for i in range(len(price_tuple)-1):
            for i2 in range(i, len(price_tuple)):
                current_profit = price_tuple[i2] - price_tuple[i]
                print(f"i2 = {i2}, current_profit = {current_profit}")
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
prices3 = [1,2]
new_soltion = Solution()
print(new_soltion.maxProfit(prices1))
# print(new_soltion.maxProfit(prices2))
# print(new_soltion.maxProfit(prices3))
