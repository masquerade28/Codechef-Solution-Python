'''
  There is a cricket match going on between two teams A and B.
  Team B is batting second and got a target of X runs. 
  Currently, team B has scored Y runs. 
  Determine how many more runs Team B should score to win the match.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For The Target They Have To Chase (X) And Their Current Score (Y) 
  X,Y = map(int, input().split())
  
  # Runs Remaining = Target - Current Runs
  print(X-Y)
