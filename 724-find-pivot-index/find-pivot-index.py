class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1
        preSum_left = [0]*(len(nums))
        preSum_right= [0]*(len(nums))

        preSum_left[left] = nums[left]
        preSum_right[right] = nums[right]
        left += 1
        right -= 1
        
        while left < len(nums):
            preSum_left[left] = preSum_left[left-1] + nums[left]
            preSum_right[right] = preSum_right[right + 1] + nums[right]

            right -= 1
            left += 1
        
        for i in range(len(nums)):
            if preSum_left[i] == preSum_right[i]:
                return i
        
        return -1




        