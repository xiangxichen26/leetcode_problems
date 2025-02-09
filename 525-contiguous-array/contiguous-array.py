class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = 0
        preSum_to_index = {}
        preSum_to_index[0] = -1

        res = 0
        for i, num in enumerate(nums):
            # 如果这个前缀和还没有对应的索引，说明这个前缀和第一次出现，记录下来
            preSum += num if num==1 else -1
            if preSum not in preSum_to_index:
                preSum_to_index[preSum] = i
            else:
                # 这个前缀和已经出现过了，则找到一个和为 0 的子数组
                res = max(res, i - preSum_to_index[preSum])
            # 因为题目想找长度最大的子数组，所以前缀和索引应尽可能小
        return res
        