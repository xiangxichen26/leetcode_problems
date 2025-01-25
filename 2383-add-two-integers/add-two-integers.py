############################################################
# Int.py
# Implements Int object
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2025
# added to git
###########################################################


###########################################################
#  class  Int
###########################################################
class Int:
    def __init__(self, n: "Python int" = 0):
        # ONLY DATA STRUCTURE ALLOWED
        # self._positive
        # self._a
        self._positive = True
        if n < 0:
            self._positive = False
        self._a = self.build(n)

    def _get_key(self)->'List of int':
        return self._a

    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################

    #############################
    # -1986 is returned as [1, 9, 8, 6]
    # 1986  is returned as [1, 9, 8, 6]
    # -100  is returned as [1, 0, 0]
    # -0    is returned as [0]
    # TIME:O(log to base 10 of n)
    # SPACE:O(log to base 10 of n)
    #############################
    def build(self, n: "Python int") -> "list of int":
        
        if n == 0:
            return [0]
        
        start = abs(n)
        result_list = []

        while start > 0:
            result_list.append(start % 10)
            start //= 10

        result_list.reverse()

        return result_list

    #############################
        # -1986 is stored as 1 9 8 6
        # 0 1 2 3
        # 1 9 8 6
        # return int value 1986
        # TIME:O(log to base 10 of n)
        # SPACE:O(log to base 10 of n)
        #############################
    def int(self) -> "Python integer":
        result = 0

        for k in self._a:
            result = result * 10 + k

        if not self._positive:
                result = - result

        return result
    
    def __len__(self):
        return len(self._a)

    def __getitem__(self, index: int) -> int:
        return self._a[index]

    def __setitem__(self, index: int, value: int):
        if not 0 <= value <= 9:
            raise ValueError("Each digit must be between 0 and 9.")
        self._a[index] = value

    def __str__(self) -> str:
        sign = "-" if not self._positive else ""
        return sign + "".join(map(str, self._a))

    def __add__(self, other: "Int") -> "Int":
        a = self.int()
        b = other.int()
        return Int(a + b)

    def __sub__(self, other: "Int") -> "Int":
        a = self.int()
        b = other.int()
        return Int(a - b)

    def __mul__(self, other: "Int") -> "Int":
        a = self.int()
        b = other.int()
        return Int(a * b)
        

    ##############################################################
    # WRITE All private functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    ##############################################################
    def __eq__(self, other: 'Int') -> bool:
        if not isinstance(other, Int):
            return False
        return self._get_key() == other._get_key() and self._positive == other._positive

############################################################
# Exam.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################

############################################################
# NOTHING CAN BE CHANGED BELOW
###########################################################

class Solution:
    def sum(self, a: int, b: int) -> int:
        ea = a + b
        ma = Int(a)
        tma = Int(a)
        mb = Int(b)
        tmb = Int(b)
        mc = Int()
        s = Exam(ma, mb, mc)
        ans = mc.int()
        print(ea)
        print(ans)
        assert(ans == ea)
        assert(ma == tma)
        assert(mb == tmb)
        return ans

########################################
# Nothing can be changed in class Exam
########################################

class Exam:
    def __init__(self, a: 'Int', b: 'Int', ans: 'Int') -> 'None':
        # NOTHING CAN BE CHANGED BELOW
        self._a = a
        self._b = b
        self._ans = ans
        self._alg()

    def _alg(self) -> 'None':
        # when both positive or negative
        if self._a._positive == self._b._positive:
            list_a = self._a._get_key()
            list_b = self._b._get_key()

            list_a.reverse()
            list_b.reverse()

            carry = 0
            result = []

            digit_length = max(len(list_b), len(list_a))

            for i in range(digit_length):
                a_value = list_a[i] if i < len(list_a) else 0
                b_value = list_b[i] if i < len(list_b) else 0
                digit_sum = a_value + b_value + carry
                carry = digit_sum // 10
                result.append(digit_sum % 10)

            if carry > 0:
                result.append(carry)

            result.reverse()
            list_a.reverse()
            list_b.reverse()
            self._ans._a = result
            self._ans._positive = self._a._positive
        else:
            list_a = self._a._get_key()
            list_b = self._b._get_key()
            
            abs_a = abs(self._a.int())
            abs_b = abs(self._b.int())
            
            list_a.reverse()
            list_b.reverse()

            carry = 0
            result = []

            digit_length = max(len(list_b), len(list_a))



            for i in range(digit_length):
                a_value = list_a[i] if i < len(list_a) else 0
                b_value = list_b[i] if i < len(list_b) else 0
                
                if abs_a > abs_b:
                    digit_sum = a_value - b_value - carry
                else:
                    digit_sum = b_value - a_value - carry

                if digit_sum < 0:
                    digit_sum += 10
                    carry = 1
                else:
                    carry = 0

                result.append(digit_sum)

            result.reverse()
            list_a.reverse()
            list_b.reverse()
            self._ans._a = result
            self._ans._positive = self._a._positive if abs_a > abs_b else self._b._positive
