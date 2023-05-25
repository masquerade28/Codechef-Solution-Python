'''
  In a classic chase, Tom is running after Jerry as Jerry has eaten Tom's favourite food.
  Jerry is running at a speed of X metres per second while Tom is chasing him at a speed of Y metres per second. 
  Determine whether Tom will be able to catch Jerry.
  Note that initially Jerry is not at the same position as Tom.
'''

for t in range(int(input())):
  
  X,Y = map(int, input().split())
  
  TomAndJerryChase = "YES" if X<Y else "NO"
  
  print(TomAndJerryChase)
