#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import 


# In[8]:


data=pd.read_table("https://data.princeton.edu/wws509/datasets/salary.dat",sep="\s+")


# In[9]:


data


# In[11]:


data.isna().sum()


# In[13]:


data.select_dtypes(include='int64')


# In[14]:


data.select_dtypes(exclude='int64')


# In[15]:


cat=data.select_dtypes(include=['object']).columns
cat


# In[16]:


for i in range(0,len(cat)):
     print(cat[i],':\n',data[cat[i]].value_counts(),'\n')


# In[18]:


dummy_set1=pd.get_dummies(data.sx,prefix="sx")
dummy_set1


# In[19]:


dummy_set2=pd.get_dummies(data.dg,prefix="dg")
dummy_set2


# In[21]:


merged_data=pd.concat([data,dummy_set1,dummy_set2],axis=1)
merged_data


# In[22]:


merged_data.drop(['sx_male','dg_doctorate'],axis=1,inplace=True)
merged_data


# In[ ]:




