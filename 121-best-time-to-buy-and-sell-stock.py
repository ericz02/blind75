
# we can use two pointers
# L for left which means buy
# R for right which means sell

# we scan through the array one time tofind where the lowest time to buy
# and we keep going unti we find the best time to sell


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    l, r = 0 #initalize to 0 left = buy, right = sell
    maxP = 0 # maxProfit default case

    # keep iterating through price while right pointer has not passed the end of prices
    while r < len(prices):
        # now check if this is a profitable transaction
        if prices[l] < prices[r]
            # if profitable, calculate that profit
            profit = prices[r] - prices[l]
            # potentially update our max profit but not sure so we check
            maxP = max(maxP, profit)
        # else, might not be a profitable transaction 
        else:
            # move left pointer to the lowest 
            l += r
            # move right pointer by one
            r += 1

    return maxP

        