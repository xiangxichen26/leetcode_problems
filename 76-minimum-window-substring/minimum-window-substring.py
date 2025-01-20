class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {} # track the frequency of each letter in the window
        need = {} # track the frequency of each letter in the t, it's also we need to cover in the window
        for i in t:
            need[i] = need.get(i,0) + 1

        left = 0
        right = 0
        valid = 0 # 记录当前window中有哪个几个字母满足了t
        start = 0 # 记录sub window的开始值
        length = float('inf')
        
        while right < len(s):
            c = s[right]
            right += 1
            # update the data in the window
            if c in need:
                window[c] = window.get(c,0) + 1
                if window[c] == need[c]:
                    valid += 1

            # close the window
            while valid == len(need):
                # update the 最小字符数串
                if right - left < length:
                    start = left
                    length = right - left
                
                d = s[left]
                left += 1
                # if d in need ,we need to update window and valid
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if length == float('inf') else s[start: start + length]