class Solution:
    def convrtBit(self,number:int) -> str:
        ans = ""
        while number:
            temp = number % 2
            ans = str(temp) + ans
            number = number // 2
        
        return ans

    def minBitFlips(self, start: int, goal: int) -> int:
        start_bit = self.convrtBit(start)
        goal_bit = self.convrtBit(goal)

        m = len(start_bit)
        n = len(goal_bit)
        count = 0

        if m > n:
            goal_bit = "0" * (m-n) + goal_bit
        elif m < n:
            start_bit = "0" * (n-m)+ start_bit

        for i in range(len(start_bit)):
            if start_bit[i] != goal_bit[i]:
                count += 1
        
        return count

