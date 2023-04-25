'''
  Chef and his girlfriend go on a date. Chef took X dollars with him, and was quite sure that this would 
  be enough to pay the bill. At the end, the waiter brought a bill of Y dollars. Print "YES" if Chef has 
  enough money to pay the bill, or "NO" if he has to borrow from his girlfriend and leave a 
  bad impression on her.
'''

# Taking Number of Test Cases and Looping
for i in range (int(input())): 
  
  # Taking Input For b (Money Chef Is Carrying) and  p(Money He Has To Pay ) in sigle line
  b,p = map(int, input().split()) 
  
  # Checking If He Have Enough Money
  if b >= p:
    
    print("YES")
    
  else:
      print("NO")
