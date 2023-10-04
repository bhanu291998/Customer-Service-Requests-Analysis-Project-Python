#!/usr/bin/env python
# coding: utf-8

# # Project Customer Service Requests Analysis

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
### import libraries
import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns   


# In[3]:


service311 = pd.read_csv ('311_Service_Requests_from_2010_to_Present.csv')


# In[4]:


service311.head()


# In[5]:


service311.shape


# In[6]:


service311.columns


# In[8]:


service311['Complaint Type'].unique()


# In[10]:


service311['Descriptor'].unique()


# In[11]:


complaintTypecity = pd.DataFrame({'count':
                                  service311.groupby(['Complaint Type','City']).size()}).reset_index()
complaintTypecity


# In[12]:


service311.groupby(['Borough','Complaint Type','Descriptor']).size()


# In[ ]:





# In[9]:


import datetime


# In[13]:


df = pd.read_csv("311_Service_Requests_from_2010_to_Present.csv", parse_dates=["Created Date", "Closed Date"])


# In[14]:


df["Request_Closing_Time"] = df["Closed Date"] - df["Created Date"]


# In[22]:


#Have a look at the status of tickets
df['Status'].value_counts().plot(kind='bar',alpha=0.6,figsize=(7,7))
plt.show()


# In[20]:


#Complaint type Breakdown with bar plot to figure out majority of complaint types and top 10 complaints
service311['Complaint Type'].value_counts().head(10).plot(kind='barh',figsize=(5,5));


# In[21]:


service311.groupby(["Borough","Complaint Type","Descriptor"]).size()


# In[23]:


majorcomplints=service311.dropna(subset=["Complaint Type"])
majorcomplints=service311.groupby("Complaint Type")

sortedComplaintType = majorcomplints.size().sort_values(ascending = False)
sortedComplaintType = sortedComplaintType.to_frame('count').reset_index()

sortedComplaintType
sortedComplaintType.head(10)


# In[25]:


sortedComplaintType = sortedComplaintType.head()
plt.figure(figsize=(5,5))
plt.pie(sortedComplaintType['count'],labels=sortedComplaintType["Complaint Type"], autopct="%1.1f%%")
plt.show()


# In[26]:


#Group dataset by complaint type to display plot against city
groupedby_complainttype = df.groupby('Complaint Type')


# In[26]:


grp_data = groupedby_complainttype.get_group('Blocked Driveway')
grp_data.shape


# In[27]:


#To get nan values in the entire dataset
df.isnull().sum()


# In[29]:


#fix blank values in City column
df['City'].dropna(inplace=True)


# In[31]:


#Shape after dropping nan values
df['City'].shape


# In[32]:


#count of null values in grouped city column data
grp_data['City'].isnull().sum()


# In[33]:


#fix those NAN with "unknown city" value instead
grp_data['City'].fillna('Unknown City', inplace =True)


# In[35]:


#Scatter plot displaying all the cities that raised complaint of type 'Blocked Driveway'
plt.figure(figsize=(20, 15))
plt.scatter(grp_data['Complaint Type'],grp_data['City'])
plt.title('Plot showing list of cities that raised complaint of type Blocked Driveway')
plt.show()


# In[ ]:




