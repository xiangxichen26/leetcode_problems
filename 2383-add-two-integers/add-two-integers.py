############################################################
# Exam.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################

############################################################
#  NOTHING CAN BE CHANGED BELOW
###########################################################
class Solution:
    def sum(self, a: int, b: int) -> int:
        ea = a + b
        ma = Int(a)
        tma = Int(a)
        mb = Int(b)
        tmb = Int(b)
        mc = Int()
        s = Exam(ma,mb,mc)
        ans = mc.int()
        assert(ans == ea)
        assert(ma == tma)
        assert(mb == tmb)
        return ans

########################################
#Nothing can be changed in class Exam
########################################
class Exam:
    def __init__(self, a:'Int', b:'Int', ans:'Int')->'None':
        #NOTHING CAN BE CHANGED BELOW
        self._a = a
        self._b = b
        self._ans = ans 
        self._alg()

    def _alg(self)->'None':
        j=len(self._a)-1
        k=len(self._b)-1
        
       # self._ans = Int()
       # self._ans = [0] * max(len(self._a), len(self._b) + 1)
        y=0
        a1=self._a.int()
        b1=self._b.int()
        if (a1 >=0 and b1>=0) or (a1<0 and b1<0):
            if j<k:
                while j >= 0:
                    x = self._a[j] + self._b[k] + y
                    self._ans.append(x % 10)
                    if x >= 10: 
                        y=1
                    else:
                        y=0
                    j -= 1
                    k -= 1
                
                while k >= 0:
                    if y > 0:
                        x = self._b[k] + 1
                        y = 0
                    else:
                        x = self._b[k]
                    self._ans.append(x)
                    k -= 1
                
            elif j == k:
                while j >= 0:
                    x = self._a[j] + self._b[j] + y
                    self._ans.append(x % 10)
                    if x >= 10: 
                        y=1
                    else:
                        y=0
                    j -= 1
                
                if y>0:
                    self._ans.append(1)
                    
            elif j>k:
                while k>=0:
                    x=self._a[j]+self._b[k]+y
                    self._ans.append(x%10)
                    if x >= 10:
                        y = 1
                    else:
                        y = 0
                    j -= 1
                    k -= 1
                
                while j>=0:
                    if y>0:
                        x=self._a[j]+y
                        if x>=10:
                            y=1
                        else:
                            y=0
                    else:
                        x=self._a[j]
                    self._ans.append(x%10)
                    j -= 1
                   
                if y>0:
                    self._ans.append(1)
                    
                      
            if a1 >= 0 and b1 >= 0:
                self._ans.positive(True)
            else:
                self._ans.positive(False)
        
        elif a1>=0 and b1<0 :
            if j<k:
                self._ans.positive(False)
                while j>=0:
                    x=self._b[k]-self._a[j]-y
                    if x >= 0:
                        y = 0 
                    else:
                        y = 1
                        x = x+10
                    self._ans.append(x)    
                    j -= 1
                    k -= 1
                
                while k>=0:
                    if y>0:
                        x=self._b[k]-1
                        if x<0:
                            y=1
                            x=x+10
                        else:
                            y=0
                    else:
                        x=self._b[k]
                    self._ans.append(x)
                    k -= 1
              
            elif j>k:
                self._ans.positive(True)
                while k>0 or k==0:
                    x=self._a[j]-self._b[k]-y
                    if x >= 0:
                        y = 0 
                    else:
                        y = 1
                        x = x+10
                    self._ans.append(x)    
                    j -= 1
                    k -= 1
                
                while j>=0:
                    if y>0:
                        x=self._a[j]-y
                        if x<0:
                            y=1
                            x=x+10
                        else:
                            y=0
                    else:
                        x=self._a[j]
                    self._ans.append(x) 
                    j -= 1
           
            elif j==k:
                b1=-b1
                if a1>=b1:
                    self._ans.positive(True)
                    
                    while j>=0:
                        x=self._a[j]-self._b[j]-y
                        if x >= 0:
                            y = 0 
                        else:
                            y = 1
                            x = x+10
                        self._ans.append(x) 
                        j -= 1
                    
    
                elif a1<b1:
                    self._ans.positive(False)
                    
                    while j>=0:
                        x=self._b[k]-self._a[j]-y
                        if x >= 0:
                            y = 0 
                        else:
                            y = 1
                            x = x+10
                        self._ans.append(x) 
                        j -= 1
                        k -= 1

                    while k>=0:                                  
                        if y>0:
                            x=self._b[k]-1
                            if x<0:
                                x=x+10
                                y=1
                            else:
                                y=0
                        else:
                            x=self._b[k]
                        self._ans.append(x) 
                        k -= 1
       
        elif a1<0 and b1>=0 :
            if j<k:
                self._ans.positive(True)
                while j>=0:
                    x=self._b[k]-self._a[j]-y
                    if x >= 0:
                        y = 0 
                    else:
                        y = 1
                        x = x+10
                    self._ans.append(x)     
                    j -= 1
                    k -= 1
                
                while k>=0:
                    if y>0:
                        x=self._b[k]-1
                        if x<0:
                            y=1
                            x=x+10
                        else:
                            y=0
                    else:
                        x=self._b[k]
                    self._ans.append(x)  
                    k -= 1
              
            elif j>k:
                self._ans.positive(False)
                while k>=0:
                    x=self._a[j]-self._b[k]-y
                    if x >= 0:
                        y = 0 
                    else:
                        y = 1
                        x = x+10
                    self._ans.append(x)       
                    j -= 1
                    k -= 1
                
                while j>=0:
                    print(y) 
                    if y>0:
                        x=self._a[j]-y
                        if x<0:
                            x=x+10
                            y=1
                        else:
                            y=0
                    else:
                        x=self._a[j]
                    self._ans.append(x)   
                    j -= 1
           
            elif j==k:
                a1=-a1
                if a1>b1:
                    self._ans.positive(False)
                    
                    while j>=0:
                        x=self._a[j]-self._b[k]-y
                        if x >= 0:
                            y = 0 
                        else:
                            y = 1
                            x = x+10
                        self._ans.append(x)
                        j -= 1
                        k -= 1
    
                elif b1>=a1:
                    self._ans.positive(True)
                    
                    while j>0 or j==0:
                        x=self._b[k]-self._a[j]-y
                        if x >= 0:
                            y = 0 
                        else:
                            y = 1
                            x = x+10
                        self._ans.append(x) 
                        j -= 1
                        k -= 1

                    while k>=0:                                  
                        if y>0:
                            x=self._b[k]-1
                            if x<0:
                                x=x+10
                                y=1
                            else:
                                y=0
                        else:
                            x=self._b[k]
                        self._ans.append(x) 
                        k -= 1

        return self._ans.reverse()

