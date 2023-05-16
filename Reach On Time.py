'''
  Chef has recently moved into an apartment. 
  It takes 30 minutes for Chef to reach office from the apartment.
  Chef left for the office X minutes before Chef was supposed to reach. 
  Determine whether or not Chef will be able to reach on time.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input
  X = int(input())
  
  # If X>=30 Chef Will Reach On Time Else He Will Get Late
  OnTime = "YES" if X>=30 else "NO"
  
  print(OnTime)
