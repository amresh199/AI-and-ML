#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#1
a=np.array([12,13,14,15, 16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37])
print(a)
print(a[::-1])


# In[3]:


#2 Question
m=int(input("enter the number of rows"))
n=int(input("enter the number of columns"))
a=np.ones((m,n))
print("original array")
print(a)
a[1:m-1,1:n-1]=0
print("array with border 1")
print(a)


# In[4]:


#3 Question
a=list(map(int,input("enter array 1").split()))
arr1=np.array(a)
a=list(map(int,input("enter array 2").split()))
arr2=np.array(a)
print(arr1)
print(arr2)
result=(i in arr2 for i in arr1 )
print(np.array(list(result)))


# In[5]:


#4 Question
arr1=np.array(list(map(int,input("enter the array1").split())))
arr2=np.array(list(map(int,input("enter the array2").split())))
print(np.setdiff1d(arr1,arr2))


# In[6]:


#5 Question

a=np.array([4,5,6,8])
d=np.diag(a)
print(d)


# In[ ]:




