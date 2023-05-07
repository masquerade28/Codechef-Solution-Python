'''
  The task is very simple: given two integers A and B, write a program to add these two numbers and output it.
'''

# Running Loop For Test Cases 
for t in range(int(input())):
  
  # Taking Input As String And Splitting It
  A,B = input().split()
  
  # Converting String Into Integer
  A,B = int(A),int(B)
  
  # Printing Sum
  print(A+B)
