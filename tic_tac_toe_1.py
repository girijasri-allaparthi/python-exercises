initial_choice='AA'
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