class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        preSum = 0
        preSum_to_index = {}
        preSum_to_index[0] = -1
        max_len = 0

        for i, hour in enumerate(hours):
            preSum += 1 if hour > 8 else -1

            if preSum > 0:
                max_len = max(max_len, i + 1)
            
            else:
                # preSum[i] 为负，需要寻找一个 j 使得 preSum[i] - preSum[j] > 0
                # 考虑到我们的 preSum 数组每两个相邻元素的差的绝对值都是 1 且 j 应该尽可能小，
                # 那么只要找到 preSum[j] == preSum[i] - 1，nums[j+1..i] 就是一个「表现良好的时间段」
                if preSum - 1 in preSum_to_index:
                    max_len = max(max_len, i - preSum_to_index[preSum - 1])

            
            if preSum not in preSum_to_index: 
                preSum_to_index[preSum] = i
        
        return max_len

            

        