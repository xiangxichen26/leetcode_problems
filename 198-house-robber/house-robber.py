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
    
    #Brute Force Implementation using Recursion
    ########################################################### 
#     def _alg1(self):
#             if not self._a:
#                 self._work[0] = 1
#                 self._maxv[0] = 0
#                 return

#             n = len(self._a)
#             self._work[0] = 0
#             max_total = 0
#             best_path = []
#             for mask in range(1 << n):
#                 self._work[0] += 1
#                 current_total = 0
#                 current_path = []
#                 valid = True
#                 for i in range(n):
#                     if mask & (1 << i):
#                         if i > 0 and mask & (1 << (i-1)):
#                             valid = False
#                             break
#                         current_total += self._a[i]
#                         current_path.append(i)

#                 if valid and current_total > max_total:
#                     max_total = current_total
#                     best_path = current_path

#             self._maxv[0] = max_total
#             self._ans[:] = best_path

#             if self._show:
#                 print(f"Work = {self._work[0]}, Max Value = {self._maxv[0]}, Selected Indices = {self._ans}")
    
    def _alg1(self):
        def brute_force(index, selected, current_total):
            nonlocal max_total, best_path
            self._work[0] += 1  # Increment work counter
            if index >= len(self._a):
                if current_total > max_total:
                    max_total = current_total
                    best_path = selected[:]
                return
            brute_force(index + 1, selected, current_total)
            brute_force(index + 2, selected + [index], current_total + self._a[index])    
        
        if not self._a:
            self._work[0] = 1
            self._maxv[0] = 0
            return

        max_total = 0
        best_path = []
        self._work[0] = 0  # Reset work counter
        brute_force(0, [], 0)
    
        self._maxv[0] = max_total
        self._ans.clear()
        self._ans.extend(best_path)
        if self._show:
            print(f" Work = {self._work[0]}, Maximum Value = {self._maxv[0]}, Best Indices = {self._ans}")
      
        
    ############################################################
    #          WRITE CODE BELOW
    
    # The optimal solution uses Dynamic Programming
    ########################################################### 
    def _alg2(self):
        n = len(self._a)
        if n == 0:
            self._work[0] = 1
            self._maxv[0] = 0
            return

        self._work[0] = 0  # Reset work counter

        optimal = [0] * (n + 1)
        optimal_track = [[] for _ in range(n + 1)]

        for i in range(1, n + 1):
            self._work[0] += 1  # Track computational work
            if optimal[i - 1] >= self._a[i - 1] + (optimal[i - 2] if i > 1 else 0):
                optimal[i] = optimal[i - 1]
                optimal_track[i] = optimal_track[i - 1][:]
            else:
                optimal[i] = self._a[i - 1] + (optimal[i - 2] if i > 1 else 0)
                optimal_track[i] = optimal_track[i - 2][:] if i > 1 else []
                optimal_track[i].append(i - 1)

        self._maxv[0] = optimal[n]
        self._ans.clear()
        self._ans.extend(optimal_track[n])

        if self._show:
            print(f" Work = {self._work[0]}, Maximum Value = {self._maxv[0]}, Best Indices = {self._ans}")

  
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