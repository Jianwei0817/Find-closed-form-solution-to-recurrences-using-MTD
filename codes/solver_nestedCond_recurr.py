#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:21:00 2019

@author: jwangdk
"""
import sympy
from sympy import *
from sympy.abc import c, n, b, y, g, l, k, a, d, h
from z3 import *
import z3
import time
import copy
import sys

f=sympy.Function('f')

MTT=1800 #(:seconds)


'''将sympy的symbols list转化成Z3 LIST'''
def sympy_to_z3(sympy_var_list):     

    z3_vars = [] 
    z3_var_map = {} 

    for var in sympy_var_list: 
     name = var.name 
     z3_var = z3.Real(name) 
     z3_var_map[name] = z3_var 
     z3_vars.append(z3_var) 
    return z3_vars

#
#'''将sympy的symbol转化成Z3'''
#def sympy_to_z3(sympy_var):     
#    name = sympy_var.name 
#    z3_var = z3.Real(name) 
#    return z3_var



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


def conjectureSpace_1(iter_num):
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
                Conjecture_space.add(expand(conj1*conj2))
                
                
             
        Conjecture_base=Conjecture_base.union(Conjecture_space)
       
        count_1=count_1+1
    sorted_space=sortConj(Conjecture_space)
    conj=c
    
    for i in range(len(sorted_space)):
        conj=conj+(sympy.Symbol(chr(65+i))*(sorted_space)[i]) 
        CONJ.append(conj)
    count_1=count_1+1            
   
    return CONJ


def conjectureSpace_2(iter_num):
    Conjecture_base=set()
    
    CONJ=[]
    CONJ.append(b)

    Conjecture_base.add(n)
    
    Conjecture_space=set()
    Conjecture_space.add(n)
    
    count_1=0

    while(count_1<=iter_num):
        for conj1 in Conjecture_base:
            #Conjecture_space.add(expand(Symbol(chr(random.randint(80,90)))*conj1))

            for conj2 in Conjecture_base:
             
                #Conjecture_space.add(expand(Symbol(chr(random.randint(83,85)))*conj1)+expand(Symbol(chr(random.randint(86,88)))*conj2))
                Conjecture_space.add(expand(conj1*conj2))
                
                
             
        Conjecture_base=Conjecture_base.union(Conjecture_space)
       
        count_1=count_1+1
    sorted_space=sortConj(Conjecture_space)
    conj=b
    
    for i in range(len(sorted_space)):
        conj=conj+(sympy.Symbol(chr(90-i))*(sorted_space)[i]) 
        CONJ.append(conj)
    count_1=count_1+1            
   
    return CONJ

def conjectureSpace_3(iter_num):
    Conjecture_base=set()
    
    CONJ=[]
    CONJ.append(k)

    Conjecture_base.add(n)
    
    Conjecture_space=set()
    Conjecture_space.add(n)
    
    count_1=0

    while(count_1<=iter_num):
        for conj1 in Conjecture_base:
            #Conjecture_space.add(expand(Symbol(chr(random.randint(80,90)))*conj1))

            for conj2 in Conjecture_base:
             
                #Conjecture_space.add(expand(Symbol(chr(random.randint(83,85)))*conj1)+expand(Symbol(chr(random.randint(86,88)))*conj2))
                Conjecture_space.add(expand(conj1*conj2))
                
                
             
        Conjecture_base=Conjecture_base.union(Conjecture_space)
       
        count_1=count_1+1
    sorted_space=sortConj(Conjecture_space)
    conj=k
    
    for i in range(len(sorted_space)):
        conj=conj+(sympy.Symbol(chr(82-i))*(sorted_space)[i]) 
        CONJ.append(conj)
    count_1=count_1+1            
   
    return CONJ



def conditionSpace_1(iter_num):
    Conjecture_base=set()
    
    CONDITION=[]
    

    Conjecture_base.add(n)
    
    Conjecture_space=set()
    Conjecture_space.add(n)
    
    count_1=0

    while(count_1<=iter_num):
        for conj1 in Conjecture_base:
            #Conjecture_space.add(expand(Symbol(chr(random.randint(80,90)))*conj1))

            for conj2 in Conjecture_base:
             
                #Conjecture_space.add(expand(Symbol(chr(random.randint(83,85)))*conj1)+expand(Symbol(chr(random.randint(86,88)))*conj2))
                Conjecture_space.add(expand(conj1*conj2))
                
                
             
        Conjecture_base=Conjecture_base.union(Conjecture_space)
       
        count_1=count_1+1
    sorted_space=sortConj(Conjecture_space)
    conj=g
    
    for i in range(len(sorted_space)):
        conj=conj+(sympy.Symbol(chr(111+i))*(sorted_space)[i]) 
        CONDITION.append(conj)
    count_1=count_1+1            
   
    return CONDITION

def conditionSpace_2(iter_num):
    Conjecture_base=set()
    
    CONDITION=[]
    

    Conjecture_base.add(n)
    
    Conjecture_space=set()
    Conjecture_space.add(n)
    
    count_1=0

    while(count_1<=iter_num):
        for conj1 in Conjecture_base:
            #Conjecture_space.add(expand(Symbol(chr(random.randint(80,90)))*conj1))

            for conj2 in Conjecture_base:
             
                #Conjecture_space.add(expand(Symbol(chr(random.randint(83,85)))*conj1)+expand(Symbol(chr(random.randint(86,88)))*conj2))
                Conjecture_space.add(expand(conj1*conj2))
                
                
             
        Conjecture_base=Conjecture_base.union(Conjecture_space)
       
        count_1=count_1+1
    sorted_space=sortConj(Conjecture_space)
    conj=l
    
    for i in range(len(sorted_space)):
        conj=conj+(sympy.Symbol(chr(122-i))*(sorted_space)[i]) 
        CONDITION.append(conj)
    count_1=count_1+1            
   
    return CONDITION

def induction_prover_cond(cond1,cond2,final_cond1,final_cond2,final_conj1,final_conj2,final_conj3,recurr_expression1,recurr_expression2,recurr_expression3,m,R_):

    ##是否满足初始条件

    print(final_cond1.subs(n,m))
    print(final_cond2.subs(n,m))
    if final_cond1.subs(n,m) and final_cond2.subs(n,m):
        print("11111111111111")
        ##验证第一个分支
        if final_conj1.subs(n,m)==R_[f(m)]:
            
            R_[f(a)]=final_conj1.subs(n,a)
            #print(R_[f(k)])
            #print(final_conj1.subs(n,k))
            cmp1_frt=final_conj1.subs(n,(a+1))
            #print("#"*20)
            #print(sympy.expand(cmp1_frt))
            if (cond1.subs(n,m)).subs(f(m),R_[f(m)]) and (cond2.subs(n,m)).subs(f(m),R_[f(m)]):
                temp1=recurr_expression1.subs(n,a)  
                result_exp1=sympy.solve(temp1,f(a+1),check=False)[0]    
                cmp1_snd=result_exp1.subs(f(a),R_[f(a)])
            
            elif (cond1.subs(n,m)).subs(f(m),R_[f(m)]) and not (cond2.subs(n,m)).subs(f(m),R_[f(m)]):
                temp1=recurr_expression2.subs(n,a)
                result_exp1=sympy.solve(temp1,f(a+1),check=False)[0]
                cmp1_snd=result_exp1.subs(f(a),R_[f(a)])     
            else:
                temp1=recurr_expression3.subs(n,a)
                result_exp1=sympy.solve(temp1,f(a+1),check=False)[0]
                cmp1_snd=result_exp1.subs(f(a),R_[f(a)])              
            #print(sympy.expand(cmp1_snd))

        else:   
            print("Unfortunately!")
            return False
#        ###验证第二个分支
#        R_[f(d)]=final_conj2.subs(n,d)
#        cmp2_frt=final_conj2.subs(n,(d+1))
#        if not (cond1.subs(n,m)).subs(f(m),R_[f(m)]):
#            temp2=recurr_expression1.subs(n,d)  
#            result_exp2=sympy.solve(temp2,f(d+1),check=False)[0]    
#            cmp2_snd=result_exp2.subs(f(d),R_[f(d)])
#        else:
#            temp2=recurr_expression2.subs(n,d)
#            result_exp2=sympy.solve(temp2,f(d+1),check=False)[0]
#            cmp2_snd=result_exp2.subs(f(d),R_[f(d)])         
#        #print("*"*20)
#        #print(sympy.expand(cmp2_frt))
#        #print(sympy.expand(cmp2_snd))
#        #print("*"*20)  
#        ##验证第三个分支
#        R_[f(h)]=final_conj3.subs(n,h)
#        cmp3_frt=final_conj3.subs(n,(h+1))
#        if not (cond1.subs(n,m)).subs(f(m),R_[f(m)]):
#            temp3=recurr_expression3.subs(n,h)  
#            result_exp3=sympy.solve(temp3,f(h+1),check=False)[0]    
#            cmp2_snd=result_exp3.subs(f(h),R_[f(h)])
#        else:
#            temp2=recurr_expression2.subs(n,h)
#            result_exp2=sympy.solve(temp2,f(h+1),check=False)[0]
#            cmp2_snd=result_exp2.subs(f(h),R_[f(h)])   
#            
            
        if sympy.expand(cmp1_frt) == sympy.expand(cmp1_snd) or sympy.expand(cmp2_frt) == sympy.expand(cmp2_snd) or sympy.expand(cmp3_trd) == sympy.expand(cmp3_trd) :
            print("Congratulations!!")
            return True
        else:
            print("Unfortunately")
            return False  
    elif final_cond1.subs(n,m) and not final_cond2.subs(n,m):
        print("22222222222")
        if final_conj2.subs(n,m)==R_[f(m)]:
            
            R_[f(a)]=final_conj2.subs(n,a)
            #print(R_[f(k)])
            #print(final_conj1.subs(n,k))
            cmp1_frt=final_conj2.subs(n,(a+1))
            #print("#"*20)
            #print(sympy.expand(cmp1_frt))
            if (cond1.subs(n,m)).subs(f(m),R_[f(m)]) and (cond2.subs(n,m)).subs(f(m),R_[f(m)]):
                temp1=recurr_expression1.subs(n,a)  
                result_exp1=sympy.solve(temp1,f(a+1),check=False)[0]    
                cmp1_snd=result_exp1.subs(f(a),R_[f(a)])
            
            elif (cond1.subs(n,m)).subs(f(m),R_[f(m)]) and not (cond2.subs(n,m)).subs(f(m),R_[f(m)]):
                temp1=recurr_expression2.subs(n,a)
                result_exp1=sympy.solve(temp1,f(a+1),check=False)[0]
                cmp1_snd=result_exp1.subs(f(a),R_[f(a)])     
            else:
                temp1=recurr_expression3.subs(n,a)
                result_exp1=sympy.solve(temp1,f(a+1),check=False)[0]
                cmp1_snd=result_exp1.subs(f(a),R_[f(a)])              
            #print(sympy.expand(cmp1_snd))

        else:   
            print("Unfortunately!")
            return False       
    
    
    else:        
        ##验证第三个分支
        print("33333333333333")
        if final_conj3.subs(n,m)==R_[f(m)]:
            
            R_[f(a)]=final_conj3.subs(n,a)            
            cmp1_frt=final_conj3.subs(n,(a+1))
            #print("#"*20)
            #print(sympy.expand(cmp2_frt))
            if (cond1.subs(n,m)).subs(f(m),R_[f(m)]) and (cond2.subs(n,m)).subs(f(m),R_[f(m)]):
                temp1=recurr_expression1.subs(n,a)  
                result_exp1=sympy.solve(temp1,f(a+1),check=False)[0]    
                cmp1_snd=result_exp1.subs(f(a),R_[f(a)])
            
            elif (cond1.subs(n,m)).subs(f(m),R_[f(m)]) and not (cond2.subs(n,m)).subs(f(m),R_[f(m)]):
                temp1=recurr_expression2.subs(n,a)
                result_exp1=sympy.solve(temp1,f(a+1),check=False)[0]
                cmp1_snd=result_exp1.subs(f(a),R_[f(a)])     
            else:
                temp1=recurr_expression3.subs(n,a)
                result_exp1=sympy.solve(temp1,f(a+1),check=False)[0]
                cmp1_snd=result_exp1.subs(f(a),R_[f(a)])  
        else:   
            print("Unfortunately!")
            return False         
#        ###验证第一个分支
#        R_[f(l)]=final_conj1.subs(n,l)
#        cmp1_frt=final_conj1.subs(n,(l+1))
#        if not (cond1.subs(n,m)).subs(f(m),R_[f(m)]):
#            temp1=recurr_expression1.subs(n,l)  
#            result_exp1=sympy.solve(temp1,f(l+1),check=False)[0]    
#            cmp1_snd=result_exp1.subs(f(l),R_[f(l)])
#        else:
#            temp1=recurr_expression2.subs(n,l)
#            result_exp1=sympy.solve(temp1,f(l+1),check=False)[0]
#            cmp1_snd=result_exp1.subs(f(l),R_[f(l)])         
#        #print("*"*20)
#        #print(sympy.expand(cmp1_frt))
#        #print(sympy.expand(cmp1_snd))
#        #print("*"*20) 
    print(sympy.expand(cmp1_frt))
    print(sympy.expand(cmp1_snd))
    if sympy.expand(cmp1_frt) == sympy.expand(cmp1_snd):
        print("Congratulations!!")
        return True
    else:
        print("Unfortunately!")
        return False 

##同时满足条件1&2==e1; 满足条件1不满足条件2==e2； 不满足条件1==e3
def Solve_nestedCond_r(m,init_value,cond1=None,cond2=None,recurr_expression1=None,recurr_expression2=None,recurr_expression3=None):
    break_Flag=False
 
    
    R_={}
    R_[f(m)]=init_value#初始值init_value从m开始 
    
    eqs=[]
    
    start=time.clock()

    
    A,B,C,D,E,F,G,H,I,J,K,L,M=sympy.symbols('A,B,C,D,E,F,G,H,I,J,K,L,M')
    N,O,P,Q,R,S,T,U,V,W,X,Y,Z=sympy.symbols('N,O,P,Q,R,S,T,U,V,W,X,Y,Z')
    b,c,l,k,g,o,p,q,r,s,t,u,v,w,x,y,z=sympy.symbols('b,c,l,k,g,o,p,q,r,s,t,u,v,w,x,y,z')
    
  
    past_conj_set=[]
    for space_size in range(sys.maxsize):
        
   
        Condition_space_1=[]
        Condition_space_2=[]
        
        cond_space_1=conditionSpace_1(space_size)
        cond_space_2=conditionSpace_2(space_size)
        
        for cond in cond_space_1:
            Condition_space_1.append(cond>=0)
            #Condition_space_1.append(cond>0)
        for cond in cond_space_2:
            Condition_space_2.append(cond>=0)
            #Condition_space_2.append(cond>0)            
        '''
        Condition_space.append(cond_space[-1]>=0)
        Condition_space.append(cond_space[-1]>0)'''
        for condition_1 in Condition_space_1:
            
            for condition_2 in Condition_space_2:
                
                for conj1 in conjectureSpace_1(space_size):
                    
                    for conj2 in conjectureSpace_2(space_size):
                        
                        for conj3 in conjectureSpace_3(space_size):
                        
                            if (condition_1,condition_2,conj1,conj2,conj3) in past_conj_set: 
                                continue
                            else:
                                past_conj_set.append((condition_1,condition_2,conj1,conj2,conj3))
                            
                            print("Conjecture: 'ite(%s, ite(%s, %s, %s),%s)'."%(condition_1,condition_2,conj1,conj2,conj3))
                            
                            for i in [(j+m) for j in range(30)]:
                                
                                cd_1=condition_1.subs(n,i)
                                cd_2=condition_2.subs(n,i)
    
                                
                                if (cond1.subs(n,i)).subs(f(i),R_[f(i)]):
                                        #right1=conj1.subs(n,i) 
                                    if (cond2.subs(n,i)).subs(f(i),R_[f(i)]): 
                                                         
                                        r_eq=recurr_expression1.subs(n,i) 
                                    else:
                                        r_eq=recurr_expression2.subs(n,i)
                                    
                                else:
                                        #right2=conj2.subs(n,i)                                                        
                                    r_eq=recurr_expression3.subs(n,i)                                                                             
        
                                                        
                                p_=r_eq.subs(f(i),R_[f(i)])
                                R_[f(i+1)]=sympy.solve(p_,f(i+1),check=False)[0]                      
                                left=R_[f(i)]   
                                
                                
                            
                                right1=conj1.subs(n,i)
                                right2=conj2.subs(n,i)
                                right3=conj3.subs(n,i)
                                
        
                                sympy_var_list1=[A,B,C,D,E,F,G,H,I,J,K,L,M]
                                A,B,C,D,E,F,G,H,I,J,K,L,M=sympy_to_z3(sympy_var_list1)
                                sympy_var_list2=[N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
                                N,O,P,Q,R,S,T,U,V,W,X,Y,Z=sympy_to_z3(sympy_var_list2)
                                sympy_var_list3=[b,c,l,k,g,o,p,q,r,s,t,u,v,w,x,y,z]
                                b,c,l,k,g,o,p,q,r,s,t,u,v,w,x,y,z=sympy_to_z3(sympy_var_list3)
                                
                                
                                
                                cd_1=(eval(str(cd_1)))
                                cd_2=(eval(str(cd_2)))
                                
                                right1=(eval(str(right1)))
                                right2=(eval(str(right2)))
                                right3=(eval(str(right3)))
                                
                                
                                #z3.If(cd_1,right1,right2)
                                eqs.append(z3.If(cd_1, z3.If(cd_2,right1==left, right2==left), right3==left))  
                                #print(eqs)
                                
                                A,B,C,D,E,F,G,H,I,J,K,L,M=sympy.symbols('A,B,C,D,E,F,G,H,I,J,K,L,M')
                                N,O,P,Q,R,S,T,U,V,W,X,Y,Z=sympy.symbols('N,O,P,Q,R,S,T,U,V,W,X,Y,Z')
                                b,c,l,k,g,o,p,q,r,s,t,u,v,w,x,y,z=sympy.symbols('b,c,l,k,g,o,p,q,r,s,t,u,v,w,x,y,z')
        
                            
                            sol=z3.Solver()
                            sol.add(eqs)
                            result=sol.check()
                            
                            
                            if result==z3.sat:
                                end=time.clock()
                                time_cost=end-start
                                mol=sol.model()
                                #print(type(str(bb)))
                                rr=dict()
                                
                                for dd in mol.decls():
                                    
                                    rr[eval(dd.name())]=sympy.Rational(str(mol[dd]))
                
                                final_conj1=conj1.subs(rr)
                                #print(final_conj1)
                                final_conj2=conj2.subs(rr)            
                                #print(final_conj2)
                                final_conj3=conj3.subs(rr)
                                
                                
                                final_cond1=condition_1.subs(rr)
                                final_cond2=condition_2.subs(rr)
                                #print(condition)
                                #print(final_cond)
                                
                                #print("#"*15)
                                value=induction_prover_cond(cond1,cond2,final_cond1,final_cond2,final_conj1,final_conj2,final_conj3,recurr_expression1,recurr_expression2,recurr_expression3,m,R_)

                                if value: 
                                    print("Congratulations!!! The conjecture f(n)=ite(%s, ite(%s, %s, %s),%s) must be correct!"%(final_cond1,final_cond2,final_conj1,final_conj2,final_conj3))
                                    print("Usage of time:", time_cost, "seconds")
                                    break_Flag=True
                                    break
                                    #return [final_cond1,final_cond2,final_conj1,final_conj2,final_conj3,time_cost]
                                else:
                                    print("The conjecture 'ite(%s, ite(%s, %s, %s),%s)' is NOT correct!"%(condition_1,condition_2,conj1,conj2,conj3))
                                    print("*"*20)
                                    #return [final_cond1,final_cond2,final_conj1,final_conj2,final_conj3,time_cost]
                                    
                                #print("The conjecture 'ite(%s, ite(%s, %s, %s),%s)' is correct."%(final_cond1,final_cond2,final_conj1,final_conj2,final_conj3))
                                
                                #print(R_)
                                
                                
                            else:
                                end=time.clock()
                                time_cost=end-start
                                if time_cost>=MTT:
                                    break_Flag=True
                                    print("Sorry, we cannot find the closed form solution to this recurrence in %s mins!"%(int(MTT/60)))
                                    #return -1
                                    break
                                else:
                                    R_={}
                                    R_[f(m)]=init_value#初始值init_value从m开始     
                                    eqs=[]
                                    print("The conjecture 'ite(%s, ite(%s, %s, %s),%s)' is NOT correct!"%(condition_1,condition_2,conj1,conj2,conj3))
                                    print("*"*20)
                                    pass
                        if break_Flag==True:
                            break
                    if break_Flag==True:
                        break
                if break_Flag==True:
                    break
            if break_Flag==True:
                break
        if break_Flag==True:
            break
        

  
if __name__=="__main__":

    Solve_nestedCond_r(2,2,n>5,n>7,f(n+1)-f(n)+n**3+2,f(n+1)-f(n)-n-1,f(n+1)-f(n)+6*n-4*n)

    
    
    
    
    
