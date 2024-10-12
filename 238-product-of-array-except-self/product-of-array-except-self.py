############################################################
# All imports
###########################################################
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        work = [0]
        ans = []
        if (False):
            b = L0238(nums,ans,work,"Brute Force")
        if (True):
            b = L0238(nums,ans,work,"Use Division")
        if (False):
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
            product = 1
            for j in range(n):
                if i != j:
                    product *= self._s.getdata(j)
            self._s.setans(i, product)
    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################

    def _n_time_constant_space_with_divison(self)->'None':
        n = len(self._s)
        total_product = 1
        zero_count = 0

        # Calculate the total product of non-zero elements and count zeros
        for i in range(n):
            num = self._s.getdata(i)
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        # Fill in the answer array
        for i in range(n):
            num = self._s.getdata(i)
            if zero_count > 1:
                self._s.setans(i, 0)  # More than one zero, all products are zero
            elif zero_count == 1:
                if num == 0:
                    self._s.setans(i, total_product)  # Only the zero element gets total product
                else:
                    self._s.setans(i, 0)  # Other elements with a zero present
            else:
                self._s.setans(i, total_product // num)  # No zeros, use division


    ########################################
    # TIME:THETA(N)
    # Space:THETA(N)
    #########################################
    def _n_time_n_space(self)->'None':
        n = len(self._s)
        left = [1] * n
        right = [1] * n

        # Calculate left products
        for i in range(1, n):
            left[i] = left[i - 1] * self._s.getdata(i - 1)

        # Calculate right products
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * self._s.getdata(i + 1)

        # Calculate final answer by multiplying left and right products
        for i in range(n):
            self._s.setans(i, left[i] * right[i])


    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    def _n_time_1_space(self)->'None':
        n = len(self._s)
        left_product = 1

        # Use the ans array to store the left products
        for i in range(n):
            self._s.setans(i, left_product)
            left_product *= self._s.getdata(i)

        right_product = 1

        # Multiply by right products
        for i in range(n - 1, -1, -1):
            self._s.setans(i, self._s.getans(i) * right_product)
            right_product *= self._s.getdata(i)
