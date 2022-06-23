{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "15764f11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "Player 1 enter your choice for 1R1C1\n",
      "   C1|C2|C3\n",
      "R1|X|AA|AA\n",
      "R2|AA|AA|AA\n",
      "R3|AA|AA|AA\n",
      "True\n",
      "Player 2 enter your choice for 1R1C1\n",
      "Choice already taken.Retry\n",
      "True\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [5]\u001b[0m, in \u001b[0;36m<cell line: 17>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m choice_is_ok:         \n\u001b[0;32m     24\u001b[0m     \u001b[38;5;28mprint\u001b[39m(choice_is_ok)\n\u001b[1;32m---> 25\u001b[0m     choice\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mPlayer \u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mplayer\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m enter your choice for \u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mchoice_count\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m            \n\u001b[0;32m     27\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m choice \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m choice_all:\n\u001b[0;32m     28\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mincorrect choice.Retry\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py:1075\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1071\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_allow_stdin:\n\u001b[0;32m   1072\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(\n\u001b[0;32m   1073\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1074\u001b[0m     )\n\u001b[1;32m-> 1075\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_input_request\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   1076\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mprompt\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1077\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_parent_ident\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1078\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_parent\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1079\u001b[0m \u001b[43m    \u001b[49m\u001b[43mpassword\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\n\u001b[0;32m   1080\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py:1120\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1117\u001b[0m             \u001b[38;5;28;01mbreak\u001b[39;00m\n\u001b[0;32m   1118\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[0;32m   1119\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[1;32m-> 1120\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28mNone\u001b[39m\n\u001b[0;32m   1121\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1122\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
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
    "choice_count=0\n",
    "def print_boxes():\n",
    "    print ('   C1|C2|C3')\n",
    "    for key  in dict_tic_tac.keys():\n",
    "           print(key+'|'+'|'.join(list(dict_tic_tac[key].values())))\n",
    "\n",
    "choice_is_ok=True\n",
    "            \n",
    "while game_is_on:\n",
    "        choice_count=choice_count+1\n",
    "        if choice_count>choice_threshold:\n",
    "            games_is_on=False\n",
    "        for player in players_choice.keys():\n",
    "            choice_is_ok=True\n",
    "            while choice_is_ok:         \n",
    "                print(choice_is_ok)\n",
    "                choice=input('Player '+str(player)+' enter your choice for '+str(choice_count))            \n",
    "\n",
    "                if choice not in choice_all:\n",
    "                    print('incorrect choice.Retry')\n",
    "                    choice_count=choice_count-1\n",
    "                    choice_is_ok=True\n",
    "                elif choice in choice_list:\n",
    "                    print('Choice already taken.Retry')\n",
    "                    choice_count=choice_count-1\n",
    "                    choice_is_ok=True\n",
    "                elif choice in choice_all:\n",
    "                    dict_tic_tac[choice[:2]][choice[-2:]]=players_choice[player]\n",
    "                    choice_list.append(choice)                    \n",
    "                    print_boxes()\n",
    "                    choice_is_ok=False\n",
    "               \n",
    "                    \n",
    "    \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bdf80f82",
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
