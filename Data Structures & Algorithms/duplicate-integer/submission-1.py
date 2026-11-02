class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(nums[i-1]) > 1:
                return True
        return False