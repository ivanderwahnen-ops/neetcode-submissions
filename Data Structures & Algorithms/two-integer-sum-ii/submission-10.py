class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0

        for n in range(len(numbers)):
            while numbers[n] + numbers[len(numbers) - 1 - l] > target:
                l += 1
            if numbers[n] + numbers[len(numbers) - 1 - l] == target:
                return [n+1,len(numbers) - l]
            l = 0
