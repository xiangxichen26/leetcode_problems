class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        count = 0

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                count = 0
            else:
                if count < 2:
                    slow += 1
                    nums[slow] = nums[fast]
                    count = 2
            fast += 1
        return slow + 1
            





        