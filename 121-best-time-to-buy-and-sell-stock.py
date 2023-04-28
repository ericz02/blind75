class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0  #initialize left and right pointers to 0
        maxP = 0  #initialize maxProfit to 0

        # keep iterating through price while right pointer has not passed the end of prices
        while r < len(prices):
            # now check if this is a profitable transaction
            if prices[l] < prices[r]:
                # if profitable, calculate that profit
                profit = prices[r] - prices[l]
                # potentially update our max profit but not sure so we check
                maxP = max(maxP, profit)
            # else, might not be a profitable transaction 
            else:
                # move left pointer to the lowest 
                l = r
            # move right pointer by one
            r += 1

        return maxP
