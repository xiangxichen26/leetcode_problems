 ############################################################
#  AFTER EXAM DELETE CODE BELOW AND ADD GIVEN CODE
###########################################################  

############################################################
#  class  Solution
# Nothing can be changed in Solution
###########################################################    
class Solution():
    def rob(self, nums:'Python list') -> 'int':
        #Nothing can be changed here
        ans = []
        maxv = [0]
        work = [0]
        t = Alg(nums,ans,maxv,work,False)
        return maxv[0]

############################################################
# Nothing can be changed in check_result
# Note check_result is a global hanging function
###########################################################  
def check_result(a:'Python list',ans:'Python List',amax:'int',alg1_ans:'Python list',alg1_max:'int'):
    if (alg1_max):
        #alg1 did not run
        if (alg1_max != amax):
          print("alg1 max=", alg1_max)
          print("alg2 max=", amax)
          assert(False)

        x = sorted(alg1_ans)
        y = sorted(ans)
    x = sorted(ans)
    t = 0
    for e in x:
        t = t + a[e]
    assert(t == amax)
    # assert you did not break the rule
    lx = len(x)
    for i in range(0,lx-1,2):
        pos1 = x[i]
        pos2 = x[i +1]
        assert(pos2 >= (pos1+1))













############################################################
# Exam.py 
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################

############################################################
#  All imports here
###########################################################

############################################################
#  class  Alg
###########################################################    
class Alg():
    def __init__(self,a:'python list',ans:'python list',maxv:'list of size 1',work:'list of size 1',show:'bool'):
        ## Nothing can be changed below
        self._a = a
        self._ans = ans
        self._maxv = maxv
        self._work = work
        self._show = show
        self._exam() #Everything happens in _exam
        
    ############################################################
    #          Nothing can be changed in _exam
    ########################################################### 
    def _exam(self):
        alg1_ans = []
        alg1_max = [0]
        if (len(self._a) < 25):
          self._alg1()
          assert(self._work[0])
          #your answer is checked here after exam
          check_result(self._a,self._ans,self._maxv[0],alg1_ans,alg1_max[0]) 
          
          for e in self._ans:
            alg1_ans.append(e)
          alg1_max[0] = self._maxv[0]
          self._ans.clear()
          
          self._maxv[0] = 0 
          self._work[0] = 0

        #always run alg2
        self._alg2()
        assert(self._work[0])
        #your answer is checked here after exam
        check_result(self._a,self._ans,self._maxv[0],alg1_ans,alg1_max[0]) 

    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg1(self):
        n = len(self._a)
        a = self._a
        def generate_combinations(index, current_combination):
            self._work[0] += 1
            if index >= n:
                subset_sum = sum(a[i] for i in current_combination)
                if self._show:
                    print(f"{current_combination} = {subset_sum}")
                return
        
            generate_combinations(index + 2, current_combination + [index])
            generate_combinations(index + 1, current_combination)
        
        generate_combinations(0, [])
        def helper(index):
            if index < 0:
                return (0, [])
            
            include_sum, include_indices = helper(index - 2)
            include_sum += a[index]
            include_indices = include_indices + [index]
            
            exclude_sum, exclude_indices = helper(index - 1)
            
            if include_sum > exclude_sum:
                return include_sum, include_indices
            else:
                return exclude_sum, exclude_indices
        
        total, indices = helper(n - 1)
        self._maxv[0] = total
        self._ans.extend(indices)

        if self._show:
            print('----------------------------------------------')
            print('Algorithm - 1 (Brute Force)')
            print("Complexity Time: O(2^n * n) Space:O(n)")
            print('----------------------------------------------')
            print(f"maxv={self._maxv[0]}, ans={self._ans}, work={self._work[0]}")    
            print('----------------------------------------------')
    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg2(self):
        n = len(self._a)
        if n == 0:
            self._maxv[0] = 0
            self._work[0] += 1
            return
        elif n == 1:
            self._maxv[0] = self._a[0]
            self._ans.append(0)
            self._work[0] += 1
            return

        dp = [0] * n
        prev = [-1] * n

        dp[0] = self._a[0]
        dp[1] = max(self._a[0], self._a[1])
        prev[0] = -1
        prev[1] = 0 if self._a[0] >= self._a[1] else -1
        self._work[0] += 2

        for i in range(2, n):
            self._work[0] += 1
            if dp[i-1] > dp[i-2] + self._a[i]:
                dp[i] = dp[i-1]
                prev[i] = prev[i-1]
            else:
                dp[i] = dp[i-2] + self._a[i]
                prev[i] = i-2

        self._maxv[0] = dp[-1]
        self._ans.clear()
        i = n - 1
        indices = []

        while i >= 0:
            self._work[0] += 1
            if i == 0:
                indices.append(0)
                break
            if dp[i] == dp[i-1]:
                i -= 1
            else:
                indices.append(i)
                i -= 2

        indices.reverse()
        self._ans.extend(indices)

        if self._show:
            print('----------------------------------------------')
            print('Algorithm - 2')
            print("Complexity Time: O(n) Space:O(n)")
            print('----------------------------------------------')
            print(f"{indices} : {self._maxv[0]}")
            print(f"maxv={self._maxv[0]}, ans={self._ans}, work={self._work[0]}")
            print('----------------------------------------------')

        self._work[0] += 1
  
 ############################################################
#  AFTER EXAM DELETE CODE BELOW AND ADD GIVEN CODE
###########################################################  

############################################################
# Nothing can be changed in check_result
# Note check_result is a global hanging function
###########################################################  
def check_result(a:'Python list',ans:'Python List',amax:'int',alg1_ans:'Python list',alg1_max:'int'):
    print("Checking routine will be added after exam")
    print("Be careful. May fail if not filled properly")
    
 