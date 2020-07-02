#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data={'X1':[7,7,3,1],'X2':[7,4,4,4],'Y':["Bad","Bad","Good","Good"]}
data


# In[3]:


df=pd.DataFrame(data)
df


# In[4]:


x=3
y=7


# In[5]:


data1=data['X1']
data2=data['X2']
data1


# In[6]:


data2


# In[7]:


data3=[]
import math
for i in range(0,len(data1)):
    sq=(x-data1[i])**2 + (y-data2[i])**2
    data3.append(math.sqrt(sq))
data3


# In[8]:


df1=pd.DataFrame(data3,columns=['Distance'])
df1


# In[9]:


df2=pd.concat([df,df1],axis=1)
df2


# In[10]:


df2.sort_values(by=['Distance'],inplace=True)


# In[11]:


df2


# In[12]:


df.append({'X1':3,'X2':7,'Y':"Good"},ignore_index=True)


# In[13]:


data={'X1':[7,7,3,1],'X2':[7,4,4,4],'Y':["Bad","Bad","Good","Good"]}
data


# In[14]:


df=pd.DataFrame(data)
df


# In[15]:


x=3
y=7


# In[16]:


data1=data['X1']
data2=data['X2']
data1


# In[17]:


data2


# In[18]:


data3=[]
import math
for i in range(0,len(data1)):
    sq=(x-data1[i])**2 + (y-data2[i])**2
    data3.append(math.sqrt(sq))
data3


# In[19]:


df1=pd.DataFrame(data3,columns=['Distance'])
df1


# In[20]:


df2=pd.concat([df,df1],axis=1)
df2


# In[21]:


df2.sort_values(by=['Distance'],inplace=True)
df2


# In[22]:


df.append({'X1':3,'X2':7,'Y':"Good"},ignore_index=True)


# In[ ]:




