class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)
        p = len(nums) - 1 if a > 0 else 0
        print(p)

        while left <= right:
            # 开口向上，两端的端点一定有一个时最大值
            val_left = self.quadraticFunction(a,b,c,nums[left])
            val_right = self.quadraticFunction(a,b,c,nums[right])
            if a > 0:
                if val_left < val_right:
                    res[p] = val_right
                    right -= 1
                else:
                    res[p] = val_left
                    left += 1
                p -= 1
            else:
                if val_left < val_right:
                    res[p] = val_left
                    left += 1
                else:
                    res[p] = val_right
                    right -= 1
                p += 1
        return res


    def quadraticFunction(self, a, b, c, x):
        ans = a*(x**2) + b*x + c
        return ans
