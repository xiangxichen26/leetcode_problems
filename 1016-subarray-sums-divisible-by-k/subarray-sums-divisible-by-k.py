class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # this questions equals to find get the total number of the sub arrays that the sum of the subarray is the multiples of the k
        preSum = 0
        mod_to_index = {0:1}
        count = 0

        for i,num in enumerate(nums):
            preSum += num
            need = preSum % k

            if need in mod_to_index:
                count += mod_to_index[need]
            
            mod_to_index[preSum % k] = mod_to_index.get(preSum % k,0) + 1
        return count
        