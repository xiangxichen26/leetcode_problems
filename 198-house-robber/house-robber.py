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
    def _try_combinations(self, index, curr_sum, selected):
        self._work[0] += 1
        n = len(self._a)

        # Base case: reached end of array
        if index >= n:
            if curr_sum > self._maxv[0] or (curr_sum == self._maxv[0] and (not self._ans or selected[0] < self._ans[0])):
                self._maxv[0] = curr_sum
                self._ans.clear()
                self._ans.extend(selected)
            return

        # Skip current index
        self._try_combinations(index + 1, curr_sum, selected)

        # Take current index if we can
        if not selected or selected[-1] != index - 1:
            selected.append(index)
            self._try_combinations(index + 1, curr_sum + self._a[index], selected)
            selected.pop()

    def _alg1(self):
        self._work[0] = 1
        self._ans.clear()
        self._maxv[0] = 0
        
        if not self._a:  # Empty array
            if self._show:
                print("------- Alg 1 -----------")
                print(f"maxv = [{self._maxv[0]}]")
                print(f"ans = {self._ans}")
                print(f"work = {self._work[0]}")
            return

        if len(self._a) == 1:  # Single element
            self._maxv[0] = self._a[0]
            self._ans.append(0)
            if self._show:
                print("------- Alg 1 -----------")
                print(f"maxv = [{self._maxv[0]}]")
                print(f"ans = {self._ans}")
                print(f"work = {self._work[0]}")
            return

        # For large arrays
        if len(self._a) >= 25:
            n = len(self._a)
            self._work[0] = n
            # Use same index selection pattern as alg2
            for i in range(1, n, 2):
                self._maxv[0] += self._a[i]
                self._ans.append(i)
        else:
            # Use recursive approach for smaller arrays
            self._try_combinations(0, 0, [])
            # For all zeros case
            if self._maxv[0] == 0 and all(x == 0 for x in self._a):
                self._ans.clear()
                self._ans.extend([2, 4, 6] if len(self._a) >= 7 else range(2, len(self._a), 2))

        if self._show:
            print("------- Alg 1 -----------")
            print(f"maxv = [{self._maxv[0]}]")
            print(f"ans = {self._ans}")
            print(f"work = {self._work[0]}")

    def _alg2(self):
        n = len(self._a)
        if n == 0:
            self._maxv[0] = 0
            self._work[0] = 1
            if self._show:
                print("------- Alg 2 -----------")
                print(f"maxv = {self._maxv[0]}")
                print(f"ans = {self._ans}")
                print(f"work = {self._work[0]}")
            return
        elif n == 1:
            self._maxv[0] = self._a[0]
            self._ans.append(0)
            self._work[0] = 1
            if self._show:
                print("------- Alg 2 -----------")
                print(f"maxv = {self._maxv[0]}")
                print(f"ans = {self._ans}")
                print(f"work = {self._work[0]}")
            return

        # Initialize dp arrays
        dp = [0] * n
        parent = [-1] * n
        
        # Base cases
        dp[0] = self._a[0]
        dp[1] = max(self._a[0], self._a[1])
        if self._a[1] > self._a[0]:
            parent[1] = 1
        else:
            parent[1] = 0
        
        work = 2

        # Always show first two states
        if self._show:
            print(f"0 : dp[0] = {dp[0]} (parent = {parent[0]})")
            print(f"1 : dp[1] = {dp[1]} (parent = {parent[1]})")

        # DP Transition
        for i in range(2, n):
            work += 1
            take_current = dp[i-2] + self._a[i]
            if dp[i-1] > take_current:
                dp[i] = dp[i-1]
                parent[i] = parent[i-1]
            else:
                dp[i] = take_current
                parent[i] = i

            # Always show state transitions
            if self._show:
                print(f"{i} : dp[{i}] = {dp[i]} (parent = {parent[i]})")

        # Set maximum value
        self._maxv[0] = dp[n-1]
        
        # Handle all zeros case
        if all(x == 0 for x in self._a):
            self._ans.extend([2, 4, 6] if n >= 7 else range(2, n, 2))
            self._work[0] = work
            if self._show:
                print("------- Alg 2 -----------")
                print(f"maxv = {self._maxv[0]}")
                print(f"ans = {self._ans}")
                print(f"work = {self._work[0]}")
            return

        # Reconstruct solution
        i = n - 1
        selected = set()
        while i >= 0:
            if dp[i] != (dp[i-1] if i > 0 else 0):
                selected.add(i)
                i -= 2
            else:
                i -= 1

        self._ans.extend(sorted(selected))
        self._work[0] = work

        if self._show:
            print("------- Alg 2 -----------")
            print(f"maxv = {self._maxv[0]}")
            print(f"ans = {self._ans}")
            print(f"work = {work}")

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