############################################################
# Int.py
# Implements Int object
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2025
# added to git
###########################################################

class Int:
    def __init__(self, n: "Python int" = None):
        if n is None:
            self._a = []

        else:
            self._positive = True
            if n < 0:
                 self._positive = False
            self._a = self.build(n)

    def _get_key(self)-> list[int]:
        return self._a
    
    def positive(self, a: bool) -> 'None':
        self._positive = a

    def build(self, n) -> "list of int":
        a=[]
        
        if n==0:
            a.append(n)

        elif n>0 or n<0:
            if n<0:
                n=-n 
            while n>0:
                a.append(n%10)
                n=n//10
            a.reverse()

        elif n=='':
            a=[]  
        
        return a 

        
    def append(self, value: int):
        self._a.append(value)

    def reverse(self):
        self._a.reverse()
        return self._a

    def int(self) -> "Python integer":
        n=self._a
        x=0
        i=0
        
        while i<len(n):
            x=x*10+n[i]
            i+=1
            
        if self._positive == False:
            x=-x
        return x
        
    def __str__(self): 
        return str(self._a)
        
    def __len__(self):
        return len(self._a)

    def __getitem__(self, index: "Python int"):
        return self._a[index]
            
    def __setitem__(self, index, value):
        self._a[index] = value

    def __eq__(self, other):
        a = len(self._a)
        b = len(other._a)
        if a!=b:
            return False
        else:
            i=0
            for i in range(len(self._a)):
                if self._a[i] != other._a[i]:
                    return False
        return True
