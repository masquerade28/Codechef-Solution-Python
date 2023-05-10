'''
  According to a recent survey, Biryani is the most ordered food. 
  Chef wants to learn how to make world-class Biryani from a MasterChef. 
  Chef will be required to attend the MasterChef's classes for X weeks, and the cost of classes per week is Y coins. 
  What is the total amount of money that Chef will have to pay?
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input; X = Weeks To Attend and Y = Cost per Week
  X,Y = input().split()
  
  # Converting X and Y Into Integers
  X,Y = int(X),int(Y)
  
  # Total Amount Of Money That Chef Will Have To Pay
  print(X*Y)
