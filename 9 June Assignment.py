#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
d=pd.read_csv("cricket.csv")
d
data1=d["ManOfMach"].value_counts().rename_axis('players').reset_index(name='no.of ManOfMach')
data2=data1.sort_values(by=['players'],ascending=True)
data2.head(29)


# In[16]:


df3=d["Country_Name"].value_counts()[:10].plot(kind="pie",colors=["blue","green","red"],autopct="%0.1f%%",explode=[0.2,0,0],startangle=40,radius=1.2)
df3


# In[ ]:




