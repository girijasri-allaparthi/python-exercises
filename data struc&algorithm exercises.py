#!/usr/bin/env python
# coding: utf-8

# # R 1.4 -

# write a short python function that takes a positive integer n and returns the sum of the squares of all the positive integers 
# smaller than n.

# In[5]:


def sum_squares(num):
    
    sum=0
    while num>0:
        sum+=num**2
        print(num**2)
        print(sum)
        
        num-=1
    return sum

num=int(input("enter number:"))
sum_squares(num)
        


# 1.5 Give a single command that computes the sum from above exercise relying on pythons's comprehension syntax and the built-in 
# sum function.
# 

# In[5]:


sum(num**2 for num in range(1,5))
    
    


# 1.7 Give a single command that computes the sum of squares of odd positive integers smaller than the given number, relying on pythons's comprehension syntax and the built-in sum function.
# 

# In[12]:


sum(num**2 for num in range(1,8,2))
    


# 1.6 write a short python function that takes a positive integer n and returns the sum of the squares of all odd the positive integers smaller than n.

# In[11]:


def sumodd_squares(num):
    sum=0
    if num%2==0:
        n=num-1
        while n>=1:
            sum=sum+n**2
            
            n=n-2
        return sum    
    else:
        n=num-2
        while n>=1:
            sum=sum+n**2
            
        return sum

num=int(input("enter number:"))
sumodd_squares(num)
        


# 1.8 Python allows negative integers to be used as indeces into a sequence, such as a string .If string s has length n , and
# expression s[k] is used for index -n<=k<0,what is the equivalent index j>=0 such that s[j] references the same element?
# 

# 0<=j<n

# 1.9 what parameters should be sent to the range constructor ,to produce range with values 50,60,70,80?

# In[16]:


list(range(50,81,10))


# 1.10 what parameters should be sent to the range constructor,to produce a range with values 8,6,4,2,0,-2,-4,-6,-8?

# In[18]:


list(range(8,-9,-2))


# 1.11 demonstrate how to use python's list comprehension syntax to produce the list [1,2,4,8,16,32,64,128,256]

# def list_num(num):
#     num_list=[1]
#     i=1
#     while num>1:
#         i=i*2
#         num_list.append(i)
#       #  print(num_list)
#       #  print(i)
#         num-=1   
#     return num_list
# list_num(9)

# In[1]:


in_list=range(0,9)
[2**i for i in in_list]


# In[51]:


import math
def sumodd_squares(num):
    num_of_odds=math.floor((num+1)/2)
    result=(num_of_odds*(4*num_of_odds**2-1))/3
    return result
num=int(input("enter number:"))
sumodd_squares(num)
        


# In[49]:


import math
math.floor(4.5)
num_of_odds=4
4*(4*16-1)/3


# In[2]:


s='Deepak'
s[-1]
len(s)
    


# In[86]:


import random


# 1.12 Python's random module includes a function choice(data) that returns a random element from a non-empty sequence.The 
# random module includes a more basic function randrange,with parameterization similar to the built-in range function
# from the given range.Using only the randrange function,implement your own version of the choice function.

# In[135]:


def my_choice(inlist):
  #  print("enter the range:")
  #  m=int(input("first number:"))
  #  n=int(input("second num :"))
  #  instr=input("enter the input:")
    l=len(inlist)
    
    return inlist[random.randrange(0,l)]
    


# In[149]:


inlist=['a','d','v',5,6,7,8]
my_choice(inlist)


# In[ ]:


m=2
n=6
random.randrange(m,n)


# In[7]:


help()


# In[44]:


random.randrange(1,11)


# In[70]:


random.choice(chr(97))


# In[116]:


random.choice(range(1,10))


# In[156]:


def scale(data,factor):
    for j in range(len(data)):
        data[j]*=factor
    return data
       
        
scale([1,2,3,4],2)        
        


# In[161]:


def scale(data,factor):
    for val in data:
        val*=factor
        print(val) 
    return data 

scale([1,2,3,4],2)

