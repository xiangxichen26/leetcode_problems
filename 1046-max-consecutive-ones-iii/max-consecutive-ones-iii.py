class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zero = 0
        max_len = 0

        left = right = 0
        
        while right < len(nums):
            if nums[right] == 0:
                count_zero += 1
            
            right += 1

            # close the window
            while left < right and count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
            
            max_len = max(max_len, right - left)
        
        return max_len
        