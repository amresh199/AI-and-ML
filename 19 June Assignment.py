#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data=pd.read_csv("https://raw.githubusercontent.com/Mounika-Kajjam/Datasets/master/company_sales_data.csv")
data


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


lines = data.plot(x='month_number',y='total_profit',label ='Profit data month wise',color='r',marker='o',linewidth=3,linestyle='--')
lines


# In[8]:


line1=data.plot(x='month_number',y=['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer'],marker='o',linewidth=3,linestyle='--',)
line1


# In[9]:


line2=data.plot(x='month_number',y='toothpaste',kind='scatter')
line2


# In[11]:


line3=data.plot(x='month_number',y=['facecream','facewash'],kind='bar',figsize=(6,6))
line3


# In[12]:


f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(data['month_number'], data['bathingsoap'], label = 'Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
axarr[0].set_title('Sales data of  a Bathingsoap')
axarr[1].plot(data['month_number'], data['facewash'], label = 'Face Wash Sales Data', color='r', marker='o', linewidth=3)
axarr[1].set_title('Sales data of  a facewash')
plt.xlabel('Month Number')
plt.show()


# In[13]:


plt.hist(data['total_profit'],[150000,200000,250000,300000,350000,400000,450000])


# In[ ]:




