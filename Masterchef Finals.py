'''
  Chef has been working hard to compete in MasterChef.
  He is ranked X out of all contestants. However, only 10 contestants would be selected for the finals.
  Check whether Chef made it to the top 10 or not ?
'''

# Runnig Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For Chef's Rank
  x = int(input())
  
  # Checking Whether Chef Made It To The Top 10 Or Not
  if (x <= 10):
    
    # If Yes Print "YES"
    print("YES")
    
  else:
    
    # If No Print "NO"
    print("NO")
