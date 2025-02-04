class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1

        if len(nums) < 2:
            return len(nums)

        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            else:
                fast += 1
        
        return slow + 1 
        