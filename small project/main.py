import random
from colorama import Fore , Style , init
init(autoreset=True)
'''
1 for ROCK 
-1 for PAPER
0 for SISSOR
'''
youDict = {"ROCK":1, "PAPER":-1,"SISSOR":0}
reverseDict = {1:"ROCK",-1:"PAPER",0:"SISSOR"}
while True:
    youstr = input("\nEnter your choice (ROCK / PAPER / SCISSOR) or press Q to quit: ").upper()
    if youstr == "Q":
        print("Game Over. Thanks for playing! 👋")
        break
    computer = random.choice([-1,0,1])
    you = youDict[youstr]

    print (Fore.GREEN+f"YOU CHOICE {reverseDict[you]}\n COMPUTER CHOICE {reverseDict[computer]}")

    if (computer == you ):
     print( Fore.YELLOW+"IT A DRAW")
    else:
     if computer == 1 and you == -1 :
       print(Fore.BLUE+"YOU WIN")
     elif computer == 1 and you == 0:
       print (Fore.MAGENTA+"YOU LOSE")
     elif computer == -1 and you == 1:
       print(Fore.MAGENTA+"YOU LOSE")
     elif computer == -1 and you == 0:
       print(Fore.BLUE+"YOU WIN")
     elif computer == 0 and you == -1:
       print (Fore.MAGENTA+"YOU LOSE")
     elif computer == 0 and you == 1:
       print (Fore.BLUE+"YOU WIN ")
     else : 
       print("SOMTHING WRONG")


