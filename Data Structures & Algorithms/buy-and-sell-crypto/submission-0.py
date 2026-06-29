class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pt = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if i!=j:
                    curr_pt = prices[j]-prices[i]
                    max_pt = max(max_pt,curr_pt)
        return max_pt