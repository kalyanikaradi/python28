#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DATAFRAME
#Pandas provides the DataFrame class, which allows you to create, manipulate, and analyze two-dimensional tabular data efficiently
import pandas as pd
d = pd.DataFrame()


# In[2]:


print(d)


# In[3]:


print(type(d))


# In[4]:


data=[['abc',1],['def',2],['ghi',3],['','hij'],['klm','a']]


# In[5]:


data


# In[7]:


d1=pd.DataFrame(data)
d1


# In[8]:


#df using dict
data={'name':['a','b','c','d','e','f'],'age':[45,32,67,88,90,10]}
d=pd.DataFrame(data)
d


# In[9]:


d.rename({'name':'candidate','age':'age_years'},axis=1,inplace=True)


# In[10]:


d


# In[11]:


data=[['Alex',10,'maths'],['bob',12,'Science'],['Kelly',15,'eco'],
     ['Boris',14,'geo'],['Ken',18,'English']]


# In[12]:


data


# In[13]:


data[2][0]


# In[14]:


data[3][2]


# In[15]:


#changing data
data[2][0]='ak'


# In[16]:


data


# In[17]:


import pandas as pd


# In[18]:


d= pd.DataFrame(data,columns=['name','age','subject'])
d


# In[20]:


d['name']


# In[22]:


d[['name','subject']]


# In[23]:


#iloc is index location
d.iloc[1,1]


# In[24]:


d.iloc[0,0]='ALEX'
d


# In[25]:


#adding col
d['Gender']='Male'
d


# In[26]:


d['age']=d['age']-1
#each age -1
d


# In[27]:


d.iloc[:,[0,1]]


# In[28]:


d.iloc[1:3,[0,1]]


# In[29]:


d.iloc[1]


# In[ ]:




