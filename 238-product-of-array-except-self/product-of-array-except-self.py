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
        # Uncomment the algorithm you want to test:
        if False:  # Change to True to activate Brute Force
            b = L0238(nums, ans, work, "Brute Force")
        if False:  # Change to True to activate Use Division
            b = L0238(nums, ans, work, "Use Division")
        if True:  # Change to True to activate n time n space
            b = L0238(nums, ans, work, "n time n space")
        if False:  # Change to True to activate n time 1 space
            b = L0238(nums, ans, work, "n time 1 space")
        return ans

############################################################
# You cannot change anything in L0238
###########################################################
class L0238:
    def __init__(self, a: List[int], ans: List[int], work: 'list of size 1', alg: 'string') -> None:
        self._a = a  # Data
        self._ans = ans  # answer
        self._work = work
        self._l = len(a)
        for i in range(self._l):
            self._ans.append(0)  # Data is allocated and initialized to 0
        Algorithm(self, alg)
    def __len__(self):
        return self._l

    def getdata(self, i: 'int') -> 'int':
        assert i >= 0 and i < self._l
        self._work[0] = self._work[0] + 1
        return self._a[i]

    def getans(self, i: 'int') -> 'int':
        assert i >= 0 and i < self._l
        self._work[0] = self._work[0] + 1
        return self._ans[i]

    def setans(self, i: 'int', v: 'int') -> 'None':
        assert i >= 0 and i < self._l
        self._work[0] = self._work[0] + 1
        self._ans[i] = v


class Algorithm:
    def __init__(self, s: 'L0238', alg: 'string') -> None:
        self._s = s
        if alg == "Brute Force":
            self._nsquare_time_constant_space()
        elif alg == "Use Division":
            self._n_time_constant_space_with_division()
        elif alg == "n time n space":
            self._n_time_n_space()
        elif alg == "n time 1 space":
            self._n_time_1_space()
        else:
            assert False

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
    def _n_time_constant_space_with_division(self) -> 'None':  # Fixed spelling of 'division'
        n = len(self._s)
        total_product = 1
        zero_count = 0
        zero_index = -1

        for i in range(n):
            num = self._s.getdata(i)
            if num == 0:
                zero_count += 1
                zero_index = i
            else:
                total_product *= num

        if zero_count > 1:
            for i in range(n):
                self._s.setans(i, 0)
        elif zero_count == 1:
            for i in range(n):
                self._s.setans(i, 0 if i != zero_index else total_product)
        else:
            for i in range(n):
                self._s.setans(i, total_product // self._s.getdata(i))

    ########################################
    # TIME:THETA(N)
    # Space:THETA(N)
    #########################################
    def _n_time_n_space(self) -> 'None':
        n = len(self._s)
        left_products = [1] * n
        right_products = [1] * n

        for i in range(1, n):
            left_products[i] = left_products[i - 1] * self._s.getdata(i - 1)

        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * self._s.getdata(i + 1)

        for i in range(n):
            self._s.setans(i, left_products[i] * right_products[i])

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
        ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    def _n_time_1_space(self) -> 'None':
        n = len(self._s)
        # Initialize the answer array with 1s
        for i in range(n):
            self._s.setans(i, 1)

        # Calculate left products
        left_product = 1
        for i in range(n):
            self._s.setans(i, left_product)
            left_product *= self._s.getdata(i)

        # Calculate right products and update answer
        right_product = 1
        for i in range(n - 1, -1, -1):
            self._s.setans(i, self._s.getans(i) * right_product)
            right_product *= self._s.getdata(i)
