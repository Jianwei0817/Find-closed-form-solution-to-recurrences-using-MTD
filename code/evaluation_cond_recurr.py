#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:44:29 2019
@author: jasonwang
"""

"""系统测试条件类递归问题"""
from solver_cond_recurr import *
from numpy import *
import numpy as np
#a=numpy.random.randint(0, 1)
#print(a)
####用来计数时间
T_1=0#1分钟内
T_3=0
T_5=0
T_10=0
T_15=0
T_30=0

T_NA=0 #30分钟外，无解
F_=open("34_100_3.txt",'w+')

"""########type1#########################
for i in range(500):
    b_1=np.random.randint(0, 5)##base 为自然数
    b_2=np.random.randint(-5, 10)
    c_=np.random.randint(0, 15)##n>c_,c_的绝对值理论上应该大于b_1    
    while(c_< b_1):
        c_=np.random.randint(0, 15)
    p_1=np.random.randint(-5, 10)
    p_2=np.random.randint(-5, 10)
    p_3=np.random.randint(-5, 10)
    p_4=np.random.randint(-5, 10)
    p_5=np.random.randint(-5, 10)
    p_6=np.random.randint(-5, 10)
    p_7=np.random.randint(-5, 10)
    p_8=0#np.random.randint(-5, 10)
    p_9=0#np.random.randint(-5, 10)
    p_10=0#np.random.randint(-5, 10)
    p_11=np.random.randint(-5, 10)
    
    P_1=np.random.randint(-5, 10)
    P_2=np.random.randint(-5, 10)
    P_3=np.random.randint(-5, 10)
    P_4=np.random.randint(-5, 10)
    P_5=np.random.randint(-5, 10)
    P_6=np.random.randint(-5, 10)
    P_7=np.random.randint(-5, 10)
    P_8=0#np.random.randint(-5, 10)  
    P_9=0#np.random.randint(-5, 10)
    P_10=0#np.random.randint(-5, 10)
    P_11=np.random.randint(-5, 10)

    cset=['>','<',">=","<="]
    cs=np.random.randint(0, 4)
    
    print("****"*10,i)
    
    if cs==0:        
        print("f(%s)=%s,ite(n>(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s))"%(b_1,b_2,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8,P_9,P_10,P_11),file=F_)
        res=Solve_cond_r(b_1,b_2,n>c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8)*n**8+(P_9)*n**9+(P_10)*n**10+P_11)
    elif cs==1:
        print("f(%s)=%s,ite(n<(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s))"%(b_1,b_2,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8,P_9,P_10,P_11),file=F_)
        res=Solve_cond_r(b_1,b_2,n<c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8)*n**8+(P_9)*n**9+(P_10)*n**10+P_11)
    elif cs==2:
        print("f(%s)=%s,ite(n>=(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s))"%(b_1,b_2,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8,P_9,P_10,P_11),file=F_)
        res=Solve_cond_r(b_1,b_2,n>=c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8)*n**8+(P_9)*n**9+(P_10)*n**10+P_11)
    else:
        print("f(%s)=%s,ite(n<=(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s))"%(b_1,b_2,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8,P_9,P_10,P_11),file=F_)
        res=Solve_cond_r(b_1,b_2,n<=c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8)*n**8+(P_9)*n**9+(P_10)*n**10+P_11)


    if res==-1:
        print("NANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANAN",file=F_)
        T_NA += 1
        print("*"*36,file=F_)
    else: 
        TIME=res[3]
        print("The conjecture 'ite(%s, %s, %s)' is correct."%(res[0],res[1],res[2]),file=F_)
        print("Usage of time:",TIME,"seconds",file=F_)
        if TIME <= 60:
            T_1 += 1
        elif TIME >60 and TIME <= 180:
            T_3 += 1
        elif TIME >180 and TIME <= 300:
            T_5 += 1
        elif TIME >300 and TIME <= 600:
            T_10 += 1
        elif TIME >600 and TIME <= 900:
            T_15 += 1
        else:
            T_30 += 1
        print("*"*36,file=F_)
        print("ok")

