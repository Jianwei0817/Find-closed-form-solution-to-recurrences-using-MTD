#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:44:29 2019
@author: jasonwang
"""

"""系统测试非条件类递归问题"""
from solver_recurr import *
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
F_=open("1.txt",'w+')

########type1#########################
for i in range(500):
    b_1=np.random.randint(0, 5)##base 为自然数
    b_2=np.random.randint(-5, 10)
    k_1=np.random.randint(0, 10)##k_1必须为正，才可以满足指数函数的定义
    while(k_1==0):
        k_1=np.random.randint(0, 10)
    p_1=np.random.randint(-5, 10)
    p_2=np.random.randint(-5, 10)
    p_3=np.random.randint(-5, 10)
    p_4=np.random.randint(-5, 10)
    p_5=np.random.randint(-5, 10)
    p_6=np.random.randint(-5, 10)
    p_7=np.random.randint(-5, 10)
    p_8=np.random.randint(-5, 10)
    p_9=np.random.randint(-5, 10)
    p_10=np.random.randint(-5, 10)
    p_11=np.random.randint(-5, 10)
    p_12=np.random.randint(-5, 10)
    p_13=np.random.randint(-5, 10)
    p_14=np.random.randint(-5, 10)
    p_15=np.random.randint(-5, 10)
    p_16=np.random.randint(-5, 10)
    
    print("****"*10,i)
    print("f(%s)=%s,f(n+1)-(%s)*f(n)+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s)*n**11+(%s)*n**12+(%s)*n**13+(%s)*n**14+(%s)*n**15+(%s)"%(b_1,b_2,k_1,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,p_12,p_13,p_14,p_15,p_16),file=F_)
    RES=Solve_r(b_1,b_2,f(n+1)-k_1*f(n)+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11)*n**11+(p_12)*n**12+(p_13)*n**13+(p_14)*n**14+(p_15)*n**15+(p_16))
    if RES==-1:
        print("NANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANAN",file=F_)
        T_NA += 1
        print("*"*36,file=F_)
    else: 
        CJ=RES[0]
        print('Congratulations!! The conjecture f(n)=%s must be correct!!!'%(CJ),file=F_)
        TIME=RES[1]
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
"""######type2#############################
for i in range(100):
    b_1=np.random.randint(0, 5)#base为自然数
    b_2=np.random.randint(-5, 5)
    k_1=np.random.randint(0, 10)##k_1必须为正，才可以满足指数函数的定义
    while(k_1==0):
        k_1=np.random.randint(0, 10)
    k_2=np.random.randint(-5, 5)
    while(k_2==0):
        k_2=np.random.randint(-5, 5)  
    p_1=np.random.randint(2, 10)##指数函数系数p_1>0 且不等于1  (p_1**n)
    print("f(%s)=%s,f(n+1)-(%s)*f(n)+(%s)*(%s)**n"%(b_1,b_2,k_1,k_2,p_1),file=F_)
    RES=Solve_r(b_1,b_2,f(n+1)-(k_1)*f(n)+(k_2)*(p_1)**n)
    if RES==-1:
        print("NANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANAN",file=F_)
        T_NA += 1
        print("*"*36,file=F_)
    else:
        CJ=RES[0]
        print('Congratulations!! The conjecture f(n)=%s must be correct!!!'%(CJ),file=F_)
        TIME=RES[1]
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
#############type 3############################
for i in range(100):
    b_1=np.random.randint(0, 5)##base 为自然数
    b_2=np.random.randint(-5, 10)
    k_1=np.random.randint(0, 5)##k_1必须为正，才可以满足指数函数的定义
    while(k_1==0):
        k_1=np.random.randint(0, 5)
    k_2=np.random.randint(-5, 5)
    while(k_2==0):
        k_2=np.random.randint(-5, 5)
    p_=np.random.randint(2, 5)##指数函数系数p_>0 且不等于1  (p_**n)
    p_1=np.random.randint(-5, 10)
    p_2=np.random.randint(-5, 10)
    p_3=np.random.randint(-5, 10)
    p_4=0#np.random.randint(-5, 10)
    p_5=np.random.randint(-5, 10)
    p_6=np.random.randint(-5, 10)
    p_7=np.random.randint(-5, 10)
    p_8=0#np.random.randint(-5, 10)
    p_9=0#np.random.randint(-5, 10)
    p_10=0#np.random.randint(-5, 10)
    p_11=0#np.random.randint(-5, 10)
    p_12=0#np.random.randint(-5, 10)
    p_13=0#np.random.randint(-5, 10)
    p_14=0#np.random.randint(-5, 10)
    p_15=0#np.random.randint(-5, 10)
    p_16=np.random.randint(-5, 10)
    
    print("****"*10,i)
    print("f(%s)=%s,f(n+1)-(%s)*f(n)+(%s)*(%s)**n+(%s)*n+(%s)*n**2+(%s)*n**3+(%s)*n**4+(%s)*n**5+(%s)*n**6+(%s)*n**7+(%s)*n**8+(%s)*n**9+(%s)*n**10+(%s)*n**11+(%s)*n**12+(%s)*n**13+(%s)*n**14+(%s)*n**15+(%s)"%(b_1,b_2,k_1,k_2,p_,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,p_12,p_13,p_14,p_15,p_16),file=F_)
    RES=Solve_r(b_1,b_2,f(n+1)-k_1*f(n)+(k_2)*(p_)**n+(p_1)*n+(p_2)*n**2+(p_3)*n**3+(p_4)*n**4+(p_5)*n**5+(p_6)*n**6+(p_7)*n**7+(p_8)*n**8+(p_9)*n**9+(p_10)*n**10+(p_11)*n**11+(p_12)*n**12+(p_13)*n**13+(p_14)*n**14+(p_15)*n**15+(p_16))
    if RES==-1:
        print("NANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANANAN",file=F_)
        T_NA += 1
        print("*"*36,file=F_)
    else: 
        CJ=RES[0]
        print('Congratulations!! The conjecture f(n)=%s must be correct!!!'%(CJ),file=F_)
        TIME=RES[1]
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
print("T_1:%s;T_3:%s;T_5:%s;T_10:%s;T_15:%s;T_30:%s;T_NA:%s;"%(T_1,T_3,T_5,T_10,T_15,T_30,T_NA),file=F_)"""
F_.close()
    

        
    
