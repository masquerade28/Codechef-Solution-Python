'''
  There are three friends and a total of N candies.
  There will be a fight amongst the friends if all of them do not get the same number of candies.
  Chef wants to divide all the candies such that there is no fight. Find whether such distribution is possible.
'''

# Taking Number of Test Cases and Looping
for i in range(int(input())):
  
  # Taking Input For Number of Candies
  n = int(input())
    
  # Checking If Can Be Distributed Into 3
  if n % 3 == 0:
    
    print("YES")
    
  else:
    
    print("NO")
