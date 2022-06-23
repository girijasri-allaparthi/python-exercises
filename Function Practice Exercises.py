#!/usr/bin/env python
# coding: utf-8

# #### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#     lesser_of_two_evens(2,4) --> 2
#     lesser_of_two_evens(2,5) --> 5

# In[1]:


def lesser_of_two_evens(num1,num2):
    if num1%2==0 and num2%2==0:
        if num1<num2:
            return num1
        else:
            return num2
    else:
        if num1>num2:
            return num1
        else:
            return num2
        
        


# In[7]:


lesser_of_two_evens(8,16)


# #### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#     animal_crackers('Levelheaded Llama') --> True
#     animal_crackers('Crazy Kangaroo') --> False
#         

# In[8]:


two_word_string=str(input("enter two word string"))

                    


# In[10]:


def animal_crackers(two_word_string):
    two_word_string=str(input("enter two word string"))
    word_list=two_word_string.split()
    if word_list[0][0]==word_list[1][0]:
        return True
    else:
        return False
            
   
        
                   

             


# In[14]:


animal_crackers(two_word_string)


# #### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
# 
#     makes_twenty(20,10) --> True
#     makes_twenty(12,8) --> True
#     makes_twenty(2,3) --> False

# In[3]:


a=int()
b=int()


# In[3]:


def makes_twenty(a,b):
   # a=int(input("enter number1:"))
   # b=int(input("enter number2:"))
    if a+b==20 or a==20 or b==20:
        return True
    else:
        return False
    


# In[4]:


makes_twenty(30,20)


# #### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#      
#     old_macdonald('macdonald') --> MacDonald
#     
# Note: `'macdonald'.capitalize()` returns `'Macdonald'`

# In[18]:


def old_macdonald(name):
    
    if len(name)>3:
        return name[:3].capitalize()+name[3:].capitalize()
    else:
        return "name is too short"
         
        
    


# In[26]:


old_macdonald("")


# #### MASTER YODA: Given a sentence, return a sentence with the words reversed
# 
#     master_yoda('I am home') --> 'home am I'
#     master_yoda('We are ready') --> 'ready are We'
#     
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
# 
#     >>> "--".join(['a','b','c'])
#     >>> 'a--b--c'
# 
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
# 
#     >>> " ".join(['Hello','world'])
#     >>> "Hello world"

# In[ ]:


def master_yoda(sentence):    
    words_sentence=sentence.split()
    words_sentence.reverse()
    sentence=' '.join(words_sentence)
    return(sentence)

test_sentence=int(input('write something'))

master_yoda(test_sentence)     
    


# #### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# 
#     almost_there(90) --> True
#     almost_there(104) --> True
#     almost_there(150) --> False
#     almost_there(209) --> True
#     
# NOTE: `abs(num)` returns the absolute value of a number

# In[17]:


def almost_there(n):
    if abs(100-n) <=10 or abs(200-n)<=10:
        return True
    else:
        return False
n=int(input("eneter number:"))
almost_there(n)


# #### FIND 33: 
# 
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# 
#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False

# In[88]:


def find_33(number_list):
    n=0
    first_three_position=False
    for num in number_list:
        n+=1
        if num==3 and not first_three_position:
            first_three_position=n
        if first_three_position:
            if num==3 and n!=first_three_position:
                print('Found '+'3')
            else:
                pass
                
        else:
            pass
        
    
    

        
               # return True
          #  else:
           #     return False
       # else:
       #     return False
            
            

            


# In[87]:


number_list=[1,3,6,4,7,3,3,3,3]

     
print(find_33(number_list)    )           
            
    


# In[43]:


3 in number_list
number_list[3:]


# In[52]:


def find_33(num_list):
    if 3 in num_list and 3 in num_list[(num_list.index(3)+1):]:
        return True
    else:
        return False
number_list=[1,3,6,4,7,8,9,10,11]
find_33(number_list)

