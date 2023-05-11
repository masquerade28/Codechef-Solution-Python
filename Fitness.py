'''
  Chef wants to become fit for which he decided to walk to the office and return home by walking. 
  It is known that Chef's office is X km away from his home.
  If his office is open on 5 days in a week, find the number of kilometers Chef travels through office trips in a week.
'''

# Running Loop For Test cases
for t in range(int(input())):
  
  # Taking Input For The Distance
  X = int(input())
  
  # Total Km Chef Walks = 5 Days * 2 Time Travelling * Distance
  print(10*X)
