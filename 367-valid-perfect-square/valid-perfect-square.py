class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left = 2
        right = num // 2

        while left <= right:
            mid = left + (right - left) // 2
            guess = mid * mid

            if guess == num:
                return True
            elif guess < num:
                left = mid + 1
            elif guess > num:
                right = mid - 1
        
        return False
