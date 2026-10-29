class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        
        result = sorted(frequency, key = lambda k: frequency[k])

        
        return result[len(result)-k:]
