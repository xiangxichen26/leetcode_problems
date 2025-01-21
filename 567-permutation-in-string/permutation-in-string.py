class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, need = {}, {}
        for c in s1:
            need[c] = need.get(c,0) + 1
        
        left = 0
        right = 0
        valid = 0

        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] = window.get(c,0) + 1
                if window[c] == need [c]:
                    valid += 1
            
            # close the window
            while right-left >= len(s1):
                if valid == len(need):
                    return True
                
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return False

