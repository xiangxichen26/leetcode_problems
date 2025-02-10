class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        count = 0
        win_s = 1

        while right < len(nums):
            win_s *= nums[right]
            right += 1
            
            while left < right and win_s >= k:
                win_s //= nums[left]
                left += 1
            
            # 现在必然是一个合法的窗口，但注意思考这个窗口中的子数组个数怎么计算：
            # 比方说 left = 1, right = 4 划定了 [1, 2, 3] 这个窗口（right 是开区间）
            # 但不止 [left..right] 是合法的子数组，[left+1..right], [left+2..right] 等都是合法子数组
            # 所以我们需要把 [3], [2,3], [1,2,3] 这 right - left 个子数组都加上
            count += right - left
        
        return count