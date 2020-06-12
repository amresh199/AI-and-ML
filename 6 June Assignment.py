#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv("https://raw.githubusercontent.com/kotagiri-preeti/Summer-Internship-AI-and-ML/master/german_credit_data.csv")
df


# In[2]:


df.drop(['Unnamed: 0'],axis=1,inplace=True)# removing the column which is Unnamed
df


# In[3]:


df.head(7)# to get top 7 rows


# In[4]:


df.tail(3)# to get last 3 rows


# In[5]:


#Total Number of entries
print(df.shape[0]) # to get the total number of rows


# In[6]:


print("The number of features in the data is",df.shape[1])# to get the total no. of columns
print("The Feature for the data is:")
for i in df.columns:      # to get all the columns from the data
    print(i)


# In[7]:


print(list(df.index)) # print the row indices of the dataframe


# In[8]:


d=df.dtypes
d


# In[9]:


df.describe(include=[np.number])


# In[10]:


df.describe(include=[np.object])


# In[11]:


df.isnull().sum()


# In[12]:


df.info()


# In[13]:


df.iloc[0:3] # access the rows using iloc


# In[14]:


df.iloc[:,0:4] # access the columns using iloc


# In[15]:


df.loc[0:5] # access the rows using loc


# In[16]:


df.loc[:,'Age'] # access the columns using loc


# In[17]:


for i in df.columns:
    print(i,len(df[i].unique()))


# In[ ]:




