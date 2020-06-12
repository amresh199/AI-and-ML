#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Question
import pandas as pd
s1=pd.Series([2,4,6,8,10])
s2=pd.Series([1,3,5,7,9])
print(list(s1),'+',list(s2),'=',list(s1+s2))
print(list(s1),'-',list(s2),'=',list(s1-s2))
print(list(s1),'*',list(s2),'=',list(s1*s2))
print(list(s1),'/',list(s2),'=',list(s1/s2))


# In[2]:


#2 Question
s1=pd.Series([12.23,23.34,45.3,45.5,67.4,67.78,34.45,23.34,67.4,23])
print(s1)
s1d=s1.describe()
print("Minimum, 25th percentile, median, 75th, and maximum of a given series:")
s2=pd.Series([s1d["min"],s1d["25%"],s1d["50%"],s1d["75%"],s1d["max"]])
print(list(s2))


# In[3]:


#3 Question
sr1=pd.Series([1,2,3,4,5])
sr2=pd.Series([2,4,6,8,10])
print(sr1)
print(sr2)
print("\nItems of sr1 not present in sr2:\n")
print(sr1[~sr1.isin(sr2)])


# In[4]:


#4 Question
s1=pd.Series(['Red','Green','Orange','Pink','Yellow','White'])
print("\nOriginal Series\n")
print(s1)
print("\nFiltered words\n")
print(s1[s1.str.count('a')+s1.str.count('e')+s1.str.count('i')+s1.str.count('o')+s1.str.count('u')+s1.str.count('A')+s1.str.count('E')+s1.str.count('I')+s1.str.count('O')+s1.str.count('U')>=2])


# In[5]:


#5 Question
dict1 = {'a':'Anastasia','b':'Dima','c':'Katherine','d':'James','e':'Emily',
         'f':'Michael','g':'Matthew','h':'Laura','i':'Kevin','j':'Jonas'}
dict2 = {'a':12.5,'b':9.0,'c':16.5,'d':'NaN','e':9.0,'f':20.0,'g':14.5,'h':'NaN','i':8.0,
         'j':19.0}
dict3 = {'a':1,'b':3,'c':2,'d':3,'e':2,'f':3,'g':1,'h':1,'i':2,
         'j':1}
dict4={'a':'yes','b':'no','c':'yes','d':'no','e':'no','f':'yes','g':'yes','h':'no','i':'no',
         'j':'yes'}
data={"name":dict1,"score":dict2,"attempts":dict3,"qualify":dict4}
df=pd.DataFrame(data)
print("\nOriginal Data\n")
print(df)
print("\nData where number of attempts in examination is greater than 2\n")
print(df[df['attempts']>2])


# In[ ]:




