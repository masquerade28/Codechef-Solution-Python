'''
  In Chefland, everyone who earns strictly more than Y rupees per year, has to pay a tax to Chef. 
  Chef has allowed a special scheme where you can invest any amount of money and claim exemption for it.
  You have earned X (X>Y) rupees this year. 
  Find the minimum amount of money you have to invest so that you don't have to pay taxes this year.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For The Salary and Taxes Limit
  X,Y = input().split()
  
  # Converting Them Into Integer
  X,Y = int(X),int(Y)
  
  # Printing The Amount He Can Invest to Get Rid Of The Taxes
  print(X-Y)
