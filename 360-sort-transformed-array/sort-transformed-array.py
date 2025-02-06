class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []

        for i in nums:
            temp = a *(i*i) + b*i + c
            res.append(temp)
        
        res.sort()

        return res
        