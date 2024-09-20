class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = collections.defaultdict()
        
        for i in s:
            dicts[i] = dicts.get(i,0) + 1
           
        for i in t:
            if i not in dicts:
                return False
            else:
                dicts[i] = dicts.get(i) - 1
                if dicts[i] == 0:
                    del dicts[i]

        if dicts:
            return False
        else:
            return True
                