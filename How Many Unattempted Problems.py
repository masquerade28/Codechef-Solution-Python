'''
  Our Chef is currently practicing on CodeChef and is a beginner. 
  The count of ‘All Problems’ in the Beginner section is X. 
  Our Chef has already ‘Attempted’ Y problems among them. How many problems are yet ‘Un-attempted’?
'''

# Taking Input Into String Form And Separating Them
X,Y = input().split()

# Converting Input Into Integers
X,Y = int(X),int(Y)

# To Get The Un-attempted Problems We Have To Just Subtract The Attempted Ones From The Total
print(X-Y)
