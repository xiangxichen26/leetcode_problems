class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        time = k
        ans = 0

        for i in range(len(nums)):
            if nums[i] < 0 and time > 0:
                nums[i]= -nums[i]
                time -= 1
            else: 
                break
        
        nums.sort()
        if time % 2 == 0:
            ans = sum(nums)
        else:
            nums[0] = -nums[0]
            ans = sum (nums)
        
        return ans

                