#!/usr/bin/env python
# coding: utf-8

# # Guessing Game Challenge

# The Challenge:
# 
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# 
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
#  * within 10 of the number, return "WARM!"
#  * further than 10 away from the number, return "COLD!"
# 3. On all subsequent turns, if a guess is 
#  * closer to the number than the previous guess return "WARMER!"
#  * farther from the number than the previous guess, return "COLDER!"
# 4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!
# 

# In[37]:


from random import randint
random_num=randint(1,100)
print(random_num)
player_name=[input("enter name:")]
guess_num_lst=[]         
guess='F'
while  guess=='F':
    guess_num=int(input("enter number:"))
    guess_num_lst.append(guess_num)
    l=len(guess_num_lst)
    if random_num==guess_num:
        print ("guess is correct")
        print (f"num_of_guesses {l}")
        print (guess_num_lst)
        guess = 'T'
    elif 1<=guess_num<=100:   
                   
         
        if l==1 :
            if abs(random_num-guess_num)<10:
                print("warm")
            else:
                
                print("cold")
        
                                 
        else: 
                                  
            if abs(random_num-guess_num_lst[-1])<abs(random_num-guess_num_lst[-2]):
                print("warmer")
                        
            else:                     
                print('colder')                
                      
                             
    else:
         
        print ("out of Bounds")

         

    
        
            


# 

# In[26]:


d={}
d['deepak']='deepak'


# In[28]:


d['girija']='girija'


# In[32]:


d['attempt']=1
d

