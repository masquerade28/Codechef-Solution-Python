'''
  Chef is playing Ludo. 
  According to the rules of Ludo, a player can enter a new token into the play only when he rolls a 6 on the die.
  In the current turn, Chef rolled the number X on the die. 
  Determine if Chef can enter a new token into the play in the current turn or not.
'''


# Running Loop For test Cases 
for t in range(int(input())):
  
  # Taking Input For The Number He Got On Dice
  X = int(input())
    
  # Checking If Chef Got 6
  Token = "YES" if X==6 else "NO"
    
  print(Token)
