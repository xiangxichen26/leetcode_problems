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
        def helper(idx, selected_indices, current_sum):
            nonlocal max_sum, optimal_indices, operation_count
    
            
            operation_count += 1
    
           
            if idx == total_indices:
                if current_sum > max_sum:
                    max_sum = current_sum
                    optimal_indices = selected_indices[:]
                return
    
           
            helper(idx + 1, selected_indices, current_sum)
    
            
            if not selected_indices or selected_indices[-1] != idx - 1:  
                selected_indices.append(idx)
                helper(idx + 1, selected_indices, current_sum + self._a[idx])
                selected_indices.pop()  
    
        total_indices = len(self._a)
        max_sum = 0
        optimal_indices = []
        operation_count = 0
    
      
        helper(0, [], 0)
    
       
        self._ans.extend(optimal_indices)
        self._maxv[0] = max_sum
        self._work[0] = operation_count
    
        if self._show:
            print("Brute Force Results:")
            print(f"Max Marks: {max_sum}")
            print(f"Selected Indices: {optimal_indices}")
            print(f"Work Done: {operation_count}")
             
        
    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg2(self):
        total_items = len(self._a)
        if total_items == 0:
            return
    
        dp_table = [0] * total_items
        include_item = [False] * total_items
        operation_count = 0
    
       
        dp_table[0] = self._a[0]
        if total_items > 1:
            dp_table[1] = max(self._a[0], self._a[1])
            include_item[1] = self._a[1] > self._a[0]
        operation_count += 2
    
        
        for idx in range(2, total_items):
            operation_count += 1
            if dp_table[idx - 1] > self._a[idx] + dp_table[idx - 2]:
                dp_table[idx] = dp_table[idx - 1]
            else:
                dp_table[idx] = self._a[idx] + dp_table[idx - 2]
                include_item[idx] = True
    
      
        idx = total_items - 1
        selected_indices = []
        while idx >= 0:
            operation_count += 1
            if include_item[idx]:
                selected_indices.append(idx)
                idx -= 2
            else:
                idx -= 1
    
      
        self._ans.extend(reversed(selected_indices))
        self._maxv[0] = dp_table[total_items - 1]
        self._work[0] = operation_count
    
        if self._show:
            print("Dynamic Programming Results:")
            print(f"Max Marks: {dp_table[total_items - 1]}")
            print(f"Selected Indices: {selected_indices}")
            print(f"Work Done: {operation_count}")  
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
    
 