class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        behind_you = prices[0]
        res = 0
        smallest = prices[0]

        for i in prices:
            if i > behind_you:
                if behind_you < smallest: smallest = behind_you
                if res < i - smallest: 
                    res = i - smallest
            behind_you = i

        return res 
        