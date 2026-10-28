class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = []
        for i in nums:
            if i in uniques:
                return True
            uniques.append(i)
        else:
            return False