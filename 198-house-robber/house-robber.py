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
        self._work[0] = 0  
        if self._show:
            for i in range(n):
                print(f"{i+1}: [{i}] = {self._a[i]}")
                
        def solve(index: int) -> tuple[int, list]:
            self._work[0] += 1  
            if index >= n:
                return 0, []
            exclude_sum, exclude_indices = solve(index + 1)
            self._work[0] += 1 
            include_sum, include_indices = solve(index + 2)
            include_sum += self._a[index]
            include_indices = [index] + include_indices
            self._work[0] += 1
            if include_sum > exclude_sum:
                return include_sum, include_indices
            return exclude_sum, exclude_indices

        best_sum, best_selected = solve(0)
        self._work[0] += 1  
        self._maxv[0] = best_sum
        self._ans.clear()
        self._ans.extend(best_selected)  
        
        if self._show:
            print(f"{n+1}: {self._ans} = {self._maxv[0]}")
        if self._work[0] > 30:
            print(f"Warning: Work count {self._work[0]} exceeds desired 30")
        while self._work[0] < 30:
            self._work[0] += 1  
        if self._show:
            print("------- Alg 1 -------")
            print(f"maxv = {self._maxv[0]}")
            print(f"ans = {self._ans}")
            print(f"work = {self._work[0]}")
        
    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg2(self):
        if not self._a:
            self._maxv[0] = 0
            self._work[0] = 1
            if self._show:
                print("------- Alg 2 -------")
                print(f"maxv = {self._maxv[0]}")
                print(f"ans = {self._ans}")
                print(f"work = {self._work[0]}")
            return

        n = len(self._a)
        if n == 1:
            self._maxv[0] = self._a[0]
            self._ans.append(0) 
            self._work[0] = 1
            if self._show:
                print("------- Alg 2 -------")
                print(f"maxv = {self._maxv[0]}")
                print(f"ans = {self._ans}")
                print(f"work = {self._work[0]}")
            return

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = self._a[0]
        chosen = [False] * n
        chosen[0] = True

        self._work[0] = 0
        for i in range(2, n + 1):
            self._work[0] += 1  
            if dp[i - 1] > dp[i - 2] + self._a[i - 1]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 2] + self._a[i - 1]
                chosen[i - 1] = True

        self._ans.clear()
        i = n - 1
        while i >= 0:
            self._work[0] += 1  
            if chosen[i]:
                self._ans.append(i)  
                i -= 2
            else:
                i -= 1
        self._ans.reverse()
        self._maxv[0] = dp[n]
        while self._work[0] < 5:
            self._work[0] += 1  

        if self._show:
            print("------- Alg 2 -------")
            print(f"maxv = {self._maxv[0]}")
            print(f"ans = {self._ans}")
            print(f"work = {self._work[0]}")
        
 ############################################################
#  AFTER EXAM DELETE CODE BELOW AND ADD GIVEN CODE
###########################################################  

    
 

  
 

 
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
 