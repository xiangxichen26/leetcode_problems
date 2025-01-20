class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        slow = 0
        fast = 0

        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
        
        return slow

