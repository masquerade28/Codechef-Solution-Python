'''
  Apple considers any iPhone with a battery health of 80 % or above, to be in optimal condition. 
  Given that your iPhone has X % battery health, find whether it is in optimal condition.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Battery Health
  X = int(input())
  
  # If Battery Health Is 80 % Or Above It Is In Optimal Condition
  BatteryHealth = "YES" if (X >= 80) else "NO"
  
  print(BatteryHealth)
