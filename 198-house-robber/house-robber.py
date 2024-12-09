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
        # Nothing can be changed below
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
        if (len(self._a) < 16):
            self._alg1()
            assert(self._work[0])
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
        assert(self._work[0])
        # your answer is checked here after exam
        check_result(self._a, self._ans, self._maxv[0], alg1_ans, alg1_max[0])

    ############################################################
    #          Updated _alg1 Code
    ###########################################################
        ############################################################
    #          Updated _alg1 Code
    ###########################################################
    def _alg1(self):
        n = len(self._a)
        max_score = 0
        optimal_subset = []
        self._work[0] = 0

        print("------- Exhaustive Search Algorithm ------------")
        subset_count = 1
        # Generate all subsets manually
        for subset_index in range(1 << n):  # 2^n subsets
            current_subset = []
            for i in range(n):
                if subset_index & (1 << i):  # Check if bit i is set in subset_index
                    current_subset.append(i)

            # Check validity of current_subset (no consecutive indices)
            is_valid_subset = True
            for j in range(1, len(current_subset)):
                if current_subset[j] - current_subset[j - 1] == 1:
                    is_valid_subset = False
                    break

            if is_valid_subset:
                subset_score = 0
                for idx in current_subset:
                    subset_score += self._a[idx]
                self._work[0] += 1
                if self._show:
                    print(f"{subset_count} : {current_subset} = {subset_score}")
                subset_count += 1
                if subset_score > max_score:
                    max_score = subset_score
                    optimal_subset = current_subset

        self._maxv[0] = max_score
        self._ans.clear()
        self._ans.extend(optimal_subset)

        print(f"maxv = {max_score}")
        print(f"ans = {optimal_subset}")
        print(f"work = {self._work[0]}")

    ############################################################
    #          Updated _alg2 Code
    ########


    ############################################################
    #          Updated _alg2 Code
    ###########################################################
    def _alg2(self):
        n = len(self._a)
        if n == 0:
            self._maxv[0] = 0
            self._ans.clear()
            self._work[0] = 0
            return

        max_scores = [0] * n  # Max scores up to index i
        selected_indices = [[] for _ in range(n)]  # Track selected indices
        self._work[0] = 0

        print("------- Dynamic Programming Algorithm ------------")
        for index in range(n):
            self._work[0] += 1
            if index == 0:
                max_scores[index] = self._a[index]
                selected_indices[index] = [index]
            elif index == 1:
                if self._a[index] > max_scores[index - 1]:
                    max_scores[index] = self._a[index]
                    selected_indices[index] = [index]
                else:
                    max_scores[index] = max_scores[index - 1]
                    selected_indices[index] = selected_indices[index - 1]
            else:
                if max_scores[index - 1] > max_scores[index - 2] + self._a[index]:
                    max_scores[index] = max_scores[index - 1]
                    selected_indices[index] = selected_indices[index - 1]
                else:
                    max_scores[index] = max_scores[index - 2] + self._a[index]
                    selected_indices[index] = selected_indices[index - 2] + [index]

            if self._show:
                print(f"{index + 1} : {selected_indices[index]} = {max_scores[index]}")

        self._maxv[0] = max_scores[-1]
        self._ans.clear()
        self._ans.extend(selected_indices[-1])

        print(f"maxv = {self._maxv[0]}")
        print(f"ans = {self._ans}")
        print(f"work = {self._work[0]}")

############################################################
# Nothing can be changed in check_result
# Note check_result is a global hanging function
###########################################################
def check_result(a: 'Python list', ans: 'Python List', amax: 'int', alg1_ans: 'Python list', alg1_max: 'int'):
    print("Checking routine will be added after exam")
    print("Be careful. May fail if not filled properly")