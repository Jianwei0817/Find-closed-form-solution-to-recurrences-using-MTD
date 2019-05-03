#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 20:15:28 2019

@author: jasonwang
"""

from add20190324 import *
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
F_=open("add86.txt",'w+')
"""
########type1#########################
for i in range(10):
    b_1=np.random.randint(0, 10)##base 为自然数
    b_2=np.random.randint(-20, 20)
    k=np.random.randint(1, 20)
    r=np.random.randint(-5, 5)
    

    
    
    print("****"*10,i)
    print("f(%s)=%s,f(n+1)-(%s)*f(n)+(%s)*f(n)**2)"%(b_1,b_2,k,r),file=F_)
    RES=Solve_r(b_1,b_2,f(n+1)-k*f(n)+r*f(n)**2)
    if RES[0]==-1:
        condition=RES[1]
        conj1=RES[2]
        conj2=RES[3]
        print("Sorry, we cannot find the closed form solution to this recurrence in 30 mins! And the last conjecture we try is 'ite(%s,%s,%s)'"%(condition,conj1,conj2),file=F_)
        T_NA += 1
        print("*"*36,file=F_)
    else: 
        TIME=RES[3]
        print("Congratulations!! The conjecture 'ite(%s, %s, %s)' is correct!!!"%(RES[0],RES[1],RES[2]),file=F_)
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
########type2#########################
for i in range(40):
    b_1=np.random.randint(0, 10)##base 为自然数
    b_2=np.random.randint(-20, 20)
    k=np.random.randint(1, 20)
    r=np.random.randint(-5, 5)
    
    p_1=np.random.randint(-6,6)
    p_2=np.random.randint(-6,6)
    p_3=np.random.randint(-6,6)
    p_4=np.random.randint(-6,6)
    p_5=np.random.randint(-6,6)
    p_6=np.random.randint(-6,6)
    p_7=np.random.randint(-6,6)
    p_8=np.random.randint(-6,6)
    
    print("****"*10,i)
    print("f(%s)=%s,f(n+1)-(%s)*f(n)+(%s)*f(n)**2+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s))"%(b_1,b_2,k,r,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8),file=F_)
    RES=Solve_r(b_1,b_2,f(n+1)-k*f(n)+r*f(n)**2+p_1*n+p_2*n**2+p_3*n**3+p_4*n**4+p_5*n**5+p_6*n**6+p_7*n**7+p_8)
    if RES[0]==-1:
        condition=RES[1]
        conj1=RES[2]
        conj2=RES[3]
        print("Sorry, we cannot find the closed form solution to this recurrence in 10 mins! And the last conjecture we try is 'ite(%s,%s,%s)'"%(condition,conj1,conj2),file=F_)
        T_NA += 1
        print("*"*36,file=F_)
    else: 
        TIME=RES[3]
        print("Congratulations!! The conjecture 'ite(%s, %s, %s)' is correct!!!"%(RES[0],RES[1],RES[2]),file=F_)
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
