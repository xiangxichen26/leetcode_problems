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
        # Initialize variables for the problem
        size = len(self._a) # Length of the input array
        self._ans.clear() # Clear the answer list
        self._maxv[0] = 0 # Reset the maximum value to 0
        self._work[0] = 0 # Reset the work counter

        # Recursive explore function to explore all subsets of non-adjacent elements
        def explore(idx, chosen, sum_so_far):
            # Increment work counter to track operations
            self._work[0] += 1
        
            # Print the current state of exploration
            print(f"Step {self._work[0]}: Exploring idx={idx}, chosen={chosen}, sum_so_far={sum_so_far}")

            # Base case: if the index is out of bounds, check if the current sum is the best
            if idx >= size:
                if sum_so_far > self._maxv[0]:
                    print(f"Updating _maxv from {self._maxv[0]} to {sum_so_far}, _ans to {chosen}")
                    self._maxv[0] = sum_so_far
                    self._ans[:] = chosen[:] # Update the best selection
                return
            # Exclude the current element and move to the next index
            explore(idx + 1, chosen, sum_so_far)
            
            # Include the current element if it's not adjacent to the last selected element
            if not chosen or chosen[-1] != idx - 1:
                explore(idx + 1, chosen + [idx], sum_so_far + self._a[idx])
        # Start recursion from the first index
        explore(0, [], 0)

        # Debug output to show the results
        if self._show:
            print("------- Algorithm 1 -----------")
            print(f"maxv = {self._maxv[0]}")
            print(f"ans = {self._ans}")
            print(f"work = {self._work[0]}")   
    ############################################################
    #          WRITE CODE BELOW
    ###########################################################
    def _alg2(self):
        # Get the size of the input array
        length = len(self._a)

        # Handle the edge case where the input array is empty
        if length == 0:
            self._maxv[0] = 0
            self._ans.clear()
            self._work[0] = 1 # One operation to detect empty input
            if self._show:
                print("------- Algorithm 2 -----------")
                print(f"maxv = {self._maxv[0]}")
                print(f"ans = {self._ans}")
                print(f"work = {self._work[0]}")
            return

        # Initialize DP array and list to store selected indices
        dp_table = [0] * length
        selected = [[] for _ in range(length)]
        self._work[0] = 0
 
        # Base case: first element
        dp_table[0] = self._a[0]
        selected[0] = [0]
        self._work[0] += 1
        
        # Base case: second element
        if length > 1:
            dp_table[1] = max(self._a[0], self._a[1])
            selected[1] = [0] if self._a[0] > self._a[1] else [1]
            self._work[0] += 1

        # Fill DP table for the rest of the elements
        for i in range(2, length):
            self._work[0] += 1
            if dp_table[i - 1] >= dp_table[i - 2] + self._a[i]:
                dp_table[i] = dp_table[i - 1]
                selected[i] = selected[i - 1][:]
            else:
                dp_table[i] = dp_table[i - 2] + self._a[i]
                selected[i] = selected[i - 2] + [i]

        # Extract the results from the DP table
        self._maxv[0] = dp_table[-1]
        self._ans[:] = selected[-1]
        
        # Debug output to show the results
        if self._show:
            print("------- Algorithm 2 -----------")
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