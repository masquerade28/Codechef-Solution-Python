'''
  Chef is fond of burgers and decided to make as many burgers as possible.
  Chef has A patties and B buns. 
  To make 1 burger, Chef needs 1 patty and 1 bun.
  Find the maximum number of burgers that Chef can make.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # A = No. Of Patties ; B = No. Of Buns
  A,B = input().split()
  
  # Converting Input Into Integers
  A,B = int(A),int(B)
  
  # To Find The Maximum No. Of Burgers That Chef Can Find We Have To Find The Quatintity Which Is Less Among The Buns and Patties
  Burgers = A if A < B else B
  
  print(Burgers)
