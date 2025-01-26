############################################################
# Exam.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2025
###########################################################

############################################################
# All imports
##############################################5#############
#from Int import *

############################################################
#  NOTHING CAN BE CHANGED BELOW
###########################################################
class Solution:
    def sum(self, a: int, b: int) -> int:
        ma = Int(a)
        ma1 = Int(a)
        mb = Int(b)
        mb1 = Int(b)
        mc = Int()
        s = Exam(ma,mb,mc)
        assert(ma == ma1)
        assert(mb == mb1)
        ans = mc.int()
        return ans

########################################
#Nothing can be changed in class Exam
########################################
class Exam:
    def __init__(self, a:'Int', b:'Int', ans:'Int')->'None':
      #NOTHING CAN BE CHANGED BELOW
      self._a = a
      self._b = b
      self._ans = ans 
      self._alg()

    def _alg(self)->'None':
      self._ans._set_value(self._a + self._b)
    # Time Complexity: Θ(log n)
    # Space Complexity: Θ(log n) 


############################################################
# Int.py
# Implements Int object
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2025
# added to git
###########################################################

############################################################
# All imports
###########################################################
import copy  #For deepcopy

###########################################################
#  class  Int
# Write class Int
###########################################################
class Int:
    def __init__(self, n: "Python int" = 0):
        self._positive = True
        if n < 0:
            self._positive = False
        self._a = self.build(n)

    def _get_key(self)->"List of int":
        return self._a

    def build(self, n: "Python int") -> "list of int":
        if n < 0:
            n = -n
        l = []
        if n < 10:
            l.append(n)
        else:
            while n != 0:
                l.append(n % 10)
                n = n // 10
        self._reverse(l)
        return l
        
    def int(self) -> "Python integer":
        v = 0
        for e in self._a:
            v = 10 * v + e
        if v == 0 or self._positive:
            return v
        return -v
    
    def _set_value(self, other: "Int") -> "None":
        self._a = other._a
        self._positive = other._positive

    def __len__(self) -> "int":
        return len(self._a)
    
    def __str__(self) -> "String":
        n = self.int()
        sign = "-"
        if self._positive:
            sign = "+"

        s = str(n)
        return s

    def _reverse(self, l: "list of int") -> "None":
        i = 0
        j = len(l) - 1
        while i < j:
            t = l[i]
            l[i] = l[j]
            l[j] = t
            i = i + 1
            j = j -1

    def __getitem__(self, pos) -> "int":
        n = len(self)
        assert pos >= 0 and pos < n
        return self._a[pos]

    def __setitem__(self, pos, v) -> "None":
        n = len(self)
        assert pos >= 0 and pos < n
        self._a[pos] = v

    def __eq__(self, other: "Int") -> "bool":
        return self.int() == other.int() and self._positive == other._positive
    
    def __gt__(self, other: "Int") -> "bool":
        return self.int() > other.int()

    def _ripple_carry_adder(self, b: "Int") -> "Int":
        l = []
        a = self
        pa = len(a) - 1
        pb = len(b) - 1
        
        carry = 0
        while (pa >= 0 or pb >= 0):
            va = 0
            if (pa >= 0):
                va = a[pa]
                pa = pa - 1
            vb = 0
            if (pb >= 0):
                vb = b[pb]
                pb = pb - 1
            s = carry + va + vb
            assert(s >= 0 and s < 20)
            carry = 0
            if (s >= 10):
                carry = 1
            l.append(s % 10)
        if (carry):
            l.append(carry)
        self._reverse(l)
        c = Int(0)
        c._a = l
        return c

    def __add__(self, b:"Int") -> "Int":
        if (self._positive and b._positive):
            r = self._ripple_carry_adder(b)
        elif (self._positive == False and b._positive == False):
            r = self._ripple_carry_adder(b)
            r._positive = False
        else:
            if (self._positive == True and b._positive == False):
                b._positive = True
                if self > b:
                    r = self.__sub__(b)
                else:
                    r = b.__sub__(self)
                    r._positive = False
                b._positive = False
            else:
                self._positive = True
                if self > b:
                    r = self.__sub__(b)
                    r._positive = False
                else:
                    r = b.__sub__(self)
                self._positive = False
        return r
    
    def __sub__(self, b: "Int") -> "Int":
        
        a = self
        result_digits = []
        borrow = 0

        if a < b:
            tem = a
            a = b
            b = tem

        pa = len(a) - 1
        pb = len(b) - 1

        while pa >= 0 or pb >= 0:
            va = 0
            if pa >= 0:
                va = a[pa]
                pa -= 1

            vb = 0
            if pb >= 0:
                vb = b[pb]
                pb -= 1

            diff = va - vb - borrow

            if diff < 0:  
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result_digits.append(diff)

        self._reverse(result_digits)

        c = Int(0)
        c._a = result_digits
        return c

