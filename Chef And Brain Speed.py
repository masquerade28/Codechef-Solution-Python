'''
  In ChefLand, human brain speed is measured in bits per second (bps). 
  Chef has a threshold limit of X bits per second above which his calculations are prone to errors. 
  If Chef is currently working at Y bits per second, is he prone to errors?
  If Chef is prone to errors print YES, otherwise print NO.
'''

# Taking Input For X = Chef's Threshold Limit ; Y = Rate At Which Chef Is Currently Working At
X,Y = map(int, input().split())

# If Chef's Current Brain Speed Is Greater Than The Threshold Than Chef Is Prone To Errors
BrainSpeed = "YES" if Y>X else "NO"

print(BrainSpeed)
