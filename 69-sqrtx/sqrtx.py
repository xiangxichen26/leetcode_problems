class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 1
        right = x // 2

        while left <= right:
            mid = left + (right-left) // 2
            guess = mid * mid
            if guess == x:
                return mid
            elif guess < x:
                left = mid + 1
            elif guess > x:
                right = mid - 1
        
        return right // 1