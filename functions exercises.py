#!/usr/bin/env python
# coding: utf-8

# In[13]:


def find_33(number_list):
    n=0
    
    for num in number_list:
        n+=1
        if n<len(number_list):
            if num==number_list[n]==3:
                return True
            else:
                pass
        else:
            return False        
        
        
number_list=[3,0,3,4,7,3,0,0,3,5,6,3,3]
find_33(number_list)              
            

            


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'

# In[40]:


def paper_doll(inp_str):
    str=''
    for letter in inp_str:
       # letter=letter*3
        str+=letter*3
   # print(str)
    return str        
          
            
            
        
            
            
            
        

    
    
#inp_str=("girija")
paper_doll('deepak')


# ##### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#     blackjack(5,6,7) --> 18
#     blackjack(9,9,9) --> 'BUST'
#     blackjack(9,9,11) --> 19

# In[ ]:


def black_jack(a,b,c):
    sum=a+b+c
    
    if sum<=21:
        return sum
    else: 
        if 11 in (a,b,c):
            sum-=10
            if sum<=21:
                return sum
            else:
                return "BUST"

a=int(input("eneter num1:"))


b=int(input("eneter num2:"))

c=int(input("eneter num3:"))
black_jack(a,b,c)   


# In[57]:


black_jack(9,11,11)


# # #### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#  
#     summer_69([1, 3, 5]) --> 9
#     summer_69([4, 5, 6, 7, 8, 9]) --> 9
#     summer_69([2, 1, 6, 9, 11]) --> 14

# In[33]:


def summer_69(list_num):
    n=0
    sum_num=0
    sum1_num=0
    for num in list_num:
        n+=1
        sum_num+=num
        
        if num==6:
            if 9 in list_num[n:]:
                m=list_num.index(9)
                sum1_num=sum(list_num[(n-1):(m+1)])
                 # print("hi")
                
                
    return sum_num-sum1_num          
            
            
    


# In[41]:


summer_69([4, 5, 6, 2,3,4,5,6,9, 0, 10])


# #### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# 
#      spy_game([1,2,4,0,0,7,5]) --> True
#      spy_game([1,0,2,4,0,5,7]) --> True
#      spy_game([1,7,2,0,4,5,0]) --> False

# In[46]:


def spy_game(int_list):
    
    n=0
    for num in int_list:
        n+=1
        if num==0:
            if 0 in int_list[n:]:
                m=int_list.index(0)
                if 7 in int_list[m:]:
                    return True
                
    return False
int_list=[1,7,2,0,4,5,0]
spy_game(int_list)
                


# #### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
#     count_primes(100) --> 25
# 
# By convention, 0 and 1 are not prime.

# In[7]:


def count_primes(num_100):
    n=0
    m=0
    factors_list=[]
    for num in num_100:
        n+=1 
        
    
        while m<n:
            if num%(num_100)[m]==0:
            factors_list.append()=num_100[m]
            m+=1
            if len(factors_list)=2:
                
        else:
            break
        if len(list_num)=2:
             print(num)
num_100=range(1,101)
count_primes(num_100)
        


# In[16]:


def count_primes(num_100):
    n=0
    m=0
    
    prime_list=[]
    for num in num_100:
        factors_list=[]   
        m=0
        while m<n:
            
            if num%(num_100[m])==0:
                factors_list.append(num_100[m])
                #print(factors_list)
            m+=1
        
        if len(factors_list)<=2:
            prime_list.append(num)
            #print(prime_list)
                  
        n+=1       
            
    print(prime_list)

num_100=range(1,101)
count_primes(num_100)
        


# In[ ]:


def count_primes(num_100):
    n=0
    m=0
    factors_list=[]
    prime_list=[]
    for num in num_100:
        n+=1 
        m=1
        print(n,m,num_100[m])
        while m<=num: 
            print(n,m,num_100[m])
            if num%(num_100[m])==0:
                factors_list.append(num_100[m])
                print(factors_list)
                m=m+1
                if len(factors_list)>1:
                    prime_list.append(num)
                    print(prime_list)
                  
                
            
    print(prime_list)

num_100=range(1,101)
count_primes(num_100)
        

