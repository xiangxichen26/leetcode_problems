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
        def helper(i, selected, total):
            self._work[0] += 1
            if self._show:
                print(f"Brute step {self._work[0]}: i={i}, selected={selected}, total={total}")
            if i >= len(self._a):
                return (total, selected[:])
            # Option 1: take current
            take_total, take_sel = helper(i + 2, selected + [i], total + self._a[i])
            # Option 2: skip current
            skip_total, skip_sel = helper(i + 1, selected, total)
            if take_total > skip_total:
                return (take_total, take_sel)
            else:
                return (skip_total, skip_sel)
    
        maxval, result = helper(0, [], 0)
        self._maxv[0] = maxval
        self._ans.extend(result)
        if self._show:
            print("Brute Force Result:")
            print("Max Value:", maxval)
            print("Selected Indices:", result)
    ############################################################
    #          WRITE CODE BELOW
    def _alg2(self):
        n = len(self._a)
        if n == 0:
            self._maxv[0] = 0
            return
    
        dp = [0] * n
        pick = [[] for _ in range(n)]
    
        dp[0] = self._a[0]
        pick[0] = [0]
        self._work[0] += 1
        if self._show:
            print(f"DP step {self._work[0]}: dp[0]={dp[0]}, pick[0]={pick[0]}")
    
        if n >= 2:
            self._work[0] += 1
            if self._a[1] > self._a[0]:
                dp[1] = self._a[1]
                pick[1] = [1]
            else:
                dp[1] = self._a[0]
                pick[1] = [0]
            if self._show:
                print(f"DP step {self._work[0]}: dp[1]={dp[1]}, pick[1]={pick[1]}")
    
        for i in range(2, n):
            self._work[0] += 1
            if dp[i - 1] > dp[i - 2] + self._a[i]:
                dp[i] = dp[i - 1]
                pick[i] = pick[i - 1][:]
            else:
                dp[i] = dp[i - 2] + self._a[i]
                pick[i] = pick[i - 2] + [i]
            if self._show:
                print(f"DP step {self._work[0]}: dp[{i}]={dp[i]}, pick[{i}]={pick[i]}")
    
        self._maxv[0] = dp[-1]
        self._ans.extend(pick[-1])
        if self._show:
            print("DP Result:")
            print("Max Value:", self._maxv[0])
            print("Selected Indices:", self._ans)

  
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
 