########type2#########################
for i in range(500):
    b_1=np.random.randint(0, 5)##base 为自然数
    b_2=np.random.randint(-5, 10)
    c_=np.random.randint(20, 100)##n>c_,c_的绝对值理论上应该大于b_1    
    while(c_< (b_1**2)):
        c_=np.random.randint(20, 100)
    p_1=np.random.randint(-5, 10)
    p_2=np.random.randint(-5, 10)
    p_3=np.random.randint(-5, 10)
    p_4=np.random.randint(-5, 10)
    p_5=np.random.randint(-5, 10)
    p_6=np.random.randint(-5, 10)
    p_7=np.random.randint(-5, 10)
    p_8=0#np.random.randint(-5, 10)
    p_9=0#np.random.randint(-5, 10)
    p_10=0#np.random.randint(-5, 10)
    p_11=np.random.randint(-5, 10)
    
    P_1=np.random.randint(-5, 10)
    P_2=np.random.randint(-5, 10)
    P_3=np.random.randint(-5, 10)
    P_4=np.random.randint(-5, 10)
    P_5=np.random.randint(-5, 10)
    P_6=np.random.randint(-5, 10)
    P_7=np.random.randint(-5, 10)
    P_8=0#np.random.randint(-5, 10)  
    P_9=0#np.random.randint(-5, 10)
    P_10=0#np.random.randint(-5, 10)
    P_11=np.random.randint(-5, 10)

    cset=['>','<',">=","<="]
    cs=np.random.randint(0, 4)
    
    print("****"*10,i)
    if cs==0:
        print("f(%s)=%s,ite(n**2>(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s))"%(b_1,b_2,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8,P_9,P_10,P_11),file=F_)
        res=Solve_cond_r(b_1,b_2,n**2>c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8)*n**8+(P_9)*n**9+(P_10)*n**10+P_11)
    elif cs==1:
        print("f(%s)=%s,ite(n**2<(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s))"%(b_1,b_2,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8,P_9,P_10,P_11),file=F_)
       res=Solve_cond_r(b_1,b_2,n**2<c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8)*n**8+(P_9)*n**9+(P_10)*n**10+P_11)
    elif cs==2:
        print("f(%s)=%s,ite(n**2>=(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s))"%(b_1,b_2,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8,P_9,P_10,P_11),file=F_)
        res=Solve_cond_r(b_1,b_2,n**2>=c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8)*n**8+(P_9)*n**9+(P_10)*n**10+P_11)
    else:
        print("f(%s)=%s,ite(n**2<=(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s))"%(b_1,b_2,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8,P_9,P_10,P_11),file=F_)
        res=Solve_cond_r(b_1,b_2,n**2<=c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8)*n**8+(P_9)*n**9+(P_10)*n**10+P_11)
         
    
    if res==-1:
        print("NANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANAN",file=F_)
        T_NA += 1
        print("*"*36,file=F_)
    else: 
        TIME=res[3]
        print("The conjecture 'ite(%s, %s, %s)' is correct."%(res[0],res[1],res[2]),file=F_)
        print("Usage of time:",TIME,"seconds",file=F_)
        if TIME <= 60:
            T_1 += 1
        elif TIME >60 and TIME <= 180:
            T_3 += 1
        elif TIME >180 and TIME <= 300:
            T_5 += 1
        elif TIME >300 and TIME <= 600:
            T_10 += 1
        elif TIME >600 and TIME <= 900:
            T_15 += 1
        else:
            T_30 += 1
        print("*"*36,file=F_)
        print("ok")

