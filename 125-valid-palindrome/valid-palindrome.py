class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        sb = []
        for c in s:
            if c.isalnum():
                sb.append(c.lower())
        
        s = ''.join(sb)
        
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True



        