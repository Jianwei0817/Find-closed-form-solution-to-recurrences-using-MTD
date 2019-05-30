import re
##输入try.txt 输出1.txt
f = open("t2.txt")
F_=open("t3.txt",'w+')
F=open("t4.txt",'w+')
line = f.readline()
#while line:
#    if "f(n+1)" in str(line):        
#        print(line.strip(),file=F_)
#    line = f.readline()
#去掉首行开头部分和斜杠后 打开1.txt  输出2.txt
#while line:
#    if "m" in str(line):
#        p=re.findall(r"-?\d+",str(line))
#        print(p,file=F_)
#    line = f.readline()
###   打开2.txt 处理数据格式 输入到methematica  输出3 and 4.txt 
"exp1_1"
#while line:
#    temp=[]
#    temp2=[]
#    tt=line.strip().split(",")
#    for i in tt:
#        p=re.findall(r"-?\d+",i)
#        temp.append(int(p[0]))                  
#    print(temp,file=F_) 
#    
#    for i in temp:
#        temp2.append(str(i))
#    temp2=" ".join(temp2)
#    print(temp2,file=F)
#    line = f.readline() 
"exp1_2"
#while line:
#    temp=[]
#    temp2=[]
#    tt=line.strip().split(",")
#    for i in tt:
#        p=re.findall(r"-?\d+",i)
#        temp.append(int(p[0]))
#    ##将系数反过来 
#    temp[3]=temp[3]*(-1) 
#    temp[4]=temp[4]*(-1)    
#    temp[5]=temp[5]*(-1) 
#    temp[6]=temp[6]*(-1) 
#    temp[7]=temp[7]*(-1)
#    temp[8]=temp[8]*(-1)   
#    temp[9]=temp[9]*(-1) 
#    temp[10]=temp[10]*(-1)
#    temp[11]=temp[11]*(-1)  
#    temp[12]=temp[12]*(-1) 
#    temp[13]=temp[13]*(-1) 
#    temp[14]=temp[14]*(-1)
#    temp[15]=temp[15]*(-1)   
#    temp[16]=temp[16]*(-1) 
#    temp[17]=temp[17]*(-1)
#    temp[18]=temp[18]*(-1)  
#
#      
#    print(temp,file=F_) 
#    
#    for i in temp:
#        temp2.append(str(i))
#    temp2=" ".join(temp2)
#    print(temp2,file=F)
#    line = f.readline()  
"exp1_3"
#while line:
#    temp=[]
#    temp2=[]
#    tt=line.strip().split(",")
#    for i in tt:
#        p=re.findall(r"-?\d+",i)
#        temp.append(int(p[0]))
#    ##将系数反过来 
#    temp[-1]=temp[-1]*(-1)                 
#    print(temp,file=F_) 
#    
#    for i in temp:
#        temp2.append(str(i))
#    temp2=" ".join(temp2)
#    print(temp2,file=F)
#    line = f.readline()  
"exp1_4"
#while line:
#    temp=[]
#    temp2=[]
#    tt=line.strip().split(",")
#    for i in tt:
#        p=re.findall(r"-?\d+",i)
#        temp.append(int(p[0]))
#    ##将系数反过来 
#    temp[3]=temp[3]*(-1)  
#    temp[4]=temp[4]*(-1)
#    temp[5]=temp[5]*(-1) 
#    temp[6]=temp[6]*(-1) 
#    temp[7]=temp[7]*(-1)
#    temp[8]=temp[8]*(-1)   
#    temp[9]=temp[9]*(-1) 
#    temp[10]=temp[10]*(-1)
#    temp[11]=temp[11]*(-1)          
#    print(temp,file=F_) 
#    
#    for i in temp:
#        temp2.append(str(i))
#    temp2=" ".join(temp2)
#    print(temp2,file=F)
#    line = f.readline() 
"exp1_5"    
#while line:
#    temp=[]
#    temp2=[]
#    tt=line.strip().split(",")
#    for i in tt:
#        p=re.findall(r"-?\d+",i)
#        temp.append(int(p[0]))
#    ##将系数反过来 
#    temp[3]=temp[3]*(-1)           
#    print(temp,file=F_) 
#    
#    for i in temp:
#        temp2.append(str(i))
#    temp2=" ".join(temp2)
#    print(temp2,file=F)
#    line = f.readline() 
"exp1_6"
while line:
    temp=[]
    temp2=[]
    tt=line.strip().split(",")
    for i in tt:
        p=re.findall(r"-?\d+",i)
        temp.append(int(p[0]))
    ##将系数反过来 
    temp[3]=temp[3]*(-1)  
    temp[5]=temp[5]*(-1) 
    temp[6]=temp[6]*(-1) 
    temp[7]=temp[7]*(-1)
    temp[8]=temp[8]*(-1)   
    temp[9]=temp[9]*(-1) 
    temp[10]=temp[10]*(-1)
    temp[11]=temp[11]*(-1)  
    temp[12]=temp[12]*(-1) 
    temp[13]=temp[13]*(-1) 
    temp[14]=temp[14]*(-1)
    temp[15]=temp[15]*(-1)   
    temp[16]=temp[16]*(-1) 
    temp[17]=temp[17]*(-1)
    temp[18]=temp[18]*(-1)  
    temp[19]=temp[19]*(-1) 
    temp[20]=temp[20]*(-1)
      
    print(temp,file=F_) 
    
    for i in temp:
        temp2.append(str(i))
    temp2=" ".join(temp2)
    print(temp2,file=F)
    line = f.readline() 
f.close()
F_.close()
F.close()
 

