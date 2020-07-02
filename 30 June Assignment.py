#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv("https://raw.githubusercontent.com/Mounika-Kajjam/Datasets/master/wbcd.csv")
data


# In[3]:


data.isnull().sum()


# In[4]:


# Descriptive statistics of the dataset
data1=data.drop(columns=['id'])
data1.describe()


# In[5]:


# Histogram
data1.hist(figsize=(20,20))


# In[6]:


# Boxplot
for i in data1.select_dtypes(include=['int64','float64']).columns:
    sns.boxplot(data1[i])
    plt.show()


# In[7]:



# Find the correlation in the data and visualize it 
data1.corr()


# In[8]:


plt.figure(figsize=(20,20))
sns.heatmap(data1.corr(),annot=True,cmap='YlGnBu')


# In[9]:


# Visualize the frequency of the output categories
data['diagnosis'].value_counts()


# In[10]:


data['diagnosis'].value_counts().plot(kind='bar')


# In[11]:


# Apply the KNN Algorithm to the dataset without applying scaling operation and try to compare the 
# results before scaling and after scaling.
X = data.drop(['id','diagnosis'],axis=1)
X.head()


# In[12]:


y = data.diagnosis
y.head()


# In[13]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.30,random_state=2)


# In[14]:


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[15]:


# With Sacling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Scaling for training data
scaled_X_train = pd.DataFrame(scaler.fit_transform(X_train),columns=X_train.columns)
scaled_X_train


# In[16]:


# Scaling for testing data
# Testing the data based on training data
scaled_X_test = pd.DataFrame(scaler.fit_transform(X_test),columns=X_test.columns)
scaled_X_test


# In[17]:


# Model Building
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=6,metric='euclidean')
#knn = KNeighborsClassifier(n_neighbors=25,metric='euclidean')
#knn = KNeighborsClassifier(n_neighbors=40,metric='euclidean')
# Apply the knn object on the dataset
# Syntax: objectName.fit(Input,Output)
knn.fit(scaled_X_train,y_train)


# In[18]:


# Without Scaling
knn1 = KNeighborsClassifier(n_neighbors=6,metric='euclidean')
knn1.fit(X_train,y_train)


# In[19]:


# Predictions on the data
#predict function--> gives the predicted values
# Syntax:objectname.predict(Input)
y_train_pred = knn.predict(scaled_X_train)
y_train_pred


# In[20]:


#Without Scaling
y_train_pred1 = knn1.predict(X_train)
y_train_pred1


# In[21]:


from sklearn.metrics import classification_report
print(classification_report(y_train,y_train_pred))


# In[22]:


# Without Scaling
from sklearn.metrics import classification_report
print(classification_report(y_train,y_train_pred1))


# In[23]:


# Checking for optimum k-value
# Build the models with multiple k values
from sklearn.metrics import accuracy_score
scores =[]
for k in range(1,20):
    knn_model = KNeighborsClassifier(n_neighbors=k)#,metric='euclidean')
    knn_model.fit(scaled_X_train,y_train)
    pred_test = knn_model.predict(scaled_X_test)
    scores.append(accuracy_score(y_test,pred_test))
scores


# In[24]:


# Without Scaling
from sklearn.metrics import accuracy_score
scores1 =[]
for k in range(1,20):
    knn_model1 = KNeighborsClassifier(n_neighbors=k)#,metric='euclidean')
    knn_model1.fit(X_train,y_train)
    pred_test1 = knn_model1.predict(X_test)
    scores1.append(accuracy_score(y_test,pred_test1))
scores1


# In[25]:



# Plot of K values and Scores
plt.plot(range(1,20),scores,marker='o',markerfacecolor='r',linestyle='--')


# In[26]:


#Without Scaling
plt.plot(range(1,20),scores1,marker='o',markerfacecolor='r',linestyle='--')


# In[27]:


# Optimum k value is 7
final_model = KNeighborsClassifier(n_neighbors=7,metric='euclidean')
final_model.fit(scaled_X_train,y_train)


# In[28]:


# Without Scaling
final_model1 = KNeighborsClassifier(n_neighbors=9,metric='euclidean')
final_model1.fit(X_train,y_train)


# In[29]:


# Prediction on training data
final_train_pred = final_model.predict(scaled_X_train)
final_train_pred


# In[30]:


#Without Scaling
final_train_pred1 = final_model1.predict(X_train)
final_train_pred1


# In[31]:


from sklearn.metrics import confusion_matrix
sns.heatmap(confusion_matrix(y_train,final_train_pred),annot=True,fmt='d')


# In[32]:


#Without Scaling
from sklearn.metrics import confusion_matrix
sns.heatmap(confusion_matrix(y_train,final_train_pred1),annot=True,fmt='d')


# In[33]:


# classification report
# Precision--> PPV --> Out of the positive predicted values,how many truely positive
print(classification_report(y_train,final_train_pred))


# In[34]:


# Without Scaling
print(classification_report(y_train,final_train_pred1))


# In[35]:


# Prediction on Test Data
final_test_pred = final_model.predict(scaled_X_test) #y_test
final_test_pred


# In[36]:


final_test_pred1 = final_model1.predict(X_test) #y_test
final_test_pred1


# In[37]:


# Compare actual values of test data(y_test) and final_test_pred(model predicted values)
#Confusion_matrix(actualValues,predictedValues)
sns.heatmap(confusion_matrix(y_test,final_test_pred),annot=True,fmt='d')


# In[38]:


# Without Scaling
sns.heatmap(confusion_matrix(y_test,final_test_pred1),annot=True,fmt='d')


# In[39]:


print(classification_report(y_test,final_test_pred))


# In[40]:


#Without Scaling
print(classification_report(y_test,final_test_pred1))


# In[ ]:




