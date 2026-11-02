class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, current = 0
        for num in nums:
            current = current + 1 if num else 0
            max_count = max(max_count,current)
        return max_count