#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv("https://raw.githubusercontent.com/Mounika-Kajjam/Datasets/master/claimants.csv")
data.head()


# In[3]:


data.drop(['CASENUM'],axis=1,inplace=True)
data


# In[4]:


data.isnull().sum()


# In[5]:


def fill_na(col):
    col.fillna(col.value_counts().index[0],inplace=True)
    return col
data.apply(lambda col:fill_na(col))


# In[6]:


data.isnull().sum()


# In[7]:


X = data.iloc[:,1:]
X.head()


# In[8]:


y=data.ATTORNEY
y.head()


# In[9]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=2)


# In[10]:


# Training Data
from  sklearn.linear_model import LogisticRegression
reg=LogisticRegression()
reg.fit(X_train,y_train)


# In[11]:


y_train_pred = reg.predict(X_train)
y_train_pred


# In[12]:


from sklearn.metrics import confusion_matrix,accuracy_score
conf = confusion_matrix(y_train,y_train_pred)
conf


# In[13]:


sns.heatmap(confusion_matrix(y_train,y_train_pred),annot=True,fmt='3.0f',annot_kws={'size':'20'})


# In[14]:


# Testing Data
from  sklearn.linear_model import LogisticRegression
reg=LogisticRegression()
reg.fit(X_test,y_test)


# In[15]:


y_test_pred = reg.predict(X_test)
y_test_pred


# In[16]:


from sklearn.metrics import confusion_matrix,accuracy_score
conf = confusion_matrix(y_test,y_test_pred)
conf


# In[17]:


sns.heatmap(confusion_matrix(y_test,y_test_pred),annot=True,fmt='3.0f',annot_kws={'size':'20'})


# In[18]:


from sklearn.metrics import classification_report
# Syntax: classification_report(actualValues,predictedValues)
print(classification_report(y_train,y_train_pred))
print(classification_report(y_test,y_test_pred))


# In[19]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Scaling for training data
scaled_X_train = pd.DataFrame(scaler.fit_transform(X_train),columns=X_train.columns)
scaled_X_train


# In[20]:


scaled_X_test = pd.DataFrame(scaler.fit_transform(X_test),columns=X_test.columns)
scaled_X_test


# In[21]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
scores =[]
for k in range(1,20):
    knn_model = KNeighborsClassifier(n_neighbors=k)#,metric='euclidean')
    knn_model.fit(scaled_X_train,y_train)
    pred_test = knn_model.predict(scaled_X_test)
    scores.append(accuracy_score(y_test,pred_test))
scores


# In[22]:


plt.plot(range(1,20),scores,marker='o',markerfacecolor='r',linestyle='--')


# In[23]:


final_model = KNeighborsClassifier(n_neighbors=7,metric='euclidean')
final_model.fit(scaled_X_train,y_train)


# In[24]:


final_train_pred = final_model.predict(scaled_X_train)
final_train_pred


# In[25]:


from sklearn.metrics import confusion_matrix
sns.heatmap(confusion_matrix(y_train,final_train_pred),annot=True,fmt='d')


# In[27]:


print(classification_report(y_train,final_train_pred))


# In[28]:


# Prediction on Test Data
final_test_pred = final_model.predict(scaled_X_test) #y_test
final_test_pred


# In[29]:


sns.heatmap(confusion_matrix(y_test,final_test_pred),annot=True,fmt='d')


# In[30]:


print(classification_report(y_test,final_test_pred))


# In[31]:


y_test_prob=final_model.predict_proba(scaled_X_test)
y_test_prob=pd.DataFrame(y_test_prob)
y_test_prob


# In[32]:


# Logistic Regression
y_test_prob1=reg.predict_proba(X_test)
y_test_prob1=pd.DataFrame(y_test_prob1)
y_test_prob1


# In[33]:


y_test


# In[34]:


from sklearn.metrics import roc_auc_score,roc_curve
m_prob = final_model.predict_proba(scaled_X_test)[:,1]
#m_prob
fpr,tpr,threshold = roc_curve(y_test,m_prob,pos_label=1)
print(fpr)
print(tpr)
print(threshold)
print(pd.DataFrame(threshold))


# In[35]:


# Logistic Regression
m_prob1 = reg.predict_proba(scaled_X_test)[:,1]
fpr1,tpr1,threshold1 = roc_curve(y_test,m_prob1,pos_label=1)


# In[36]:


plt.plot(fpr,tpr)


# In[37]:


# Logistic Regression
plt.plot(fpr1,tpr1)


# In[38]:


roc_auc_score(y_test,m_prob)


# In[39]:


# Logistic Regression 
roc_auc_score(y_test,m_prob1)


# In[ ]:




