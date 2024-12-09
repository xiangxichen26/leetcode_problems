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











import sys  # For getting Python Version
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
    #          Brute Force Algorithm
    ########################################################### 
    def _alg1(self):
        def rob_recursive(idx, selected, current_marks):
            nonlocal max_marks, best_indices
            self._work[0] += 1  # Increment work counter
            if idx >= len(self._a):  # Base case
                if current_marks > max_marks:
                    max_marks = current_marks
                    best_indices = selected[:]
                return
        # Option 1: Skip current course
            rob_recursive(idx + 1, selected, current_marks)
        # Option 2: Take current course (skip next)
            rob_recursive(idx + 2, selected + [idx], current_marks + self._a[idx])

        if not self._a:  # Handle empty input array
            self._work[0] = 1
            self._maxv[0] = 0
            return

        max_marks = 0
        best_indices = []
        self._work[0] = 0  # Reset work counter
        rob_recursive(0, [], 0)
        self._maxv[0] = max_marks
        self._ans.clear()
        self._ans.extend(best_indices)

        if self._show:
            print(f"Work = {self._work[0]}, Max Value = {self._maxv[0]}, Selected Courses = {self._ans}")

        
    ############################################################
    #          Optimal Algorithm
    ########################################################### 
    def _alg2(self):
        n = len(self._a)
        if n == 0:
            self._work[0] = 1  # Minimal work for empty array
            self._maxv[0] = 0
            return

        self._work[0] = 0  # Reset work counter
        dp = [0] * (n + 1)
        dp_indices = [[] for _ in range(n + 1)]

        for i in range(1, n + 1):
            self._work[0] += 1  # Increment work counter
            if dp[i - 1] > self._a[i - 1] + (dp[i - 2] if i > 1 else 0):
                dp[i] = dp[i - 1]
                dp_indices[i] = dp_indices[i - 1][:]
            else:
                dp[i] = self._a[i - 1] + (dp[i - 2] if i > 1 else 0)
                dp_indices[i] = dp_indices[i - 2][:] if i > 1 else []
                dp_indices[i].append(i - 1)

        self._maxv[0] = dp[n]
        self._ans.clear()
        self._ans.extend(dp_indices[n])

        if self._show:
            print(f"Work = {self._work[0]}, Max Value = {self._maxv[0]}, Selected Courses = {self._ans}")

############################################################
# Nothing can be changed in check_result
# Note check_result is a global hanging function
###########################################################  
def check_result(a:'Python list',ans:'Python List',amax:'int',alg1_ans:'Python list',alg1_max:'int'):
    print("Checking routine will be added after exam")
    print("Be careful. May fail if not filled properly")
