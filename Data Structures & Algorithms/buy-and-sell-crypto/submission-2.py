class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        smallest = prices[0]

        for i in prices:
            if res < i - smallest: 
                    res = i - smallest
            
            if i < smallest:
                smallest = i

        return res 
        