# The game function in a program lets a user play 
# a game  and return the score as an integerr. 
# you need to read file 'hi-score.txt' 
# which is either blank or contain the previous hi-score .
#  you need to write a program to update the hi- 
# score whenever the game() function break the hi-score

import random
def game():
   print("you are playing the game")
   score = random.randint(1,100)
  #   fetch the hiscore
   with open("hiscore.txt") as f :
    hiscore = f.read()
    if hiscore !='':   
       hiscore = int(hiscore)
    else:
        hiscore= 0
   print(f"your score is {score}")
   if score>hiscore:
      print("congratulation you have just broken the hiscore")
      with open("hiscore.txt","w") as f:
         f.write(str(score))
   return score 

game( )
