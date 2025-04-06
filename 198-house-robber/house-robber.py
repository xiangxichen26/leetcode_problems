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
        best_num = [0]
        best_choice = [[]]
        self._work[0] = 0

        def rec(i,cur_num,idx):
            self._work[0] += 1
            if self._show:
                print("Brute force step: i =",i,"cur_num =",cur_num,"idx =",idx)
            if i>=len(self._a):
                if cur_num>best_num[0]:
                    best_num[0] = cur_num
                    best_choice[0] = idx.copy()
                return
            rec(i+1,cur_num,idx)
            rec(i+2,cur_num+self._a[i],idx+[i])
         
        rec(0,0,[])
        self._maxv[0] = best_num[0]
        self._ans.extend(best_choice[0])

    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg2(self):
        self._work[0] = 0
        n=len(self._a)
        if n==0:
            self._maxv[0] = 0
            self._ans.clear()
            return
        dp=[0]*n
        dp[0]=self._a[0]
        self._work[0]+=1
        if self._show:
            print("DP step: i =",0,"dp[0] =",dp[0])
        if n==1:
            self._maxv[0] = dp[0]
            self._ans.clear()
            self._ans.append(0)
            return
        dp[1]=max(self._a[0],self._a[1])
        self._work[0]+=1
        if self._show:
            print("DP step: i =",1,"dp[1] =",dp[1])
        for i in range(2,n):
            self._work[0]+=1
            dp[i]=max(dp[i-1],dp[i-2]+self._a[i])
            if self._show:
                print("DP step: i =",i,"dp[i] =",dp[i])
        self._maxv[0] = dp[n-1]

        result = []
        i=n-1
        while i>=0:
            if i==0:
                result.append(0)
                break
            if i==1:
                result.append(1) if self._a[1]>=self._a[0] else result.append(0)
                break
            if dp[i-1]>=dp[i-2]+self._a[i]:
                i-=1
            else:
                result.append(i)
                i-=2
        result.reverse()
        self._ans.clear()
        self._ans.extend(result)

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
 