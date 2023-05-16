'''
  Alice and Bob were having an argument about which of them is taller than the other. 
  Charlie got irritated by the argument, and decided to settle the matter once and for all.
  Charlie measured the heights of Alice and Bob, and got to know that Alice's height is X centimeters and Bob's height is Y centimeters. 
  Help Charlie decide who is taller.
  It is guaranteed that X ≠ Y.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For Alice And Bob's Height
  A,B = map(int, input().split())
  
  # If Alice Is Taller It Will Return A Else B
  Taller = 'A' if A>B else 'B'
  
  print(Taller)
