#!/usr/bin/env python
# coding: utf-8

# # Statements Assessment Test

# In[34]:


st = 'Print only the words that start with s in this sentence' 
st.split()
for word in st.split():
    if word[0]=='s':
        print (word)
       
        
         
    


# **Use range() to print all the even numbers from 0 to 10.**

# In[42]:


for num in range(0,10):
    if num%2==0:
            print (num)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[43]:


[x for x in range(0,51) if x%3==0]


# In[37]:


list(range(0,11,2))


# In[66]:


st = 'Print every word in this sentence that has an even number of letters'

[word for word in st.split() if len(word)%2==0]


# In[45]:


st = 'Print every word in this sentence that has an even number of letters'
st.split()
for word in st.split():
    if len(word)%2==0:
        print(word)


# **Go through the string below and if the length of a word is even print "even!"**

# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[62]:


for num in range(1,101):
    if num%3==0 and num%5==0:
        print ("FizzBuzz")
    elif num%5==0:
        print("Buzz")
    elif num%3==0:
        print("Fuzz")
        
    else:
        print(num)


# Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[61]:


st = 'Create a list of the first letters of every word in this string'
st.split()
for word in st.split():
    print (word[0])


# In[64]:


[word[0] for word in st.split()]


# In[ ]:




