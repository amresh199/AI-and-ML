#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("https://raw.githubusercontent.com/Mounika-Kajjam/Datasets/master/cities.csv")


# In[3]:


df


# In[4]:


df.describe()


# In[5]:



df.info()


# In[6]:


df1=pd.DataFrame(df.sample(axis=1))
df1


# In[7]:


s1=pd.DataFrame(df.sample(axis=1))
s1


# In[8]:


dfint = df.select_dtypes(include='int64')
dfint=dfint.astype(float)
dfint


# In[9]:


dffloat=df.select_dtypes(include='float64')
dffloat=dffloat.astype(int)
dffloat


# In[10]:


sns.heatmap(df.isnull())


# In[11]:


df1=pd.DataFrame(df)
for i in df1.columns:
    df1.drop_duplicates(i,inplace=True)
df1


# In[12]:


df[df.population_total==max(df['population_total'])]


# In[14]:


df2=df.groupby(['state_name'])['population_total'].mean()
df2=pd.DataFrame(df2)
df2.sort_values(by='population_total')


# In[15]:


df2.plot.barh(figsize=(5,5))


# In[16]:


df1=df.sort_values(by='population_total').head()
df1


# In[17]:


df2=df.sort_values(by='population_total',ascending=False).head()
df2


# In[18]:


pd.concat([df1,df2])


# In[ ]:




