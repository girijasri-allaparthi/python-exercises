#!/usr/bin/env python
# coding: utf-8

# ### Just for fun, not a real problem :)
# 
# #### PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#     print_big('a')
#     
#     out:   *  
#           * *
#          *****
#          *   *
#          *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns. <br>For purposes of this exercise, it's ok if your dictionary stops at "E".

# In[32]:


def print_big(letter):
    patterns_dict={1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    letter_dict={'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    patterns_dict[letter_dict['A'][0]]

    for pattern in letter_dict[letter.upper()]:
        print (patterns_dict[pattern])
    
    
    
letter=str(input("enter a letter:"))
print_big(letter)


# #### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
#     count_primes(100) --> 25
# 
# By convention, 0 and 1 are not prime.

# In[2]:


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
           


# In[3]:


num=int(input("enter number:"))
count_primes(num)


# In[13]:


import timeit
def min_max(data):
    l=len(data)
  #  print(l)
    max_data=data[0]
    min_data=max_data
   # print(max_data)
    n=1
    while n<l:
        if data[n]>max_data:
            max_data=data[n]
        if data[n]<min_data:
            min_data=data[n]
          #  print(max_data)
        n+=1
            
             
    return (max_data,min_data)
                    
    
            
            
            
data=[2,3,10,20,21,14,80,99,1,10]
min_max(data)
    


# In[12]:


data=[2,3,10,20,21,14,80,99,1,10]
data.sort()
x=(data[0],data[len(data)-1])
print(x)


# In[ ]:





# In[ ]:




