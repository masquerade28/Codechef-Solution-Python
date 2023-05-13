'''
  Chef appeared for a placement test.
  There is a problem worth X points. 
  Chef finds out that the problem has exactly 10 test cases. 
  It is known that each test case is worth the same number of points.
  Chef passes N test cases among them. 
  Determine the score Chef will get.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input X = Total Points Of The Problem ; N = Test Cases Chef Passed
  X,N = input().split()
  
  X,N = int(X),int(N)
  
  # Points Chef Got = Points Per Test Cases * Test Cases Attempted
  print(int(((X/10)*N)))
