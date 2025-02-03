class Solution:
    def twoSumTarget(self, nums, start, target):
        lo = start
        hi = len(nums) - 1
        res = []

        while lo < hi:
            s = nums[lo] + nums[hi]
            left = nums[lo]
            right = nums[hi]

            if s < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif s > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1   
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left: 
                    lo += 1
                while lo < hi and nums[hi] == right: 
                    hi -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            tuples = self.twoSumTarget(nums, i + 1, 0 - nums[i])

            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)
        return res


        

        
        