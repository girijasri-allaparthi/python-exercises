{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be0905e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "Player 1 enter your choiceR1C2\n",
      "   C1|C2|C3\n",
      "R1|AA|X|AA\n",
      "R2|AA|AA|AA\n",
      "R3|AA|AA|AA\n",
      "True\n",
      "Player 2 enter your choiceR1C3\n",
      "   C1|C2|C3\n",
      "R1|AA|X|O\n",
      "R2|AA|AA|AA\n",
      "R3|AA|AA|AA\n",
      "True\n",
      "Player 1 enter your choiceR1C1\n",
      "   C1|C2|C3\n",
      "R1|X|X|O\n",
      "R2|AA|AA|AA\n",
      "R3|AA|AA|AA\n",
      "True\n",
      "Player 2 enter your choiceR1C1\n",
      "Choice already taken.Retry\n",
      "True\n",
      "Player 2 enter your choiceR2C1\n",
      "   C1|C2|C3\n",
      "R1|X|X|O\n",
      "R2|O|AA|AA\n",
      "R3|AA|AA|AA\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "initial_choice='AA'\n",
    "choice_list=[]\n",
    "game_is_on=True\n",
    "players_choice={1:'X',2:'O'}\n",
    "dict_tic_tac={'R1': {'C1': initial_choice, 'C2': initial_choice, 'C3': initial_choice},\n",
    "          'R2': {'C1': initial_choice, 'C2': initial_choice, 'C3': initial_choice},'R3': {'C1': initial_choice, 'C2': initial_choice, 'C3': initial_choice}}\n",
    "choice_all=['R1C1','R1C2','R1C3','R2C1','R2C2','R2C3','R3C1','R3C2','R3C3']\n",
    "choice_threshold=len(dict_tic_tac.keys())**2\n",
    "choice_count=1\n",
    "def print_boxes():\n",
    "    print ('   C1|C2|C3')\n",
    "    for key  in dict_tic_tac.keys():\n",
    "           print(key+'|'+'|'.join(list(dict_tic_tac[key].values())))\n",
    "\n",
    "choice_is_ok=True\n",
    "            \n",
    "while game_is_on:\n",
    "        \n",
    "        if choice_count>choice_threshold:\n",
    "            games_is_on=False\n",
    "        for player in players_choice.keys():\n",
    "            choice_is_ok=True\n",
    "            while choice_is_ok: \n",
    "                \n",
    "                print(choice_is_ok)\n",
    "                choice=input('Player '+str(player)+' enter your choice')          \n",
    "\n",
    "                if choice not in choice_all:\n",
    "                    print('incorrect choice.Retry')\n",
    "                    \n",
    "                    choice_is_ok=True\n",
    "                elif choice in choice_list:\n",
    "                    print('Choice already taken.Retry')\n",
    "                    \n",
    "                    choice_is_ok=True\n",
    "                elif choice in choice_all:\n",
    "                    dict_tic_tac[choice[:2]][choice[-2:]]=players_choice[player]\n",
    "                    choice_list.append(choice)                    \n",
    "                    print_boxes()\n",
    "                    choice_is_ok=False\n",
    "                    choice_count=choice_count+1\n",
    "               \n",
    "                    \n",
    "    \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "010d6057",
   "metadata": {},
   "outputs": [],
   "source": [
    "choice_all=['R1C1','R1C2','R1C3','R2C1','R2C2','R2C3','R3C1','R3C2','R3C3']\n",
    "if 'R1C2'"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
