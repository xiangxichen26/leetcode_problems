class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        modulo = 10**9 + 7
        all_sums = []
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum = (current_sum+nums[end]) % modulo
                all_sums.append(current_sum)

        all_sums.sort()

        ans = 0
        for i in range(left-1,right):
            ans += all_sums[i]
        
        return ans % modulo
