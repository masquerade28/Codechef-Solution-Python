'''
  Chef's son wants to go on a roller coaster ride. 
  The height of Chef's son is X inches while the minimum height required to go on the ride is H inches. 
  Determine whether he can go on the ride or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Chef's Son Height ; H = Minimum Height Required For The Ride
  X,H = map(int, input().split())
  
  # Chef's Son Can Go On The Ride If His Height ≥ The Minimum Required Height.
  RollerCoaster = "YES" if X>=H else "NO"
  
  print(RollerCoaster)
