#!/usr/bin/env python
# coding: utf-8

# # TICTACTOE GAME

# # displaying board function

# In[11]:


def board_ttt(list_1):
    
    l=len(list_1)
  #  print(f'length of the string {l}')
    n=1
    r=1
    rows=int(l**0.5)
  #  print(f'number of rows {rows}')
    columns=int(l**0.5)
  #  print(f'number of columns {columns}')
    while r<=rows:
        m=1
        while m<=columns:
            print(list_1[n-1], end='|  ')
            m+=1
            n+=1 
        r+=1
        print('\n-----------')
  #  print(f'r value{r}')
        
            
        
        
        
                


# # players choice display function

# In[12]:


def player_choice(player1,player2,player_1,player_2):
     
     #choice list and choice initializing
    
    choice_list=['X','O']
    player1='n'
    player2='n'
    choice='n'
  
    if player_1:
        
     # looping until the valid choice is enetered
        while choice.upper() not in choice_list:
            choice=str(input("enter your choice X or O :"))
            if choice.upper() not in choice_list:
                print("enter valid choice")
            
        player1= choice.upper()
    
        print(f'player_1 choice {player1}')
        
        if choice.upper()==choice_list[0]:
            
            player2=choice_list[1]
            
            print(f'player_2 is {player2}')
        else:
            player2=choice_list[0]
            print(f'player_2 is {player2}')
              
    else:
        while choice.upper() not in choice_list:
            choice=str(input("enter your choice X or O :"))
            if choice.upper() not in choice_list:
                print("enter valid choice")
        player2=choice.upper()
        
        print(f'player_2 choice {player2}')
        if choice.upper()==choice_list[0]:
            
            player1=choice_list[1]
            
            print(f'player_1 is {player1}')
        else:
            player1=choice_list[0]
            print(f'player_1 is {player1}')
                  
    return player1,player2          


# # Game win function

# In[13]:


def game_win(player,list_1):
      
    if (list_1[0]==list_1[3]==list_1[6])or               (list_1[1]==list_1[4]==list_1[7])or               (list_1[0]==list_1[1]==list_1[2])or               (list_1[3]==list_1[4]==list_1[5])or               (list_1[6]==list_1[7]==list_1[8])or               (list_1[2]==list_1[5]==list_1[8])or               (list_1[0]==list_1[4]==list_1[8])or               (list_1[2]==list_1[4]==list_1[6]):
        
        
        
        print(f'{player} won:game over')
        game_on=False 
  
    else:
        game_on=True
    return game_on
        
                
    


# # player toss

# In[4]:


def toss_player():
    player_1=False
    player_2=False
    import random
    r=random.randint(1,2)
    if r==1:
        print("player 1 won the toss")
        player_1=True
    else:
        player_2=True
        print("player 2 won the toss")
    return player_1,player_2


# # do you want to play again ??

# In[14]:


def play_again(playagain):
    
    
    playagain_list=['Y','N'] 
    playagain='s'   
     # looping until the valid choice is enetered
    print("would you like to play again")    
    while playagain.upper() not in playagain_list:
        playagain=str(input("enter your choice y or n :"))
        if playagain.upper() not in playagain_list:
            print("enter valid choice")
            
   
    if playagain.upper()=='Y':
        game_on=True
    else:
        game_on=False
    return game_on   
   


# # game on function

# In[ ]:


from IPython.display import clear_output
def ttt_game():
    list_1=[1,2,3,4,5,6,7,8,9]      
    x=set(list_1)
    list_2=[]
    num_flag=False
    
    player_1,player_2=toss_player()
 
 #   player_1=True
 #   player_2=False
    game_on=True
    player1='n'
    player2='n'
  # player1,player2=player_choice(player_1,player_2)
    player1,player2=player_choice(player1,player2,player_1,player_2)
    
    
    
    
    while game_on==True:
        
        while num_flag==False:
            
            board_ttt(list_1)
            
            try: 
                num=int(input("enter the number:"))
            except ValueError:
                print("Only provide numbers from the board")
                num=999
            finally:
            
                if num in list_1:
                    if num in list_2:
                        print("the number is already chosen")
                    num_flag=True       
                elif num not in list_1:
                    print("please choose the number from the board")
                elif num is str:
                    print("choose the number from the board")
        
        clear_output()
      
        if player_1==True:
            player=player1
            list_1[num-1]=player
            list_2.append(num)
            print(list_2)
            game_on=game_win(player,list_1)
            print(f'gameon {game_on}')
             ###################################################
    ###checking if the players want to play again###################
    
    
            if game_on==False:
                playagain='s'
                
              #  play_again(playagain)
                game_on=play_again(playagain)
                print(f'gameon {game_on}')
                list_1=[1,2,3,4,5,6,7,8,9]
      ###################################################################      
                           
                
            player_1=False
            print(f'player1 {player_1}')
            player_2=True
            print(f'player2 {player_2}')
            
        else:
            player=player2
            list_1[num-1]=player
            list_2.append(num)
            print(list_2)
            game_on=game_win(player,list_1)
            print(f'gameon {game_on}')
      ###################################################
    ###checking if the players want to play again###################
    
    
            if game_on==False:
                playagain='s'
                #play_again(playagain)
                game_on=play_again(playagain)
                print(f'gameon{game_on}')
                list_1=[1,2,3,4,5,6,7,8,9]
      ###################################################################            
            player_2=False
            print(f'player2 {player_2}')
            player_1=True
            print(f'player1 {player_1}')
            
    
        
         
        num_flag=False
        print(f'num_flag {num_flag}') 
        
        
        print(set(list_1))
        
        
        if  set(list_1)=={'X','O'}:
            game_on=False
            print(f'gameon {game_on}')
            
            playagain='s'
            game_on=play_again(playagain)
            print(f'gameon {game_on}')
            list_1=[1,2,3,4,5,6,7,8,9]
  
        
        
    


# In[20]:


ttt_game()


# 
# 
# 
# 
# 
# 
# 
# 
