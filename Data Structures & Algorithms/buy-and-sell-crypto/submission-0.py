class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = float('inf')
        maxProf = 0

        for price in prices:

            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProf = max(maxProf, profit)

        return maxProf
