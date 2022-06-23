#!/usr/bin/env python
# coding: utf-8

# # Functions and Methods Homework 
# 
# Complete the following questions:
# ____
# **Write a function that computes the volume of a sphere given its radius.**
# <p>The volume of a sphere is given as $$\frac{4}{3} πr^3$$</p>

# In[11]:


def vol_sphere(r):
   # r=int(input("enter radius:"))
    return (4/3)*(22/7)*(r**3)
    
vol_sphere(2)


# Write a function that checks whether a number is in a given range (inclusive of high and low)

# In[30]:


def ran_check(num,low,high):
    
   # return num in range(low,high)
    
    if num in range(low,high):
        
        print(num)
     
        print(f'{num} is in the range between {low} ,{high}')
          
    else:
        print(f'{num} is  not in the range between {low} ,{high}')      
          
    
ran_check(7,4,7)
    


# ____
# **Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**
# 
#     Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#     Expected Output : 
#     No. of Upper case characters : 4
#     No. of Lower case Characters : 33
# 
# HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**
# 
# If you feel ambitious, explore the Collections module to solve this problem!

# In[37]:


#str.isupper('A')
'A'.isupper()


# In[44]:


def uppr_lowr(str):
    
    uppr=[]
    lowr=[]
    for letter in str:
        
        if letter.isupper():
            uppr.append(letter)
        if letter.islower():
            lowr.append(letter)            
    print(f'number of upper case characters:{len(uppr)}')
    print(f'number of upper case characters:{len(lowr)}')
    
uppr_lowr('Hello Mr. Rogers, how are you this fine Tuesday?')
            
          
       


# **Write a Python function that takes a list and returns a new list with unique elements of the first list.**
# [1,1,1,1,2,2,3,3,3,3,4,5]
#     Sample List : 
#     Unique List : [1, 2, 3, 4, 5]

# In[2]:


def uniq_list(element_list):
    
    return list(set(element_list))

#element_list=list(input("enter element list"))

uniq_list([1,1,1,1,2,2,3,3,3,3,4,5])


# **Write a Python function to multiply all the numbers in a list.**
# 
#     Sample List : [1, 2, 3, -4]
#     Expected Output : -24

# In[6]:


def mult_num(nums_list):
    mult=1
    for num in nums_list:
         mult=mult*num
    return mult
mult_num([1,2,3,-4,7,8])
        
     


# ____
# **Write a Python function that checks whether a word or phrase is palindrome or not.**
# 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

# In[35]:


def palindrome(words):
           
   #if ' ' in words:
        
    words= ''.join(words.split())
            
    return words[::]==words[::-1]

    
    
            
        
    
palindrome('madam')
        


# In[8]:


word='madam'
word[1:]


# In[9]:


word[::]


# In[10]:


word[::-1]


# In[11]:


word='girija'


# In[12]:


word[::]


# In[13]:


word[::-1]


# ____
# #### Hard:
# 
# **Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)**
# 
#     Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#     For example : "The quick brown fox jumps over the lazy dog"
# 
# Hint: You may want to use .replace() method to get rid of spaces.
# 
# Hint: Look at the [string module](https://stackoverflow.com/questions/16060899/alphabet-range-in-python)
# 
# Hint: In case you want to use [set comparisons](https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41)

# In[70]:


['a','b','c','d']==['a','c','b','d']


# In[124]:


def pangram(word_string):
    #alphabet_set={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    alphabet=string.ascii_lowercase
    alphabet_set=set(alphabet)
    word_string=word_string.replace(' ','')
  #  word_string=word_string.replace(',','')
    # return word_string
    s=set(word_string.lower())
    return s==alphabet_set
    
     
pangram('The quick brown fox jumps over the lazy dog')


# In[50]:


{1,2,3,4}=={4,2,3,1}


# In[71]:


import string


# In[72]:


string.ascii_lowercase


# In[78]:


import random


# In[79]:


random


# In[99]:


random.choice('a,b')


# In[100]:


random.randrange


# In[119]:


random.randrange(10,16)


# In[121]:


x=range('a','z')
for i in x:
    print(x)


# In[ ]:




