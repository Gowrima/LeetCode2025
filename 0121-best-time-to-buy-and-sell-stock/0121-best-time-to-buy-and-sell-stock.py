class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_profit, max_profit = 0, 0
        i, j = 0, 1

        while j<len(prices):
            if prices[i] > prices[j]:
                i += 1
                j = i+1
            else:
                cur_profit = prices[j] - prices[i]
                j += 1
            
            if cur_profit > max_profit:
                max_profit = cur_profit
            
        return max_profit
            

