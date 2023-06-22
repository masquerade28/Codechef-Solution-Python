'''
  A blood drive aims to collect N number of blood donations.
  The drive has collected X donations so far. 
  Find the remaining number of donations needed to reach the target.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Number Of Collected Donations ; Y = Number Of Required Donations
  N,X = map(int, input().split())
  
  # If Number Of Required Donations > Number Of Collected Donations, Then Number Of Donations Needed = N-X else 0
  DonationDrive = N-X if N>X else 0
  
  # Displaying Result
  print(DonationDrive)
