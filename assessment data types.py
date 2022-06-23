#!/usr/bin/env python
# coding: utf-8

# # numbers: integers (.....-2,-1,0,1,2....), floating point 0.12,0.13
# strings : 'abbwjhhd',"jasdhj asahs"
# lists [1,'asdd',1.268]
# tuples (1,2,3)
# dictionaries {'key':value1,'key1':value2}
# 
# 

# In[15]:


(1e1*10)+(1/(5-1))


# 44,29,34

# In[17]:


4 * (6 + 5)


# In[18]:


4 * 6 + 5 


# In[19]:


4 + 6 * 5 


# 8.5 float

# In[24]:


2**6


# In[27]:


49**0.5


# In[28]:


s='hello'
s[1]


# In[32]:


s[::-1]


# In[33]:


s[-1]


# In[34]:


s[4]


# In[39]:


my_list=[0,0,0]
my_list


# In[40]:


my_list[3*0]
my_list


# In[42]:


list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
list3


# In[46]:


list4 = [5,3,4,6,1]
list4.sort()
list4


# In[47]:


d = {'simple_key':'hello'}
d['simple_key']


# In[49]:


d = {'k1':{'k2':'hello'}}
d['k1']['k2']


# In[59]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d['k1'][0]['nest_key'][1][0]


# In[67]:


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2][0]


# dictionaries are as per key values.can not be sorted

# lists are mutable but tuples are immutable
# tuple can be created by ()

# sets can not have duplicate values.

# In[68]:


list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)


# False,False,False,True,False

# In[69]:


2 > 3


# In[70]:


3 <= 2


# In[71]:


3 == 2.0


# In[72]:


3.0 == 3


# In[73]:


4**0.5 != 2


# Flase

# In[74]:


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']


# # completed the assesement
