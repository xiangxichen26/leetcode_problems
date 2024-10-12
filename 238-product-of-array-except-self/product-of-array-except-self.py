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
        if (False):
            b = L0238(nums,ans,work,"n time n space")
        if (True):
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

        for i in range (n):
            
            product = 1
            
            for j in range (n):
                
                if j == i:
                    continue

                else:
                    product = product * self._s.getdata(j)
            
            self._s.setans(i, product)

        

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################

    def _n_time_constant_space_with_divison(self)->'None':
        n = len(self._s)
        
        product = 1
        zero_count = 0
        set_zero_flag = False

        for i in range(n):

            value = self._s.getdata(i)

            if value == 0:
                zero_count = zero_count + 1
            
            else:
                product = product * value
            
            if zero_count > 1:
                set_zero_flag = True
                break
        

        for i in range(n):

            value = self._s.getdata(i)

            if set_zero_flag or (zero_count > 0 and value != 0):
                self._s.setans(i, 0)
            elif value == 0:
                self._s.setans(i, product)
            else:
                self._s.setans(i, product//self._s.getdata(i))
        
            

    ########################################
    # TIME:THETA(N)
    # Space:THETA(N)
    #########################################
    def _n_time_n_space(self)->'None':
        n = len(self._s)
        
        left_to_right_product_list = [0] * n
        right_to_left_product_list = [0] * n

        left  = 1
        right = 1

        for i in range(n):
            value = self._s.getdata(i)
            left_to_right_product_list[i] = left * value
            left *= value

        for i in range(n - 1, -1, -1):
            value = self._s.getdata(i)
            right_to_left_product_list[i] = right * value
            right *= value
        
        for i in range(n):

            if i == 0:
                self._s.setans(i, right_to_left_product_list[1])
            
            elif i == n - 1:
                self._s.setans(i, left_to_right_product_list[n - 2])
            
            else:
                self._s.setans(i, right_to_left_product_list[i + 1] * left_to_right_product_list[i - 1])
        

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    def _n_time_1_space(self)->'None':
        n = len(self._s) 
        
        left = 1
        for i in range(n):
            value = self._s.getdata(i)
            self._s.setans(i, left * value)
            left *= value
        
        right = 1 
        for i in range(n-1,-1,-1):
            value = self._s.getdata(i)

            if i == 0:
                self._s.setans(i,right)
            
            elif i == n - 1:
                self._s.setans(i, self._s.getans(n-2))
            
            else:
                self._s.setans(i, self._s.getans(i-1) * right)
            
            right *= value



        