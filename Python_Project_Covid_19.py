#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('C:/Users/nahid/OneDrive/Documents/DataAnalystProject/covid_19_data.csv')


# In[4]:


df.head()


# In[6]:


df.drop(['SNo','Last Update'], axis = 1, inplace= True)


# In[7]:


df


# In[14]:


df = df.rename(columns = {'ObservationDate':'Date', 'Province/State':'Province', 'Country/Region':'Country'})


# In[15]:


df.head()


# In[17]:


df.describe()


# In[18]:


df.info()


# In[57]:


df['Date'] = pd.to_datetime(df['Date'])


# In[58]:


df.drop(['Date'],axis=1, inplace=True)


# In[59]:


df = df.fillna('NA')


# In[60]:


df.info()


# In[61]:


df


# In[36]:


df2 = df.groupby('Country')[['Country','Confirmed','Deaths','Recovered']].sum().reset_index()
# to get the total number of deaths, recovered, and confirmed in each country


# In[37]:


df2


# In[77]:


df2 = df2.astype({'Confirmed':'int64', 'Deaths':'int64','Recovered':'int64'})


# ## 

# In[78]:


df2


# In[83]:


df2 = df.groupby(['Country','date'])[['Country','date','Confirmed','Deaths','Recovered']].sum().reset_index()
# get the total per day, per country


# In[80]:


df2


# In[81]:


df2 = df2.rename(columns={'date': 'Date'})


# In[82]:


# get all the record with more than 100 confirmed
df3 = df2[df2['Confirmed'] > 100]


# In[75]:


df3


# In[76]:


df2


# In[84]:


df2.info()


# In[85]:


df2 = df2.astype({'Confirmed':'int64', 'Deaths':'int64','Recovered':'int64'})


# In[86]:


df2


# In[87]:


df3 = df2[df2['Confirmed'] > 100]


# In[88]:


df3


# In[93]:


df3.head(20)


# In[94]:


# total of countries
countries = df3['Country'].unique()
len(countries)


# ## What is the trend of Deaths, Confirmed, and Recovered per country as the date move on

# In[96]:


for idx in range(0, len(countries)):
    C = df3[df3['Country'] == countries[idx]].reset_index()
    plt.plot(np.arange(0, len(C)), C['Confirmed'], color = 'blue', label = 'Confirmed')
    plt.plot(np.arange(0, len(C)), C['Recovered'], color = 'green', label = 'Recovered')
    plt.plot(np.arange(0, len(C)), C['Deaths'], color = 'red', label = ' Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since begining pandemic')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()


# In[100]:


# The trend for all over the world
df4 = df3.groupby(['Date'])[['Date', 'Confirmed','Recovered', 'Deaths']].sum().reset_index()


# In[101]:


C = df4
plt.plot(np.arange(0, len(C)), C['Confirmed'], color = 'blue', label = 'Confirmed')
plt.plot(np.arange(0, len(C)), C['Recovered'], color = 'green', label = 'Recovered')
plt.plot(np.arange(0, len(C)), C['Deaths'], color = 'red', label = ' Deaths')
plt.title('World')
plt.xlabel('Days since begining pandemic')
plt.ylabel('Number of cases')
plt.legend()
plt.show()


# In[ ]:




