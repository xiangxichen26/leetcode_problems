class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = collections.defaultdict()
        dict2 = collections.defaultdict()

        res = []

        for i in nums1:
            dict1[i] = dict1.get(i,0)+1
        for i in nums2:
            dict2[i] = dict2.get(i,0)+1

        for i in dict1:
            if i in dict2:
                res.append(i)
        
        return res
            