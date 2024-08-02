class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # count the number of ones
        n = len(nums)
        k = sum(nums)
        
        # hanlde edge cases
        if k == 0 or k == n:
            return 0

        # Extend the array to handle circular property
        extended_nums = nums + nums[:k-1]
        
        # Initialize the sliding window
        current_zeros = 0
        min_swaps = float('inf')
        left, right = 0, 0

        while right < len(extended_nums):
            if extended_nums[right] == 0:
                current_zeros += 1 
            
            if right - left + 1 >= k:
                # 满足了窗口大小，计算min_swaps
                min_swaps = min(min_swaps,current_zeros)
                if extended_nums[left] == 0:
                    current_zeros -= 1
                left += 1
            
            right += 1

    
        return min_swaps
