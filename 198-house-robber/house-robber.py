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
        max_marks = 0
        best_combination = []
        self._work[0] = 0
        print("------- Alg 1 ------------")
        step = 1
        # Generate all subsets manually
        for num in range(1 << n):  # 2^n subsets
            subset = []
            for i in range(n):
                if num & (1 << i):  # Check if bit i is set in num
                    subset.append(i)
            # Check validity of subset (no consecutive indices)
            valid = True
            for j in range(1, len(subset)):
                if subset[j] - subset[j - 1] == 1:
                    valid = False
                    break
                    
            if valid:
                marks = 0
                for idx in subset:
                    marks += self._a[idx]
                self._work[0] += 1
                if self._show:
                    print(f"{step} : {subset} = {marks}")
                step += 1
                if marks > max_marks:
                    max_marks = marks
                    best_combination = subset
        self._maxv[0] = max_marks
        self._ans.clear()
        self._ans.extend(best_combination)
        print(f"maxv = {max_marks}")
        print(f"ans = {best_combination}")
        print(f"work = {self._work[0]}")
         
        
    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg2(self):
        n = len(self._a)
        if n == 0:
            self._maxv[0] = 0
            self._ans.clear()
            self._work[0] = 0
            return
        dp = [0] * n  # Max marks up to index i
        selected_indices = [[] for _ in range(n)]  # Track selected indices
        self._work[0] = 0
        print("------- Alg 2 ------------")
        for i in range(n):
            self._work[0] += 1
            if i == 0:
                dp[i] = self._a[i]
                selected_indices[i] = [i]
            elif i == 1:
                if self._a[i] > dp[i - 1]:
                    dp[i] = self._a[i]
                    selected_indices[i] = [i]
                else:
                    dp[i] = dp[i - 1]
                    selected_indices[i] = selected_indices[i - 1]
            else:
                if dp[i - 1] > dp[i - 2] + self._a[i]:
                    dp[i] = dp[i - 1]
                    selected_indices[i] = selected_indices[i - 1]
                else:
                    dp[i] = dp[i - 2] + self._a[i]
                    selected_indices[i] = selected_indices[i - 2] + [i]
            if self._show:
                print(f"{i + 1} : {selected_indices[i]} = {dp[i]}")
        self._maxv[0] = dp[-1]
        self._ans.clear()
        self._ans.extend(selected_indices[-1])
        print(f"maxv = {self._maxv[0]}")
        print(f"ans = {self._ans}")
        print(f"work = {self._work[0]}")
  
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
    
 