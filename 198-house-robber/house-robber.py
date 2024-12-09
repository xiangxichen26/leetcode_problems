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
    def __init__(self, a: 'python list', ans: 'python list', maxv: 'list of size 1', work: 'list of size 1', show: 'bool'):
        ## Nothing can be changed below
        self._a = a
        self._ans = ans
        self._maxv = maxv
        self._work = work
        self._show = show
        self._exam()  # Everything happens in _exam

    ############################################################
    #          Nothing can be changed in _exam
    ########################################################### 
    def _exam(self):
        alg1_ans = []
        alg1_max = [0]
        if len(self._a) < 25:
            self._alg1()
            assert self._work[0]
            # your answer is checked here after exam
            check_result(self._a, self._ans, self._maxv[0], alg1_ans, alg1_max[0])
            for e in self._ans:
                alg1_ans.append(e)
            alg1_max[0] = self._maxv[0]
            self._ans.clear()
            self._maxv[0] = 0
            self._work[0] = 0

        # always run alg2
        self._alg2()
        assert self._work[0]
        # your answer is checked here after exam
        check_result(self._a, self._ans, self._maxv[0], alg1_ans, alg1_max[0])

    ############################################################
    # Brute Force Implementation with Show
    ########################################################### 
    def _alg1(self):
        if len(self._a)==0:  # Handle empty array
            self._maxv[0] = 0
            self._ans.clear()
            self._work[0]+=1
            if self._show:
                print(f"Alg1 Final: maxv={self._maxv[0]}, ans={self._ans}, work={self._work[0]}")
            return
        
        def helper(index, current_sum, path):
            self._work[0] += 1 
            if self._show:
                print(f"Alg1 Iteration: index={index}, current_sum={current_sum}, path={path}, maxv={self._maxv[0]}")

            # Base case
            if index >= len(self._a):
                # Update max value and solution path
                if current_sum > self._maxv[0]:
                    self._maxv[0] = current_sum
                    self._ans.clear()
                    self._ans.extend(path)
                    if self._show:
                        print(f"Updated maxv: {self._maxv[0]}, ans: {self._ans}, work={self._work[0]}")
                return

            # Choose the current index
            helper(index + 2, current_sum + self._a[index], path + [index])
            # Skip the current index
            helper(index + 1, current_sum, path)

        helper(0, 0, [])

        # Final output
        if self._show:
            print(f"Alg1 Final: maxv={self._maxv[0]}, ans={self._ans}, work={self._work[0]}")


    ############################################################
    # Using Dynamic Programming to Implement  prob
    ########################################################### 
    def _alg2(self):
        if len(self._a)==0:  # Handle empty array
            self._maxv[0] = 0
            self._ans.clear()
            self._work[0]+=1
            if self._show:
                print(f"Alg2 Final: maxv={self._maxv[0]}, ans={self._ans}, work={self._work[0]}")
            return
        
        n = len(self._a)
        if n == 0:
            self._maxv[0] = 0
            return

        dp = [0] * n
        prev = [None] * n  

        dp[0] = self._a[0]
        prev[0] = [0]

        self._work[0] += 1  

        if n > 1:
            if self._a[1] > self._a[0]:
                dp[1] = self._a[1]
                prev[1] = [1]
            else:
                dp[1] = self._a[0]
                prev[1] = [0]
            self._work[0] += 1  

        if self._show:
            print(f"Alg2 Initialization: dp={dp}, take={prev}")

        for i in range(2, n):
            # Increment work once per loop iteration
            self._work[0] += 1

            if dp[i - 1] > dp[i - 2] + self._a[i]:
                dp[i] = dp[i - 1]
                prev[i] = prev[i - 1] 
            else:
                dp[i] = dp[i - 2] + self._a[i]
                prev[i] = prev[i - 2] + [i]  

            if self._show:
                print(f"Alg2 Iteration {i}: dp={dp}, take={prev}")

        self._maxv[0] = dp[-1]
        self._ans = prev[-1]

        if self._show:
            print(f"Alg2 Final: maxv={self._maxv[0]}, ans={self._ans}, work={self._work[0]}")


############################################################
# Nothing can be changed in check_result
# Note check_result is a global hanging function
###########################################################  
def check_result(a: 'Python list', ans: 'Python List', amax: 'int', alg1_ans: 'Python list', alg1_max: 'int'):
    print("Checking routine will be added after exam")
    print("Be careful. May fail if not filled properly")
    
 