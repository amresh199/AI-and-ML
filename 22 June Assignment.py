#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv("https://raw.githubusercontent.com/Mounika-Kajjam/Datasets/master/cities.csv")
data


# In[4]:


female_g=data.sort_values(by='female_graduates',ascending=False).head()
female_g


# In[5]:


female_l=data.sort_values(by='female_graduates').head()
female_l


# In[6]:


datahl=pd.concat([female_g,female_l])
datahl


# In[7]:


data[data['state_name'].isin(["MAHARASHTRA","BIHAR","KERALA"])]


# In[8]:


tgdata=data.sort_values(by='total_graduates',ascending=False).head(10)
tgdata


# In[9]:


data[data['state_name'].isin(["KERALA"])].child_sex_ratio.mean()


# In[ ]:




