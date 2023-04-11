#This is a simple console Rock,Paper,Scissor Game with a Computer.
import random
import os
import time
print("<<<<--Welcome to a simple ROCK PAPER SCISSOR GAME-->>>>")
# Play the sound
choices = ['rock','paper','scissor']
name = input("Enter the your name: ")
play = True
result_tie = False
while play:
    print("************ROCK PAPER SCISSOR *******************")
    player_choice = random.choice(choices)
    CPU_choice = random.choice(choices)
    if player_choice == CPU_choice:
        print("Tie! Playing Again........!")
        time.sleep(3)
        result_tie = True
    elif player_choice == 'rock' and CPU_choice == 'scissor':
        print("Computer:{0}\n{1}:{2}\nYou Win !! Hurray!".format(CPU_choice,name,player_choice))
    elif player_choice=='scissor' and CPU_choice == 'paper':
        print("Computer:{0}\n{1}:{2}\nYou Win !! Hurray!".format(CPU_choice,name,player_choice))
    elif player_choice == 'paper'and CPU_choice == 'rock':
        print("Computer:{0}\n{1}:{2}\nYou Win !! Hurray!".format(CPU_choice,name,player_choice))
    elif CPU_choice == 'rock' and player_choice == 'scissor':
            print("Computer:{0}\n{1}:{2}\nCPU Win !! Sad trumpets!".format(CPU_choice,name,player_choice))
    elif CPU_choice=='scissor' and player_choice == 'paper':
            print("Computer:{0}\n{1}:{2}\nCPU Win !! Sad trumpets!".format(CPU_choice,name,player_choice))
    elif CPU_choice == 'paper'and player_choice == 'rock':
            print("Computer:{0}\n{1}:{2}\nCPU Win !! Sad trumpets!".format(CPU_choice,name,player_choice))
    else:
          print("Nobody Won.Somthing Went Wrong!!!")

    if result_tie:
        result_tie = False
        continue;
        
    else:
        try:
            status = input("Do you want to continue playing?(Y/N)")
            if(status.upper() == 'Y'):
                play = True
                
            else:
                play = False
        except:
            print("Something Went Wrong.")
    
    os.system('cls')