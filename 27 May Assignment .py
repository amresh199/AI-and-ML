#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print()


# In[2]:


#2
n=int(input("enter the number of rows"))
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print()


# In[3]:


#3
k =int(input("enter the number for multiplication table"))
for i in range(1,11):
    print(k," * ",i," = ",k*i)


# In[3]:


#4
import math
a=int(input("a coefficient"))
b=int(input("b coefficient"))
c=int(input("c coefficient"))
print("roots are ",(-b+math.sqrt(b**2 -4*a*c))/2*a," and ",(-b-math.sqrt(b**2 -4*a*c))/2*a)


# In[4]:


#5
n=int(input("enter a decimal value"))
bin=""
while(n>0):
    bin+=str(n%2)
    n=n//2
print(bin[::-1])


# In[5]:


#6
n=int(input("enter the number"))
f1=0
f2=1
if(n==0):
    print(0)
elif(n==1):
    print(f1)
else:
    print(f1,f2,end=" ")
    sum=0
    for i in range(2,n):
        sum=f1+f2
        f1=f2
        f2=sum
        print(f2,end=" ")


# In[ ]:




