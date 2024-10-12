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
        for i in range(n):
            p=1
            for j in range(n):
                if (i!=j):
                    p*=self._s.getdata(j)
                self._s.setans(i,p)
        

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    
    def _get_product_of_whole_array(self)->'[int,bool]':
        n = len(self._s)
        p = 1
        numzero = 0
        for i in range(n):
            v = self._s.getdata(i)
            if (v):
                p = p*v
            else:
                numzero = numzero + 1
        
        if(numzero == n):
            return [0, True] 
        
        if(numzero == 1):
            return [p, True]
        
        if(numzero > 1):
            return [0, True]
        
        return [p, False]

    def _n_time_constant_space_with_divison(self)->'None':
        n = len(self._s)
        [product, hasZero] = self._get_product_of_whole_array()
        n = len(self._s)
        for i in range(n):
            if(product == 0):
                self._s.setans(i,0)
            else:
                v = self._s.getdata(i)
                if(hasZero):
                    if(v):
                        self._s.setans(i,0)
                    else:
                        self._s.setans(i,product)
                else:
                    if(v):
                        self._s.setans(i, product//v)
                    else:
                        self._s.setans(i,0)

        
            

    ########################################
    # TIME:THETA(N)
    # Space:THETA(N)
    #########################################
    def _n_time_n_space(self)->'None':
        n = len(self._s)
        a1=[0]*n
        a2=[0]*n
        l=1
        a1[0]=1
        for i in range(1,n):
            l*=self._s.getdata(i-1)
            a1[i]=l
        r=1
        a2[n-1]=1
        for i in range(n-2,-1,-1):
            r*=self._s.getdata(i+1)
            a2[i]=r
        for i in range(n):
            self._s.setans(i,a1[i]*a2[i])
        

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    def _n_time_1_space(self)->'None':
        n = len(self._s) 
        p=1
        self._s.setans(0,1)
        self._s.setans(1,self._s.getdata(0))
        for i in range(2,n):
            self._s.setans(i,self._s.getans(i-1)*self._s.getdata(i-1)) 
        temp=self._s.getdata(n-1)
        for i in range(n-2,-1,-1):
            self._s.setans(i,self._s.getans(i)*temp) 
            temp*=self._s.getdata(i)
        