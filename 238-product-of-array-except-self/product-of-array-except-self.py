############################################################
# L0238.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2023
###########################################################
############################################################
# All imports
###########################################################
from typing import List

############################################################
# You cannot change anything in Solution
###########################################################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        work = [0]
        ans = []
        if (False):
            b = L0238(nums,ans,work,"Brute Force")
        if (False):
            b = L0238(nums,ans,work,"Use Division")
        if (True):
            b = L0238(nums,ans,work,"n time n space")
        if (False):
            b = L0238(nums,ans,work,"n time 1 space")
        return ans

############################################################
# You cannot change anything in L0238
###########################################################
class L0238:
    def __init__(self,a: List[int],ans: List[int], work:'list of size 1', alg:'string') -> None:
        self._a = a ## Data
        self._ans = ans ## answer
        self._work = work
        self._l = len(a)
        for i in range(self._l):
            self._ans.append(0) ## Data is allocated and initialized to 0
        Algorithm(self,alg)

    def __len__(self):
        return self._l;

    def getdata(self,i:'int')->'int':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        return self._a[i]

    def getans(self,i:'int')->'int':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        return self._ans[i]

    def setans(self,i:'int',v:'int')->'None':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        self._ans[i] = v 

class Algorithm:
    def __init__(self,s:'L0238', alg:'string') -> None: 
        self._s = s
        if (alg == "Brute Force"):
            self._nsquare_time_constant_space()
        elif (alg == "Use Division"):
            self._n_time_constant_space_with_divison()
        elif (alg == "n time n space"):
            self._n_time_n_space()
        elif (alg == "n time 1 space"):
            self._n_time_1_space()
        else:
            assert(False)

    ########################################
    # WRITE CODE BELOW
    #########################################
   
    ########################################
    # TIME:THETA(NSQUARE)
    # Space:THETA(1)
    #########################################
    
    def _nsquare_time_constant_space(self):
        n = len(self._s)
        for i in range(n):
            prod = 1
            for j in range(n):
                if j != i:
                    prod = prod * self._s.getdata(j)
            self._s.setans(i, prod)
        

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################

    def _n_time_constant_space_with_divison(self)->'None':
        n = len(self._s)
        zero_count = 0
        prod = 1
        for i in range(n):
            num = self._s.getdata(i)
            if num == 0:
                zero_count += 1
            else:
                prod *= num
        if zero_count == 1:
            for i in range(n):
                if self._s.getdata(i)==0:
                    self._s.setans(i, prod)
                else:
                    self._s.setans(i, 0)
        elif zero_count > 1:
            for i in range(n):
                self._s.setans(i,0)
        else:
            for i in range(n):
                remaining_product = prod // self._s.getdata(i)
                self._s.setans(i, remaining_product)
            

    ########################################
    # TIME:THETA(N)
    # Space:THETA(N)
    #########################################
    def _n_time_n_space(self)->'None':
        n = len(self._s)
        from_left = [0] * n
        from_right = [0] * n
        prod_from_left = 1
        prod_from_right = 1
        for i in range(n):
            prod_from_left *= self._s.getdata(i)
            from_left[i] = prod_from_left
        for i in range(n-1, -1, -1):
            prod_from_right *= self._s.getdata(i)
            from_right[i] = prod_from_right
        for i in range(n):
            prod = 1
            # check for boundries
            if i > 0 and i < n-1:
                prod = from_left[i-1] * from_right[i+1]
                self._s.setans(i, prod)
            elif i == 0 and n > 1:
                self._s.setans(i, from_right[i+1])
            elif i == n - 1 and n > 1:
                self._s.setans(i, from_left[i-1])
            elif i == 1:
                self._s.setans(i, 1)


    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    def _n_time_1_space(self)->'None':
        n = len(self._s)
        prod_from_left = 1
        for i in range(n):
            self._s.setans(i, prod_from_left)
            prod_from_left *= self._s.getdata(i)
        prod_from_right = 1
        for i in range(n - 1, -1, -1):
            self._s.setans(i, self._s.getans(i) * prod_from_right)
            prod_from_right *= self._s.getdata(i)
        