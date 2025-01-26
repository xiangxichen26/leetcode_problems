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

    def _alg(self) -> 'None':
      self._ans._value = self._a._value + self._b._value

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
    def __init__(self, value=0):
        self._value = value if isinstance(value, int) else 0
    
    def __str__(self):
        return str(self._value)
    
    def __eq__(self, other):
        if isinstance(other, Int):
            return self._value == other._value
        return False
    

    # TC: O(n)
    # SC: O(n)
    def __add__(self, other):
        a_list = [int(digit) for digit in str(self._value)]
        b_list = [int(digit) for digit in str(other._value)]

        result = [] 
        carry = 0  

        pa = len(a_list) - 1
        pb = len(b_list) - 1

        # Loop until both numbers are processed
        while pa >= 0 or pb >= 0:
            # Get the current digit of a or 0 if pa is out of range
            va = a_list[pa] if pa >= 0 else 0
            pa -= 1  # Move the pointer to the left

            # Get the current digit of b or 0 if pb is out of range
            vb = b_list[pb] if pb >= 0 else 0
            pb -= 1  # Move the pointer to the left

            s = carry + va + vb
            carry = s // 10  
            result.append(s % 10)  

        if carry:
            result.append(carry)

        # Reverse the result to get the final sum in correct order
        result.reverse()

        # Convert the list of digits back to an integer
        return int(''.join(map(str, result)))
    
    def int(self):
        return self._value
