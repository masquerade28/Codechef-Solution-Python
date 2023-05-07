'''
  Chef wants to appear in a competitive exam. To take the exam, there are following requirements:
    1] Minimum age limit is X (i.e. Age should be greater than or equal to X).
    2] Age should be strictly less than Y.
  Chef's current Age is A. Find whether he is currently eligible to take the exam or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input As String
  X,Y,A = input().split()
  
  # Converting Input Into String
  X,Y,A = int(X),int(Y),int(A)
  
  # If Chef Is Eligible Print Yes 
  if (A >= X AND A < Y):
    print("YES")
    
  # If Chef Is Not Eligible Print No
  else :
    print("NO")
