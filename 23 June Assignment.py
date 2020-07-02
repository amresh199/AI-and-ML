#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


data=pd.read_csv("https://raw.githubusercontent.com/Mounika-Kajjam/Datasets/master/titanic.csv")
data


# In[4]:


data.dtypes


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.isna().sum()


# In[8]:


data1=data.copy()
data1


# In[9]:


df=pd.DataFrame(data1)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df


# In[12]:


df.isna().sum()


# In[11]:


df['Age'].fillna(df['Age'].median(), inplace=True)
df


# In[13]:


df.isna().sum()


# In[14]:


df=pd.DataFrame(data1)

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Cabin'].fillna(df['Cabin'].mode()[0], inplace=True)
df


# In[15]:


df.isna().sum()


# In[16]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


# In[17]:


df.Sex=le.fit_transform(df.Sex)
df.Name=le.fit_transform(df.Name)
df.Ticket=le.fit_transform(df.Ticket)
df.Cabin=le.fit_transform(df.Cabin)
df.Embarked=le.fit_transform(df.Embarked)
df


# In[18]:


df=data.copy()
df.drop_duplicates()


# In[19]:


sns.pairplot(data)


# In[20]:


sns.heatmap(data.isna())


# In[22]:


data.hist(figsize=(12,12))


# In[23]:


for i in data.select_dtypes(include=['int64','float64']).columns:
    sns.boxplot(data[i])
    plt.show()


# In[24]:


X = df.drop('Survived',axis=1)
X.shape
y=df.iloc[:,0]
y.shape


# In[25]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.25,random_state=1)#random_state = to select the constant rows


# In[26]:


print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)


# In[27]:


X_train


# In[28]:


Y_train


# In[29]:


df


# In[ ]:




