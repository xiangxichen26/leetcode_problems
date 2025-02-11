class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_length = len(part)
        
        if len(s) < part_length:
            return s

        stk = []

        for char in s:
            stk.append(char)

            if len(stk) >= len(part) and self._check_match(stk, part, part_length):
                for _ in range(part_length):
                    stk.pop()
        
        return "".join(stk)
            
    def _check_match(self, stack: list, part: str, part_length: int) -> bool:
        # Compare the top 'part_length' elements of the stack with 'part'
        return "".join(stack[-part_length:]) == part     
                
