class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        res = 0
        
        while l < r:
            m = heights[l]
            if heights[r] < m : m = heights[r]
            area = (r - l) * m

            if area > res: res = area

            if heights[r] >= heights[l]:
                l +=1
            else: r -= 1
        
        return res






        