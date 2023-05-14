'''
  The working hours of Chef’s kitchen are from X pm to Y pm (1 ≤ X < Y ≤ 12).
  Find the number of hours Chef works.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input In Integer Form
  X,Y = map(int, input().split())
  
  # Hours Chef Work = End Time - Start Time
  print(Y-X)
