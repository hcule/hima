#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
get_ipython().magic(u'matplotlib inline')
import datetime as dt


# In[83]:


s_data = pd.read_csv('region wise data.csv')


# In[84]:


s_data.head(2)


# In[85]:


style.use('ggplot')
plt.plot(s_data['Region'],s_data['total_deaths'],'y', label = 'Date with Region wise Data', linewidth =1.5)
plt.xlabel('Region')
plt.ylabel('Total Deaths')


# In[90]:


fig, ax= plt.subplots()
plt.scatter(s_data['total_cases'],s_data['date'])
plt.title('Month Wise total Death Scatter Map')


# In[91]:


new_data = s_data.groupby('Region')
s_Europe = new_data.get_group('Europe')
s_asia = new_data.get_group('Asia')
s_Africa = new_data.get_group('Africa')
s_South_America = new_data.get_group('South America')
plt.plot(s_asia['total_cases'],s_asia['total_deaths'], 'r' , label = 'Asia')
plt.plot(s_Europe['total_cases'],s_Europe['total_deaths'], '' , label = 'Europe')
plt.plot(s_Africa['total_cases'],s_Africa['total_deaths'], 'b' , label = 'Africa')
plt.plot(s_South_America['total_cases'],s_South_America['total_deaths'], 'p' , label = 'South America')


# In[102]:


fig, ax = plt.subplots(2,2)
ax[0,0].plot(s_asia['total_cases'],s_asia['total_deaths'])
ax[0,0].set_title('Asia')
ax[0,1].plot(s_Europe['total_cases'],s_Europe['total_deaths'])
ax[0,1].set_title('Europe')
ax[1,0].plot(s_Africa['total_cases'],s_Africa['total_deaths'])
ax[1,0].set_title('Africa')
ax[1,1].plot(s_South_America['total_cases'],s_South_America['total_deaths'])
ax[1,1].set_title('South America')
for ax in ax.flat:
    ax.set(xlabel='Total Cases',ylabel='Total Death')


# In[100]:


s_data.tail(10)


# In[107]:


fig, ax = plt.subplots(2,2)
ax[0,0].plot(s_asia['total_cases'],s_asia['total_deaths'])
ax[0,0].set_title('Asia')
ax[0,1].plot(s_Europe['total_cases'],s_Europe['total_deaths'])
ax[0,1].set_title('Europe')
ax[1,0].plot(s_Africa['total_cases'],s_Africa['total_deaths'])
ax[1,0].set_title('Africa')
ax[1,1].plot(s_South_America['total_cases'],s_South_America['total_deaths'])
ax[1,1].set_title('South America')
for ax in ax.flat:
    ax.set(xlabel='Total Cases',ylabel='Total Death')


# In[111]:


plt.bar(s_asia['total_deaths'],s_asia['total_cases'], width = 6.25)
plt.xlabel('total_deaths')
plt.ylabel('Total Cases')
plt.title('COVID-19 Total Cases vs Total Death in Asis')


# In[ ]:




