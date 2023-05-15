'''
  Chef's dog binary hears frequencies starting from 67 Hertz to 45000 Hertz (both inclusive).
  If Chef's commands have a frequency of X Hertz, find whether binary can hear them or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input X = Chef's Command Frequency
  X = int(input())
  
  # If Chef's Commands Have Frequency In Range Of [67,45000], Binay Can Hear Them
  # Else Binary Will Not Be Able To Hear Them
  Audible = "YES" if X>=67 and X<=45000 else "NO"
  
  print(Audible)
