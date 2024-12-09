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
        self._ans.clear()
        self._maxv[0] = 0
        self._work[0] = 0
 
        def helper(index, selected, currSum):
            self._work[0] += 1  # incrementing work everytime the function is called
            if index >= n:
                if currSum > self._maxv[0]:
                    self._maxv[0] = currSum
                    self._ans[:] = selected[:]
                return
            # skipping current index
            helper(index + 1, selected, currSum)
            # choosing current index
            if not selected or selected[-1] != index - 1:
                helper(index + 1, selected + [index], currSum + self._a[index])
 
        helper(0, [], 0)
 
        if self._show:
            print("======= Algorithm 1 =======")
            print("Maximum Value, maxv:", self._maxv[0])
            print("Selected Indices, ans:", self._ans)
            print("Work Done (Steps), work:", self._work[0])
            print("===========================")
        
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
                print("======= Algorithm 2 =======")
                print("Maximum Value:", self._maxv[0])
                print("Selected Indices:", self._ans)
                print("Work Done (Steps):", self._work[0])
                print("===========================")
            return

        self._work[0] = 0

        # to store max values and their indices
        prev1_max = 0  # max value at i-1
        prev2_max = 0  # max value at i-2
        prev1_indices = []  # indices for i-1
        prev2_indices = []  # indices for i-2


        for i in range(n):
            self._work[0] += 1  # incrementing work counter for each index
            
            if prev1_max > prev2_max + self._a[i]:
                # skipping current index
                current_max = prev1_max
                current_indices = prev1_indices[:]
            else:
                # including the current index if it improves the sum
                current_max = prev2_max + self._a[i]
                current_indices = prev2_indices + [i]

            # updating previous values for the next iteration
            prev2_max, prev2_indices = prev1_max, prev1_indices
            prev1_max, prev1_indices = current_max, current_indices

        # assigning the final maximum value and selected indices
        self._maxv[0] = prev1_max
        self._ans[:] = prev1_indices

        # ensuring we include only contributing indices
        self._ans = [idx for idx in self._ans if self._a[idx] > 0]

        if self._show:
            print("======= Algorithm 2 =======")
            print("Maximum Value, maxv:", self._maxv[0])
            print("Selected Indices, ans:", self._ans)
            print("Work Done (Steps), work:", self._work[0])
            print("===========================") 
        
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
    
 