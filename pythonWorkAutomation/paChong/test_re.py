#!/usr/bin/env python
# coding: utf-8

# In[8]:


import re


# In[19]:


str = 'abcaaabb'
result1 = re.findall('a.b', str)
result2 = re.findall('a?b', str)
result3 = re.findall('a*b', str)
result4 = re.findall('a.*b', str)
result5 = re.findall('a.*?b', str)


# In[20]:


print(result1)


# In[21]:


print(result2)


# In[22]:


print(result3)


# In[23]:


print(result4)


# In[24]:


print(result5)


# In[ ]:




