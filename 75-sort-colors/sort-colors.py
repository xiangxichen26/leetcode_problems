class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0，p0) 是元素 0 的区间，(p2, nums.length - 1] 是 2 的区间
        p0 = 0
        p2 = len(nums) - 1
        p = 0

        while p <= p2:
            if nums[p] == 0:
                nums[p0],nums[p] = nums[p],nums[p0]
                p0 += 1
            elif nums[p] == 2:
                nums[p2],nums[p] = nums[p],nums[p2]
                p2 -= 1
                p -= 1
            p += 1