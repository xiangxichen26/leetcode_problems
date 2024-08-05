class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_d = collections.defaultdict()
        for i in arr:
            arr_d[i] = arr_d.get(i,0) + 1
        
        for i in arr_d:
            if arr_d[i] == 1:
                k -= 1
                if k == 0 :
                    return i

        if k>0:
            return "" 
