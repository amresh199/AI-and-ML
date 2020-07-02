#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


print(np.__version__)
print(pd.__version__)
print(sns.__version__)


# In[4]:


from sklearn.datasets import load_boston


# In[5]:


bson=load_boston()


# In[6]:


bson.keys()


# In[7]:


bson.target


# In[8]:


bson.feature_names


# In[9]:


print(bson.DESCR)


# In[10]:


df=pd.DataFrame(bson.data,columns=bson.feature_names)
df


# In[11]:


df['MEDV']=bson.target
df.head()


# In[12]:


df.info()


# In[13]:


df.describe()


# In[14]:


sns.distplot(df.MEDV)


# In[16]:


df[df.duplicated()]


# In[17]:


RM_y=df[['MEDV']]
RM_y


# In[18]:


RM_x=df[['RM']]
RM_x


# In[19]:


from sklearn.model_selection import train_test_split
RM_x_train,RM_x_test,RM_y_train,RM_y_test=train_test_split(RM_x,RM_y,test_size=0.2,random_state=2)


# In[20]:


print(RM_x_train.shape)
print(RM_y_train.shape)
print(RM_x_test.shape)
print(RM_y_test.shape)


# In[21]:


from sklearn.linear_model import LinearRegression


# In[22]:


le=LinearRegression()
le.fit(RM_x_train,RM_y_train)


# In[23]:


RM_y_pred=le.predict(RM_x_test)


# In[24]:


from sklearn.metrics import r2_score
r2_score(RM_y_test,RM_y_pred)


# In[25]:


plt.xlabel("RM")
plt.ylabel("MEDV")
plt.scatter(RM_x,RM_y,color="Red")
plt.plot(RM_x_test,RM_y_pred,color="Black")
plt.show()


# In[26]:


LSTAT_y=df[['MEDV']]
LSTAT_y


# In[27]:


LSTAT_x=df[['LSTAT']]
LSTAT_x


# In[28]:


LSTAT_x_train,LSTAT_x_test,LSTAT_y_train,LSTAT_y_test=train_test_split(LSTAT_x,LSTAT_y,test_size=0.2,random_state=2)
print(LSTAT_x_train.shape)
print(LSTAT_y_train.shape)
print(LSTAT_x_test.shape)
print(LSTAT_y_test.shape)


# In[29]:


le.fit(LSTAT_x_train,LSTAT_y_train)

LSTAT_y_pred=le.predict(LSTAT_x_test)

r2_score(LSTAT_y_test,LSTAT_y_pred)


# In[30]:


plt.xlabel("LSTAT")
plt.ylabel("MEDV")
plt.scatter(LSTAT_x,LSTAT_y,color="Red")
plt.plot(LSTAT_x_test,LSTAT_y_pred,color="Black")
plt.show()


# In[31]:


PTRATIO_y=df[['MEDV']]
PTRATIO_y


# In[32]:


PTRATIO_x=df[['PTRATIO']]
PTRATIO_x


# In[33]:


PTRATIO_x_train,PTRATIO_x_test,PTRATIO_y_train,PTRATIO_y_test=train_test_split(PTRATIO_x,PTRATIO_y,
                                                                               test_size=0.2,random_state=2)

print(PTRATIO_x_train.shape)
print(PTRATIO_y_train.shape)
print(PTRATIO_x_test.shape)
print(PTRATIO_y_test.shape)


# In[34]:


le.fit(PTRATIO_x_train,PTRATIO_y_train)

PTRATIO_y_pred=le.predict(PTRATIO_x_test)

r2_score(PTRATIO_y_test,PTRATIO_y_pred)


# In[35]:


plt.xlabel("PTRATIO")
plt.ylabel("MEDV")
plt.scatter(PTRATIO_x,PTRATIO_y,color="Red")
plt.plot(PTRATIO_x_test,PTRATIO_y_pred,color="Black")
plt.show()


# In[36]:


AGE_y=df[['MEDV']]
AGE_y


# In[37]:


AGE_x=df[['AGE']]
AGE_x


# In[38]:


AGE_x_train,AGE_x_test,AGE_y_train,AGE_y_test=train_test_split(AGE_x,AGE_y,
                                                                               test_size=0.2,random_state=2)

print(AGE_x_train.shape)
print(AGE_y_train.shape)
print(AGE_x_test.shape)
print(AGE_y_test.shape)


# In[39]:


le.fit(AGE_x_train,AGE_y_train)

AGE_y_pred=le.predict(AGE_x_test)

r2_score(AGE_y_test,AGE_y_pred)


# In[40]:


plt.xlabel("AGE")
plt.ylabel("MEDV")
plt.scatter(AGE_x,AGE_y,color="Red")
plt.plot(AGE_x_test,AGE_y_pred,color="Black")
plt.show()


# In[ ]:




