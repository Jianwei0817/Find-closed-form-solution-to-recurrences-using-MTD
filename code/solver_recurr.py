#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:35:53 2019

@author: jasonwang
"""


from sympy import Function, solve, Symbol,log,factorial
from sympy import *
from sympy.abc import c,k,A,B,C,D,E,F,G,H,I,J,K,Q,Y
import sys
import time
import numpy as np
import copy
import sympy
from add20190324 import *


f=Function('f')
    
n=Symbol('n')

MTT=1800 ###maximum time cost threshold(seconds)

def sortConj(Conjecture_space):
    
    before_conj=dict()
    for i in list(Conjecture_space):
        before_conj[i.subs(n,2)]=i
    after_conj=sorted(before_conj)
    sorted_conj=[]
    for i in after_conj:        
        sorted_conj.append(before_conj[i])
    #print(sorted_conj)
    return sorted_conj

def conjectureSpace(iter_num):
    Conjecture_base=set()
    
    CONJ=[]
    CONJ.append(c)

    Conjecture_base.add(n)
    
    Conjecture_space=set()
    Conjecture_space.add(n)
    count_1=0
    while(count_1<=iter_num):
        for conj1 in Conjecture_base:
            #Conjecture_space.add(expand(Symbol(chr(random.randint(80,90)))*conj1))
            for conj2 in Conjecture_base:             
                #Conjecture_space.add(expand(Symbol(chr(random.randint(83,85)))*conj1)+expand(Symbol(chr(random.randint(86,88)))*conj2))
                Conjecture_space.add(sympy.expand(conj1*conj2))
                                           
        Conjecture_base=Conjecture_base.union(Conjecture_space)
       
        count_1=count_1+1
        
    sorted_space=sortConj(Conjecture_space)
    conj_1=c

    CONJ_copy=[]##为了将conj_1+conj_2 得到幂函数和多项式的组合假设
    for i in range(len(sorted_space)):
        conj_1=conj_1+(sympy.Symbol(chr(65+i))*(sorted_space)[i]) 
        #conj_3=conj1+conj_2
        CONJ.append(conj_1)
        
        CONJ_copy.append(conj_1)
        #CONJ.append(conj_3)        
    count_2=0
    conj_2=c 
    while(count_2<=1):        
        conj_2=conj_2+(Symbol(chr(65+len(Conjecture_space)+count_2)))*pow(Symbol(chr(65+len(Conjecture_space)+count_2+8)),n)        
        CONJ.append(conj_2)        
        for i in CONJ_copy:
            CONJ.append(i+conj_2-c)            
        count_2=count_2+1    
    return CONJ



def Solve_r(m,init_value,recurr_expression):
    if "f(n)**2" in str(recurr_expression):
        Solve_rr(m,init_value,recurr_expression)        
    else:   
        
        break_Flag=False
        
        R_={}
    
        R_[f(m)]=init_value#初始值init_value从m开始 
    
        eqs=[]
        start=time.clock()
    
        
        past_conj_set=[]
        
        for space_size in range(sys.maxsize):    
            """
            if space_size == 4:
                print("Sorry, we cannot find the potential closed-form solution in 30 mins! ")
                return -1
                break
            """
            Conjecture_base=conjectureSpace(space_size)
            """
            new_Conjecture_base=copy.deepcopy(Conjecture_base)
            new_Conjecture_base=new_Conjecture_base.difference(last_Conjecture_base)
            last_Conjecture_base=copy.deepcopy(Conjecture_base)
            """
            for conj in Conjecture_base:
                
                if conj in past_conj_set:
                    continue
                else:
                    past_conj_set.append(conj)
                 
                print("conj:",conj)
                #conj=A*n + B*n**2 + C*n**3 + D*n**4 + E*n**5 + F*n**6 + G*n**7 + H*n**8 + I*n**9 + J*n**10 + c
                
                for i in [(j+m) for j in range(20)]:
    
                    right=conj.subs(n,i)
    
                    r_eq=recurr_expression.subs(n,i)
    
                    p=r_eq.subs(f(i),R_[f(i)])                    
    
                    R_[f(i+1)]=solve(p,f(i+1),check=False)[0]
                 
                    left=R_[f(i)]
    
                    equation=left-right
    
                    eqs.append(equation)
    
                try:
                    result=solve(eqs,check=False)
                except:
                    result == []
    
                if result == []:
                    #print('This conjecture f(n)=%s is not correct'%conj)
                    end=time.clock()
    
                    if (end-start) >= MTT:
    
                        
                        break_Flag=True
    
                        print("Sorry, we cannot find the potential closed-form solution in %s mins! " %(int(MTT/60)))
                        
                        #return -1
                        break
    
                    else:
    
                        pass
      
                else:
    
                    if type(result)==list:
    
                        final_conj=sympy.expand(conj.subs(result[-1]))
    
                    else:
    
                        final_conj=sympy.expand(conj.subs(result))
                    
                    #print(conj)
    
                    #print(result)
      
                    #print('The conjecture f(n)=%s may be correct'%(final_conj))
    
                    value=induction_prover(final_conj,m,R_,recurr_expression)
    
                    if value == True:
    
                        break_Flag=True
    
                        end=time.clock()
                        diff=(end-start)
                        print('Congratulations!! The conjecture f(n)=%s must be correct!!!'%(final_conj))                    
                        print("Usage of time:",diff,"seconds")
                        
                        #return [final_conj, diff]
                        break
    
                    else:
    
                        pass
    
                R_={}
    
                eqs=[]
    
                R_[f(m)]=init_value#初始值                    
                
            if break_Flag==True:
    
                break 

def induction_prover(final_conj,m,R_,recurr_expression):

    if final_conj.subs(n,m)==R_[f(m)]:

        R_[f(k)]=final_conj.subs(n,k)

        cmp1=final_conj.subs(n,(k+1))

        temp=recurr_expression.subs(n,k)

        result_exp=solve(temp,f(k+1),check=False)[0]
        cmp2=result_exp.subs(f(k),R_[f(k)])

        if sympy.expand(cmp1) == sympy.expand(cmp2):
            
            #print('Congratulations!! The conjecture f(n)=%s must be correct!!!'%(final_conj))
            return True

        else:

            print("Unfortunately, the conjecture f(n)=%s is wrong"%(final_conj))
        return False
    else:   

        print("Unfortunately, the conjecture f(n)=%s is wrong"%(final_conj))

        return False


    

if __name__ == "__main__":
    '''some examples'''
    #space=conjectureSpace(0)
    #print(space)
    #Solve_r(7,-6,f(n+1)-f(n)-5*n**4+4*n**3-3*n**2+2*n-1)
    #9*f(n)
    Solve_r(1,2,f(n+1)-f(n)+(2)*n)

    
    #Solve_r(0,1,f(n+1)-f(n)-n**4+n**2-3)
    #Solve_r(0,0,f(n+1)-f(n)-n**3/2+4*n**2)
    #Solve_r(1,1,f(n+1)-2*f(n)-3**n)
    
    ######15次方
    
    

