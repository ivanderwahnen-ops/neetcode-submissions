class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = {}

        nums.sort()

        for num in nums:
            cons[num+1] = 1 + cons.get(num,0)

        m = 0
        for v in cons.values():
            if m < v: m = v
        return m 
             

        