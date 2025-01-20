class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return 1

        left = 0
        right = 0
        while right < n:
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left],nums[right] = nums[right], nums[left]
                right += 1
        
        return left+1

        