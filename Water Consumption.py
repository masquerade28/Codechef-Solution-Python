'''
  Recently, Chef visited his doctor. 
  The doctor advised Chef to drink at least 2000 ml of water each day. 
  Chef drank X ml of water today. Determine if Chef followed the doctor's advice or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For Amount Of Water Chef Drank
  x = int(input())
  
  # Printing "YES" if Chef Drank Enough Water Otherwise "NO"
  water_consumption = "YES" if x >= 2000 else "NO"
  
  print(water_consumption)