########type3#########################
for i in range(500):
    b_1=np.random.randint(0, 5)##base 为自然数
    b_2=np.random.randint(-5, 10)
    
    c_=np.random.randint(20, 200)
    ##条件多项式参数
    pP_1=np.random.randint(-5, 10)
    pP_2=np.random.randint(-5, 10)
    pP_3=np.random.randint(-5, 10)
    pP_4=np.random.randint(-5, 10)
    pP_5=np.random.randint(-5, 10)
    pP_6=np.random.randint(-5, 10)
    pP_7=np.random.randint(-5, 10)

    ##表达式1多项式参数
    p_1=np.random.randint(-5, 10)
    p_2=np.random.randint(-5, 10)
    p_3=np.random.randint(-5, 10)
    p_4=np.random.randint(-5, 10)
    p_5=np.random.randint(-5, 10)
    p_6=np.random.randint(-5, 10)
    p_7=np.random.randint(-5, 10)
    p_8=np.random.randint(-5, 10)
    ##表达式2多项式参数
    P_1=np.random.randint(-5, 10)
    P_2=np.random.randint(-5, 10)
    P_3=np.random.randint(-5, 10)
    P_4=np.random.randint(-5, 10)
    P_5=np.random.randint(-5, 10)
    P_6=np.random.randint(-5, 10)
    P_7=np.random.randint(-5, 10)
    P_8=np.random.randint(-5, 10)  
    
    cset=['>','<',">=","<="]
    cs=np.random.randint(0, 4)
    
    print("****"*10,i)
    
    if cs==0:
        print("f(%s)=%s,ite((%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7>(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s))"%(b_1,b_2,pP_1,pP_2,pP_3,pP_4,pP_5,pP_6,pP_7,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8),file=F_)
        res=Solve_cond_r(b_1,b_2,(pP_1)*n+(pP_2)*n**2+(pP_3)*n**3+(pP_4)*n**4+(pP_5)*n**5+(pP_6)*n**6+(pP_7)*n**7>c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8))
    elif cs==1:
        print("f(%s)=%s,ite((%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7<(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s))"%(b_1,b_2,pP_1,pP_2,pP_3,pP_4,pP_5,pP_6,pP_7,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8),file=F_)
        res=Solve_cond_r(b_1,b_2,(pP_1)*n+(pP_2)*n**2+(pP_3)*n**3+(pP_4)*n**4+(pP_5)*n**5+(pP_6)*n**6+(pP_7)*n**7<c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8))
    elif cs==2:
        print("f(%s)=%s,ite((%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7>=(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s))"%(b_1,b_2,pP_1,pP_2,pP_3,pP_4,pP_5,pP_6,pP_7,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8),file=F_)
        res=Solve_cond_r(b_1,b_2,(pP_1)*n+(pP_2)*n**2+(pP_3)*n**3+(pP_4)*n**4+(pP_5)*n**5+(pP_6)*n**6+(pP_7)*n**7>=c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8))    
    else:
        print("f(%s)=%s,ite((%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7<=(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s))"%(b_1,b_2,pP_1,pP_2,pP_3,pP_4,pP_5,pP_6,pP_7,c_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8),file=F_)
        res=Solve_cond_r(b_1,b_2,(pP_1)*n+(pP_2)*n**2+(pP_3)*n**3+(pP_4)*n**4+(pP_5)*n**5+(pP_6)*n**6+(pP_7)*n**7<=c_,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8))
    
    if res==-1:
        print("NANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANAN",file=F_)
        T_NA += 1
        print("*"*36,file=F_)
    else: 
        TIME=res[3]
        print("The conjecture 'ite(%s, %s, %s)' is correct."%(res[0],res[1],res[2]),file=F_)
        print("Usage of time:",TIME,"seconds",file=F_)
        if TIME <= 60:
            T_1 += 1
        elif TIME >60 and TIME <= 180:
            T_3 += 1
        elif TIME >180 and TIME <= 300:
            T_5 += 1
        elif TIME >300 and TIME <= 600:
            T_10 += 1
        elif TIME >600 and TIME <= 900:
            T_15 += 1
        else:
            T_30 += 1
        print("*"*36,file=F_)
        print("ok")

