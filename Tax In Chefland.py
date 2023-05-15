'''
  In Chefland, a tax of rupees 10 is deducted if the total income is strictly greater than rupees 100.
  Given that total income is X rupees, find out how much money you get.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input X = Total Income
  X = int(input())
  
  # If Total Income Is Greater Than 100 The Money You Will Be Left With Will Be Income - 10
  # Else No Tax Will Be Deducted
  Tax = (X-10) if X>100 else X
  
  print(Tax)
