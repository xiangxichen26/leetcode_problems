class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        window, need = {}, {}
        for c in p:
            need[c] = need.get(c,0) + 1
        
        valid = 0
        left = 0
        right = 0

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c,0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            # close window
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res