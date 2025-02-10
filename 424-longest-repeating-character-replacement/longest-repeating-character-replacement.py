class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        freqs = defaultdict(int)
        res = 0 


        while right < len(s):
            freqs[s[right]] += 1
            right += 1
            maxFreq = max(freqs.values())

            while left < right and right - left - maxFreq > k:
                freqs[s[left]] -= 1
                left += 1
            
            res = max(res,right-left)
        
        return res
