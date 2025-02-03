class Solution:
    # n 填写想求的是几数之和，start 从哪个索引开始计算（一般填 0），target 填想凑出的目标和
    def nSumTarget(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        size = len(nums)
        res = []
        if n < 2 or size < n:
            return res
        
        if n == 2:
            lo, hi = start, size - 1
            while lo < hi:
                left, right = nums[lo], nums[hi]
                s = left + right
                if s < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif s > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    res.append([left,right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
        else:
            # n > 2 时，递归计算 (n-1)Sum 的结果
            for i in range(start, size):
                # 跳过重复值
                if i > start and nums[i] == nums[i-1]:
                    continue
                sub = self.nSumTarget(nums, n-1, i+1, target-nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
        
        return res


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.nSumTarget(nums, 3, 0, 0)



        

        
        