# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:48:20 2019

@author: CodersMine
"""
a=[[1,1,1,1],
   [1,0,0,1],
   [1,1,1,1],
   [1,0,0,1],
   [1,0,0,1]]

b=[[1,1,1,1],
   [1,0,0,1],
   [1,1,1,1],
   [1,0,0,1],
   [1,1,1,1]]

c=[[1,1,1,1],
   [1,0,0,0],
   [1,0,0,0],
   [1,0,0,0],
   [1,1,1,1]]
d=[[1,0,0,0],
   [1,1,0,0],
   [1,0,1,0],
   [1,0,1,0],
   [1,1,0,0]]
e=[[1,1,1,1],
   [1,0,0,0],
   [1,1,1,0],
   [1,0,0,0],
   [1,1,1,1]]
f=[[1,1,1,1],
   [1,0,0,0],
   [1,1,1,0],
   [1,0,0,0],
   [1,0,0,0]]
g=[[1,1,1,1],
   [1,0,0,0],
   [1,0,1,1],
   [1,0,0,1],
   [1,1,1,1]]
h=[[1,0,0,1],
   [1,0,0,1],
   [1,1,1,1],
   [1,0,0,1],
   [1,0,0,1]]
i=[[1,1,1,1],
   [0,1,1,0],
   [0,1,1,0],
   [0,1,1,0],
   [1,1,1,1]]
j=[[1,1,1,1],
   [0,0,1,0],
   [0,0,1,0],
   [1,0,1,0],
   [1,1,1,0]]
k=[[1,0,0,1],
   [1,0,1,0],
   [1,1,0,0],
   [1,0,1,0],
   [1,0,0,1]]
l=[[1,0,0,0],
   [1,0,0,0],
   [1,0,0,0],
   [1,0,0,0],
   [1,1,1,1]]
m=[[1,0,0,1],
   [1,1,1,1],
   [1,0,0,1],
   [1,0,0,1],
   [1,0,0,1]]
n=[[1,0,0,1],
   [1,1,0,1],
   [1,0,1,1],
   [1,0,0,1],
   [0,0,0,0]]
o=[[1,1,1,1],
   [1,0,0,1],
   [1,0,0,1],
   [1,0,0,1],
   [1,1,1,1]]
p=[[1,1,1,1],
   [1,0,0,1],
   [1,1,1,1],
   [1,0,0,0],
   [1,0,0,0]]
q=[[1,1,1,0],
   [1,0,1,0],
   [1,0,1,0],
   [1,1,1,1],
   [0,0,0,1]]
r=[[1,1,1,1],
   [1,0,0,1],
   [1,1,1,1],
   [1,0,1,0],
   [1,0,0,1]]
s=[[1,1,1,1],
   [1,0,0,0],
   [1,1,1,1],
   [0,0,0,1],
   [1,1,1,1]]
t=[[1,1,1,1],
   [0,1,1,0],
   [0,1,1,0],
   [0,1,1,0],
   [0,1,1,0]]
u=[[1,0,0,1],
   [1,0,0,1],
   [1,0,0,1],
   [1,0,0,1],
   [1,1,1,1]]
v=[[1,0,0,1],
   [1,0,0,1],
   [1,0,0,1],
   [0,1,1,0],
   [0,1,1,0]]
w=[[1,0,0,1],
   [1,0,0,1],
   [1,0,0,1],
   [1,1,1,1],
   [1,0,0,1]]
x=[[1,0,0,1],
   [0,1,1,0],
   [0,1,1,0],
   [1,0,0,1],
   [0,0,0,0]]
y=[[1,0,0,1],
   [0,1,0,1],
   [0,0,1,0],
   [0,0,1,0],
   [0,0,1,0]]
z=[[1,1,1,1],
   [0,0,0,1],
   [0,0,1,0],
   [0,1,0,0],
   [1,1,1,1]]

def print_star(word):
    for i in range(len(word)):
        for j in range(len(word[0])):
            if(word[i][j]==1):
                print("*",end='')
            else:
                print(" ",end='')
        print("")
        
        
print_star(a)
print_star(c)
print_star(b)

dic=dict(a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j,k=k,l=l,m=m,n=n,o=o,p=p,q=q,r=r,s=s,t=t,u=u,v=v,w=w,x=x,y=y,z=z)

for num in range(26):
    temp=chr(ord('a')+num)
    print_star(dic[temp])
    print("\n")
    
"""
to generate dictionary

for num in range(26):
    temp=chr(ord('a')+num)
    print(temp+"="+temp+",",end="")
"""  