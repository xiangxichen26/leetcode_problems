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

    def _alg1(self):
        """
        Brute force approach
        """
        def backtrack(index, current_sum, current_indices):
            self._work[0] += 1
            
            # Base case: reached end of array
            if index >= len(self._a):
                if current_sum > self._maxv[0]:
                    self._maxv[0] = current_sum
                    self._ans.clear()
                    self._ans.extend(current_indices)
                    if self._show:
                        print(f"{len(current_indices)} : {current_indices} = {current_sum}")
                return
            
            # Skip current exam
            backtrack(index + 1, current_sum, current_indices)
            
            # Take current exam (if valid)
            new_indices = current_indices.copy()
            new_indices.append(index)
            if self._show:
                print(f"{len(new_indices)} : {new_indices} = {current_sum + self._a[index]}")
            backtrack(index + 2, current_sum + self._a[index], new_indices)

            '''Work Calculation Assumptions:
1. Brute Force Algorithm (_alg1):
   * Count each recursive call as 1 unit of work
   * Work increments with each state exploration regardless of whether we take or skip an exam
   * For empty arrays, set work to 1 to pass assertion'''
        
        if self._show:
            print("------- Alg 1 -----------")
            print(list(range(len(self._a))))
            print(self._a)
        backtrack(0, 0, [])
        if self._show:
            print(f"maxv = {self._maxv[0]}")
            print(f"ans = {self._ans}")
            print(f"work = {self._work[0]}")

    def _alg2(self):
        """
        Dynamic Programming approach with step logging
        """
        if self._show:
            print("------- Alg 2 -----------")
            print(list(range(len(self._a))))
            print(self._a)
            
        n = len(self._a)
        if n == 0:
            self._maxv[0] = 0
            self._ans.clear()
            self._work[0] = 1  # Set to 1 for empty array to pass assertion
            return
        
        # Initialize DP arrays
        dp = [0] * n  # dp[i] stores the max sum we can achieve up to index i
        selected_indices = [[] for _ in range(n)]  # Tracks the selected indices for dp[i]
        self._work[0] = 0
        
        # Base case: First element
        dp[0] = self._a[0]
        if self._a[0] > 0:
            selected_indices[0] = [0]
        self._work[0] += 1
        if self._show:
            print(f"1 : {selected_indices[0]} = {dp[0]}")

        '''2. Dynamic Programming Algorithm (_alg2):
   * Count initialization of base cases as 1 unit each
   * Count each position processing as 1 unit of work
   * For n elements, expect approximately n+2 work units (base cases + n-2 iterations)
   * For empty arrays, set work to 1 to pass assertion'''    
        
        # Base case: Second element
        if n > 1:
            if self._a[0] > self._a[1]:
                dp[1] = self._a[0]
                selected_indices[1] = selected_indices[0][:]
            else:
                dp[1] = self._a[1]
                if self._a[1] > 0:
                    selected_indices[1] = [1]
            self._work[0] += 1
            if self._show:
                print(f"2 : {selected_indices[1]} = {dp[1]}")
        
        # Fill the DP table
        for i in range(2, n):
            self._work[0] += 1
            old_indices = selected_indices[i-1][:] if dp[i-1] > dp[i-2] + self._a[i] else selected_indices[i-2][:]
            if dp[i - 1] > dp[i - 2] + self._a[i]:
                dp[i] = dp[i - 1]
                selected_indices[i] = selected_indices[i - 1][:]
            else:
                dp[i] = dp[i - 2] + self._a[i]
                if self._a[i] > 0:
                    selected_indices[i] = selected_indices[i - 2] + [i]
                else:
                    selected_indices[i] = selected_indices[i - 2][:]
            if self._show:
                print(f"{i+1} : {selected_indices[i]} = {dp[i]}")
        
        # The maximum value is at the last index
        self._maxv[0] = dp[-1]
        self._ans[:] = selected_indices[-1]
        
        if self._show:
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
    
 