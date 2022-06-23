#!/usr/bin/env python
# coding: utf-8

# c-1.13 write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are
# listed in the opposite order than they were before,and compare this method to an equivalent python function for doing the 
# same thing.

# In[58]:


list1=[1,2,3,4]
list1.reverse()
list1


# In[ ]:


def rev_fun(list1):
    l=len(list1)
    list2=[]
    for n in list1:
        n=list1[l-1]
        list2.append(n)
        l-=1
    return list2    


# In[15]:


rev_fun(range(1,11))


# In[17]:


list1=[1,2,3,4]


# def rev_fun(list1):
#     l=len(list1)
#     list2=[]
#     while l>0:
#         list2.append(list1[l-1])
#         l-=1
#     return list2
# rev_fun([1,2,3,4])

# In[32]:


def rev_fun(list1):
    list2=list1[::-1]
    return list2

rev_fun([8,7,5,3,2,6,1,9])


# 1.14 Write a short python function that takes a sequence of integer values and determines if there is a distinct 
# pair of numbrs in the sequence whose product is odd

# In[90]:


def prod_odd(list1):
    m=0
    for n in list1:
        m+=1
        if n&1==1 and m<len(list1):
            if list1[m]&1==1:
                return True
            else:
                pass
        else:
            pass
    return False


# In[96]:


list1=[1,2,3,4,5,6,7,10]
prod_odd(list1)


# In[1]:


def prod_odd(list1):
    n=0
    l=len(list1)
    while n<(l-1):
       # print(list1[n])
       # print(list1[n+1])
        prod=list1[n]*list1[n+1]
        
        if prod%2==1:
            
            print(f'{list1[n]} and {list1[n+1]} product is odd')
            
        n+=1
                  
prod_odd([1,2,3,5,6,7,5,5,6])                  
                        


# 1.15 Write a python function that takes a sequence of numbers and determines if all the numbers are different from
# each other(that is they are distinct)

# In[59]:


def distinct_fun(list1):
    l=len(list1)
    m=1
    for n in list1:
        if n in list1[m:]:
            print("numbers are not distinct")
            print(n)
            return False
                    
        else:
            pass
        m+=1
        
    return True    
            
            
          
    
     
            
          
            
            
    
    


# In[69]:


def distinct_fun(list1):
    
   # list1=[1,2,3,4,4,6,2,1]
    set(list1)
    if len(set(list1))==len(list1):
        return True
    else:
        return False
    
list1=range(1,111)
    
distinct_fun(list1)


# In[42]:


distinct_fun([1,2,4,7,9,10])


# 1.18 Demonstrate how to use python's list comprehension syntax to produce the list[0,2,6,12,20,30,42,56,72,90]

# In[50]:


[n*(n-1)for n in range(1,11)]
   # n=n*(n-1)
   # print(n)


# 1.19 Demonstrate how to use Python's list comprehension syntax to produce the list ['a','b','c'.......'z'],but without
# typing all 26 such characters literally

# In[53]:


import string
[string.ascii_lowercase[n] for n in range(0,26)]


# In[54]:


string.ascii_uppercase


# In[76]:


[chr(n) for n in range(97,97+26)]


# In[ ]:





# 1.16 scale function , the body of the loop executes the command data[j]*=factor.We have discussed that numeric types are immutable and the use of the *= operator in this context causes the creation of a new instance(not the mutation of an existing instance).How is still possible,then that our implimentation of scale changes the actual parameter sent by the caller?

# In[130]:


def scale(data,factor):
    for j in range(len(data)):
        data[j]*=factor
    return data
       
        
scale([1,2,3,4],2)        
        


# 1.17 Had we implemented the scale function as follows , does it work properly?
# 

# In[131]:


def scale(data,factor):
    for val in data:
        val*=factor
        print(val) 
    return data 

scale([1,2,3,4],2)


# In[175]:


def my_shuffle(data):
    data2=[]
    l=(len(data))
  #  element=0
    
    for n in range(l):
        data2[n]=data[random.randint(0,l-1)]
        while data2[n] in data2[:n]:
            data2[n]=data[random.randint(0,l-1)]
            print(data2[n])
        
        
    return data2

my_shuffle([1,2,3,4])
            
        


# 1.20 Python's random module includes a function shuffle(data) that accepts a list of elements and randomly reorders 
# so that each possible order occures with equal probability.the random module includes a more basic function randint(a,b)
# that returns a uniformly random integer from a to b (including both end points).Using only the randint function,implement your own version of the shuffle function.

# In[170]:


def my_shuffle(data):
    
    data2=[]
    l=len(data)-1
    element=0
    
    for n in range(len(data)):
        element=data[random.randint(0,l)]
      #  print( element)
        while element in data2[:n]:
            element=data[random.randint(0,l)]
     #       print(element)
        data2.append(element)  
     #   print(data2)
            
    return data2

my_shuffle(['a','b','c',1,2,5,7,8])
            


# 1.21 Write a Python program that repeatedly reads lines from standard input until an EOFError is raised,and then outputs those lines
# reverse order(a user can indicate end of input by typing ctrl-D)
