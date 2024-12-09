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
        # assert(self._work[0])
        #your answer is checked here after exam
        check_result(self._a,self._ans,self._maxv[0],alg1_ans,alg1_max[0]) 

    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg1(self):
        num_elements = len(self._a)
        maximum_sum = 0
        best_subset_indices = []
    
        # Iterate over all possible subsets using subset IDs
        for subset_id in range(1 << num_elements):  # There are 2^n subsets
            current_subset = []
            current_sum = 0
            is_valid_subset = True
    
            # Check which elements are included in the subset
            for index in range(num_elements):
                self._work[0] += 1  # Increment work for checking each element
                if subset_id & (1 << index):  # If index-th bit is set in subset_id
                    if current_subset and current_subset[-1] == index - 1:  # Check for adjacent indices
                        is_valid_subset = False
                        break
                    current_subset.append(index)
                    current_sum += self._a[index]
    
            if is_valid_subset:
                print(f"Subset: {current_subset}, Sum: {current_sum}")
                if current_sum > maximum_sum:
                    maximum_sum = current_sum
                    best_subset_indices = current_subset.copy()
    
        # Record the best result
        self._ans.extend(best_subset_indices)
        self._maxv[0] = maximum_sum
    
        if self._show:  # Print detailed step-by-step results
            print(f"Maximum Value (maxv) = {self._maxv[0]}")
            print(f"Best Subset Indices (ans) = {self._ans}")
            print(f"Total Work Done (work) = {self._work[0]}")




        
    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg2(self):
        array_length = len(self._a)
        if array_length == 0:
            self._maxv[0] = 0
            return
    
        if array_length == 1:
            self._ans.append(0)
            self._maxv[0] = self._a[0]
            return

        val2 = max(self._a[0], self._a[1])
        if array_length == 2:
            if self._a[0] > self._a[1]:
                self._ans.append(0)
                self._maxv[0] = self._a[0]
                return
            else:
                self._ans.append(1)
                self._maxv[0] = self._a[1]
                return
    
        dp_max_values = [0] * array_length
        dp_max_values[0] = self._a[0]
        dp_max_values[1] = max(self._a[0], self._a[1])
    
        for i in range(2, array_length):
            self._work[0] += 1
            dp_max_values[i] = max(self._a[i] + dp_max_values[i - 2], dp_max_values[i - 1])
            
            print(f"Step {i}: Max Value for indices 0 to {i} is {dp_max_values[i]}")
    
        self._maxv[0] = dp_max_values[-1]
    
        i = array_length - 1
        while i >= 0:
            self._work[0] += 1
            if i == 0:
                self._ans.append(0)
                break
            elif i == 1:
                if self._a[0] > self._a[1]:
                    self._ans.append(0)
                else:
                    self._ans.append(1)
                break
    
            if self._a[i] + dp_max_values[i - 2] >= dp_max_values[i - 1]:
                self._ans.append(i)
                i -= 2
            else:
                i -= 1
    
        
        print("Optimized Results:")
        print("Selected Indices:", self._ans)
        print("Max Value:", self._maxv[0])
        print("Work Count:", self._work[0])
        print("DP List : ", dp_max_values)
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
    
 