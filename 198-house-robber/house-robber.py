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
        if (len(self._a) < 16):
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
        self._ans.clear()
        self._maxv[0] = 0
        self._work[0] = 0

        def calculate_max_sum(idx, selected, current_sum):
            # Increment work count
            self._work[0] += 1 
            print(f"Step {self._work[0]}: idx = {idx}, selected = {selected}, current_sum = {current_sum}")
 
            if idx >= n:
                if current_sum > self._maxv[0]:
                    print(f"Updating _maxv from {self._maxv[0]} to {current_sum}, _ans to {selected}")
                    self._maxv[0] = current_sum
                    self._ans[:] = selected[:]
                return
            # Skip current index
            calculate_max_sum(idx + 1, selected, current_sum)
            # Take current index if possible
            if not selected or selected[-1] != idx - 1:
                calculate_max_sum(idx + 1, selected + [idx], current_sum + self._a[idx])

        calculate_max_sum(0, [], 0)

        if self._show:
            print("---------- Algorithm 1 -----------")
            print("---------- Brute Force -----------")
            print(f"Max Value (_maxv) = {self._maxv[0]}")
            print(f"Ans (_ans) = {self._ans}")
            print(f"Work (_work) = {self._work[0]}")
         
        
    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg2(self):
        n = len(self._a)
        if n == 0:
            self._maxv[0] = 0
            self._ans.clear()
            self._work[0] = 1
            if self._show:
                print("---------- Algorithm 2 -----------")
                print("---------- Optimized Approach -----------")
                print(f"Max Value (_maxv) = {self._maxv[0]}")
                print(f"Ans (_ans) = {self._ans}")
                print(f"Work (_work)  = {self._work[0]}")
            return

        max_sum = [0] * n
        chosen_indices = [[] for _ in range(n)]
        self._work[0] = 0

        # Base cases
        max_sum[0] = self._a[0]
        chosen_indices[0] = [0]
        self._work[0] += 1

        if n > 1:
            max_sum[1] = max(self._a[0], self._a[1])
            chosen_indices[1] = [0] if self._a[0] > self._a[1] else [1]
            self._work[0] += 1

        # Fill max_sum table
        for i in range(2, n):
            self._work[0] += 1
            if max_sum[i - 1] >= max_sum[i - 2] + self._a[i]:
                max_sum[i] = max_sum[i - 1]
                chosen_indices[i] = chosen_indices[i - 1][:]
            else:
                max_sum[i] = max_sum[i - 2] + self._a[i]
                chosen_indices[i] = chosen_indices[i - 2] + [i]

        self._maxv[0] = max_sum[-1]
        self._ans[:] = chosen_indices[-1]

        if self._show:
            print("---------- Algorithm 2 -----------")
            print("---------- Optimized Approach -----------")
            print(f"Max Value (_maxv) = {self._maxv[0]}")
            print(f"Ans (_ans) = {self._ans}")
            print(f"Work (_work) = {self._work[0]}")
  
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
    
 