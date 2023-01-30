
"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that 
amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
"""
from collections import deque
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    coin_que = deque([[coin] for coin in coins]) # que has list of coins in hand for each node ([coin1, coin2, coint3 ...])
    print(coin_que)
    while coin_que:
        cur_coins = coin_que.pop()
        if sum(cur_coins) == amount:
            return cur_coins
        if len(cur_coins) < amount:
            for coin in coins:
                coin_que.append(cur_coins + [coin])
    
    return -1


"""
edge cases:
coins = []
amount = 0
"""

coins = [1]
amount = 0

print(coin_change(coins, amount))
