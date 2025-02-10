class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        freqs = {}
        max_len = 0

        left = right = 0

        while right < len(s):
            freqs[s[right]] = freqs.get(s[right],0) + 1
            right += 1

            while left < right and len(freqs) > k:
                freqs[s[left]] = freqs.get(s[left],0) - 1
                if freqs[s[left]] == 0:
                    del freqs[s[left]]
                left += 1
            
            max_len = max(max_len,right-left)
        
        return max_len