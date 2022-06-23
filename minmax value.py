#!/usr/bin/env python
# coding: utf-8

# In[40]:


my_list=[1,2,3,4,5]
my_list


# In[ ]:


l=len(my_list)
n=0
m=1
while n<=(l-1):
      if my_list[n]>my_list[m]:
        max_data=my_list[n]
        m=m+1
        


# In[ ]:


len(my_list)


# In[ ]:


my_list=[1,3,5,7,9,10,11]
my_list


# In[ ]:


'asasj'


# In[ ]:


p='amas'
p


# In[57]:


def get_maximum(inumlist):
    my_list=inumlist
    l=len(my_list)
    n=0
    max_data=my_list[n]
    while n<l-1:
          if max_data<my_list[n+1]:
            max_data=my_list[n+1]
          n=n+1
    print(max_data)
    
#my_list=[10555555555555555555555555550,200444444444440,303333333333333333333330,45111155555,168,12313123]
inputval=input('please enter some list with numbers')
my_list=list(map(int,inputval.split(',')))
get_maximum(my_list)
            

            


# In[55]:


a='100,101,102,103'
b=list(map(int,a.split(',')))
print(b)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




