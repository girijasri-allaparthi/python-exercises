#!/usr/bin/env python
# coding: utf-8

# In[52]:


r1={'1':"| |",'2':'| |','3':'| |'}
r2={'4':'| |','5':'| |','6':'| |'}
r3={'7':'| |','8':'| |','9':'| |'}


# In[40]:


print(r1)
print(r2)
print(r3)


# In[58]:


list_r=[r1,r2,r2]
print(r1)
print(r2)
print(r3)


# In[44]:


print(r1.values()[0])

print(r2.values())
print(r3.values())


# In[33]:


print(f'({r1.values[0]},{r1.values[1]},{r1.values[2]})')


# In[21]:


r1['1']


# In[34]:


print(r1.values())


# In[36]:


r1['1']='X'


# In[37]:


r1


# In[ ]:


initial_choice='  '
choice_list=[]
game_is_on=True
players_choice={1:'X',2:'O'}
dict_tic_tac={'R1': {'C1': initial_choice, 'C2': initial_choice, 'C3': initial_choice},
          'R2': {'C1': initial_choice, 'C2': initial_choice, 'C3': initial_choice},'R3': {'C1': initial_choice, 'C2': initial_choice, 'C3': initial_choice}}
choice_threshold=len(dict_tic_tac.keys())**2
choice_count=1
def print_boxes():
    print ('   C1|C2|C3')
    for key  in dict_tic_tac.keys():
           print(key+'|'+'|'.join(list(dict_tic_tac[key].values())))

choice_is_ok=True
            
while game_is_on:
        if choice_count==choice_threshold:
            games_is_on=False
        for player in players_choice.keys():
            print(str(player))
            while choice_is_ok:
                choice=input('Player '+str(player)+' enter your choice for '+str(choice_count))
                try:
                    dict_tic_tac[choice[:2]][choice[-2:]]=players_choice[player]
                except Exception as e:
                    print(str(e))
                    choice_is_ok=True
                finally:
                    choice_is_ok=False
                    choice_list.append(choice)
                    choice_count=choice_count+1
                    print_boxes()
                    print('in while still')

        
        


# In[ ]:





# In[9]:


initial_choice='  '
dict_tic_tac={'R1': {'C1': initial_choice, 'C2': initial_choice, 'C3': initial_choice},
          'R2': {'C1': initial_choice, 'C2': initial_choice, 'C3': initial_choice},'R3': {'C1': initial_choice, 'C2': initial_choice, 'C3': initial_choice}}
print(len(dict_tic_tac.keys())**2)

