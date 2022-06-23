#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def count_primes(num_100):
    n=0
    m=0
    factors_list=[]
    prime_list=[]
    for num in num_100:
        factors_list=[]
        m=0
        #print(n,m,num)
        
       
            
        while m<=n:         
                #print(n,m,num)
            if num%(num_100[m])==0:
                factors_list.append(num_100[m])
                print(factors_list)
            
                #print(prime_list)
                m=m+1
        if len(factors_list)<=2:
                prime_list.append(num)
        n+=1       
            
    print(prime_list)
    print(len(prime_list))

num_100=range(1,101)
count_primes(num_100)
        


# In[ ]:





# In[ ]:





# In[ ]:




