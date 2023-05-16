'''
  King loves to go on tours with his friends.
  King has N cars that can seat 5 people each and M cars that can seat 7 people each. 
  Determine the maximum number of people that can travel together in these cars.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For Number Of 5 Seater Cars And Number Of & Seater Cars
  N,M = map(int, input().split())
  
  # Maximum Number Of People That Can Travel Together = (No. Of 5 Seater Cars * 5) + (No. Of 7 Seater Cars * 7)
  print((N*5)+(M*7))