""" 

########type4#########################
for i in range(100):
    b_1=np.random.randint(0, 5)##base 为自然数
    b_2=np.random.randint(-5, 5)
    
    ##条件1中f(n)系数分子分母---主要目的：为了减小运算量
    zk_1=np.random.randint(-3, 3)
    mk_1=np.random.randint(1, 10)
    
    #条件1参数
    c_1=np.random.randint(20, 100)
    pP1_1=np.random.randint(-3, 3)
    pP1_2=np.random.randint(-3, 3)
    pP1_3=np.random.randint(-3, 3)
    pP1_4=np.random.randint(-3, 3)
    pP1_5=np.random.randint(-3, 3)
    pP1_6=np.random.randint(-3, 3)
    pP1_7=np.random.randint(-3, 3)

    
    p_1=np.random.randint(-3, 3)
    p_2=np.random.randint(-3, 3)
    p_3=np.random.randint(-3, 3)
    p_4=np.random.randint(-3, 3)
    p_5=np.random.randint(-3, 3)
    p_6=np.random.randint(-3, 3)
    p_7=np.random.randint(-3, 3)
    p_8=np.random.randint(-3, 3)

    
    P_1=np.random.randint(-3, 3)
    P_2=np.random.randint(-3, 3)
    P_3=np.random.randint(-3, 3)
    P_4=np.random.randint(-3, 3)
    P_5=np.random.randint(-3, 3)
    P_6=np.random.randint(-3, 3)
    P_7=np.random.randint(-3, 3)
    P_8=np.random.randint(-3, 3)  


    cset=['>','<',">=","<="]
    cs=np.random.randint(0, 4)
    
    print("****"*10,i)
    
    if cs==0:        
        print("f(%s)=%s,ite((%s)*f(n)/(%s)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7>(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s))"%(b_1,b_2,zk_1,mk_1,pP1_1,pP1_2,pP1_3,pP1_4,pP1_5,pP1_6,pP1_7,c_1,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8),file=F_)
        res=Solve_cond_r(b_1,b_2,(zk_1)*f(n)/(mk_1)+(pP1_1)*n+(pP1_2)*n**2+(pP1_3)*n**3+(pP1_4)*n**4+(pP1_5)*n**5+(pP1_6)*n**6+(pP1_7)*n**7>c_1,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8))

    elif cs==1:
        print("f(%s)=%s,ite((%s)*f(n)/(%s)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7<(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s))"%(b_1,b_2,zk_1,mk_1,pP1_1,pP1_2,pP1_3,pP1_4,pP1_5,pP1_6,pP1_7,c_1,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8),file=F_)
        res=Solve_cond_r(b_1,b_2,(zk_1)*f(n)/(mk_1)+(pP1_1)*n+(pP1_2)*n**2+(pP1_3)*n**3+(pP1_4)*n**4+(pP1_5)*n**5+(pP1_6)*n**6+(pP1_7)*n**7<c_1,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8))
    elif cs==2:
        print("f(%s)=%s,ite((%s)*f(n)/(%s)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7>=(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s))"%(b_1,b_2,zk_1,mk_1,pP1_1,pP1_2,pP1_3,pP1_4,pP1_5,pP1_6,pP1_7,c_1,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8),file=F_)
        res=Solve_cond_r(b_1,b_2,(zk_1)*f(n)/(mk_1)+(pP1_1)*n+(pP1_2)*n**2+(pP1_3)*n**3+(pP1_4)*n**4+(pP1_5)*n**5+(pP1_6)*n**6+(pP1_7)*n**7>=c_1,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8))
    else:
        print("f(%s)=%s,ite((%s)*f(n)/(%s)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7<=(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s),f(n+1)-f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s))"%(b_1,b_2,zk_1,mk_1,pP1_1,pP1_2,pP1_3,pP1_4,pP1_5,pP1_6,pP1_7,c_1,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8),file=F_)
        res=Solve_cond_r(b_1,b_2,(zk_1)*f(n)/(mk_1)+(pP1_1)*n+(pP1_2)*n**2+(pP1_3)*n**3+(pP1_4)*n**4+(pP1_5)*n**5+(pP1_6)*n**6+(pP1_7)*n**7<=c_1,f(n+1)-f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8),f(n+1)-f(n)+(P_1)*n+(P_2)*n**2+(P_3)*n**3+(P_4)*n**4+(P_5)*n**5+(P_6)*n**6+(P_7)*n**7+(P_8))
    if res==-1:
        print("NANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANAN",file=F_)
        T_NA += 1
        print("*"*36,file=F_)
    else: 
        TIME=res[3]
        print("The conjecture 'ite(%s, %s, %s)' is correct."%(res[0],res[1],res[2]),file=F_)
        print("Usage of time:",TIME,"seconds",file=F_)
        if TIME <= 60:
            T_1 += 1
        elif TIME >60 and TIME <= 180:
            T_3 += 1
        elif TIME >180 and TIME <= 300:
            T_5 += 1
        elif TIME >300 and TIME <= 600:
            T_10 += 1
        elif TIME >600 and TIME <= 900:
            T_15 += 1
        else:
            T_30 += 1
        print("*"*36,file=F_)
        print("ok")

print("T_1:%s;T_3:%s;T_5:%s;T_10:%s;T_15:%s;T_30:%s;T_NA:%s;"%(T_1,T_3,T_5,T_10,T_15,T_30,T_NA),file=F_)

F_.close()
    

        
    
