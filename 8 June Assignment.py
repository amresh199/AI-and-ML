#!/usr/bin/env python
# coding: utf-8

# In[5]:


#answer 1 ---> Pivot table

import pandas as pd 
import numpy as np
df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
df


# In[6]:


#answer 1

table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum)
table


# In[7]:


#answer 1

table = pd.pivot_table(df, values='D', index=['A', 'B'],
                    columns=['C'], aggfunc=np.sum, fill_value=0)
table


# In[8]:


#answer 1

table = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
                    aggfunc={'D': np.mean,
                             'E': [min, max, np.mean]})
table


# In[9]:


#answer 1

table = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
                    aggfunc={'D': np.mean,
                             'E': [min, max, np.mean]})
table


# In[10]:


#answer 2 ---> To store a pandas DataFrame as csv file

import pandas as pd
df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar"],
                  	       "B": ["one", "one", "one", "two", "two", "one", "one", "two", "two"],
                   	        "C": ["small", "large", "large", "small","small", "large", "small", "small","large"],
                               "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                               "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
df


# In[11]:


#answer 2

df.to_csv('csvfile.csv')


# In[12]:


#answer 3

IPL_2018 = pd.DataFrame({'IPL Team': ['CSK', 'SRH', 'KKR', 'RR', 'MI', 'RCB', 'KXIP', 'DD'],
                         'Matches Played': [16, 17, 16, 15, 14, 14, 14, 14],
                         'Matches Won': [11, 10, 9, 7, 6, 6, 6, 5]}
                       )
IPL_2018.set_index('IPL Team', inplace = True)
IPL_2018


# In[13]:



#answer 3

IPL_2017 = pd.DataFrame({'IPL Team': ['MI', 'RPS', 'KKR', 'SRH', 'KXIP', 'DD', 'GL', 'RCB'],
                         'Matches Played': [17, 16, 16, 15, 14, 14, 14, 14],
                         'Matches Won': [12, 10, 9, 8, 7, 6, 4, 3]}
                       )
IPL_2017.set_index('IPL Team', inplace = True)
IPL_2017


# In[14]:


#answer 3 ---> 1) 

Total = IPL_2018 + IPL_2017
Total


# In[15]:


#answer 3 ---> 1)

Total = IPL_2018.add(IPL_2017,fill_value=0)
Total


# In[16]:


#answer 3 ---> 2)

win_percentage = Total["Matches Won"]/Total["Matches Played"]
Total["win_percentage"]=win_percentage
Total


# In[17]:


#answer 3 ---> 3)

Total.sort_values(by=['Matches Won', 'win_percentage'],ascending=False)


# In[ ]:




