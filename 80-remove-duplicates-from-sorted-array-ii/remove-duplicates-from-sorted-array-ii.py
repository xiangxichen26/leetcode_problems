class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        count = 0
        n = len(nums) 

        if n <= 2:
            return n
        

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                # store the element
                slow += 1
                nums[slow] = nums[fast]
                count = 0
            else:
                if count < 2:
                    # store the element
                    slow += 1
                    nums[slow] = nums[fast]
                    # count = 2
                    count = 2
            fast += 1 
        
        return slow + 1





        