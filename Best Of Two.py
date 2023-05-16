'''
  Chef took an examination two times. 
  In the first attempt, he scored X marks while in the second attempt he scored Y marks. 
  According to the rules of the examination, the best score out of the two attempts will be considered as the final score.
  Determine the final score of the Chef.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For The Marks Scored In First Attempt And Marks Scored In Second Attempt
  X,Y = map(int, input().split())
  
  # Printing The Best Of Two
  print(max(X,Y))
