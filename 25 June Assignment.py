#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from sklearn.datasets import load_boston
boston=load_boston()


# In[3]:


df=pd.DataFrame(boston.data,columns=boston.feature_names)
df.head()


# In[4]:


df['MDV']=boston.target
df.head()


# In[5]:


for i in boston.feature_names:
    plt.xlabel("MDV")
    plt.ylabel(i)
    plt.scatter(df['MDV'],df[i])
    plt.show()


# In[6]:


plt.figure(figsize=(10,10))
sns.heatmap(df.corr()[df.corr()>=0.9],annot=True)


# In[7]:


x=df.drop(['MDV','RAD'],axis=1)
x


# In[8]:


y=df[['MDV']]
y


# In[9]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)


# In[10]:


print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


# In[11]:


from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)


# In[12]:


y_pred=lr.predict(x_test)


# In[13]:


from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import math


# In[14]:


print("r2_score:",r2_score(y_test,y_pred))
print("adjusted_r2_score:",1- (1-r2_score(y_test, y_pred))*(len(x_test)-1)/
                                  (len(x_test)-x_test.shape[1]-1))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))
print("RMSE:",math.sqrt(mean_squared_error(y_test,y_pred)))


# In[ ]:




