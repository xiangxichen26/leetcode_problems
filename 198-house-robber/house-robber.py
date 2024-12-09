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
    #  Time Complexity: O(2^n)
    #  Space Complexity: O(n)
    ########################################################### 
    def _alg1(self):
        stepCounter = [1]
        def maxSumRec(arr, n, indices):
            # Increment work counter
            self._work[0] += 1
            # Base cases
            if n <= 0:
                return 0, []
            if n == 1:
                return arr[0], [0]
            # Recursion: pick or not pick
            pick_sum, pick_indices = maxSumRec(arr, n - 2, indices)
            self._work[0] += 1
            pick_sum += arr[n - 1]
            pick_indices = pick_indices + [n - 1]
            
            not_pick_sum, not_pick_indices = maxSumRec(arr, n - 1, indices)
            
            if pick_sum > not_pick_sum:
                
                if self._show:
                    print(stepCounter[0], " : " , pick_indices, " = ", pick_sum)
                    stepCounter[0] += 1
                    
                return pick_sum, pick_indices
            else:

                if self._show:
                    print(stepCounter[0], " : " , not_pick_indices, " = ", not_pick_sum)
                    stepCounter[0] += 1

                return not_pick_sum, not_pick_indices

        # Calculate the maximum sum and track indices
        self._maxv[0], self._ans = maxSumRec(self._a, len(self._a), [])

        
        print("----------- Alg 1 ------------")
        print(f"maxv = {self._maxv[0]}")
        print(f"ans = {self._ans}")
        print(f"work = {self._work[0]}")
        
         
        
    ############################################################
    #  Time Complexity: O(n)
    #  Space Complexity: O(1)
    ########################################################### 
    def _alg2(self):
        stepCounter = 1
        n = len(self._a)
        if n == 0:
            self._maxv[0] = 0
            self._ans = []
            self._work[0] += 1
            
            print("----------- Alg 2 ------------")
            print(f"maxv = {self._maxv[0]}")
            print(f"ans = {self._ans}")
            print(f"work = {self._work[0]}")
            return
        
        if n == 1:
            self._maxv[0] = self._a[0]
            self._ans = [0]
            self._work[0] += 1
            
            print("----------- Alg 2 ------------")
            print(f"maxv = {self._maxv[0]}")
            print(f"ans = {self._ans}")
            print(f"work = {self._work[0]}")
            return

        # DP variables
        self._work[0] += 1
        secondLast = 0
        secondLastIndices = []

        last = self._a[0]
        lastIndices = [0]
        res = 0

        # Iterate through the array
        for i in range(1, n):
            self._work[0] += 1
            
            if self._a[i] + secondLast > last:
                res = self._a[i] + secondLast
                currentIndices = secondLastIndices + [i]
            else:
                res = last
                currentIndices = lastIndices
            if self._show:
                print(stepCounter, " : " , currentIndices, " = ", res)
                stepCounter += 1
            
            secondLast = last
            secondLastIndices = lastIndices
            last = res
            lastIndices = currentIndices

        self._maxv[0] = res

        self._ans = lastIndices

        
        print("----------- Alg 2 ------------")
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
    
 