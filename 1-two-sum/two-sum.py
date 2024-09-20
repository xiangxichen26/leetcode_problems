class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()             
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)