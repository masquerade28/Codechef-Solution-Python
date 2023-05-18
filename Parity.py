'''
  Ashu and Arvind participated in a coding contest, as a result of which they received N chocolates. 
  Now they want to divide the chocolates between them equally.
  Can you help them by deciding if it is possible for them to divide all the N chocolates in such a way that they each get an equal number of chocolates?
  You cannot break a chocolate in two or more pieces.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For N = No. Of Chocolates
  N = int(input())
  
  # If The No. Of chocolates Are Even Then It Can Be Equally Divided Among The Two
  Parity = "YES" if (N % 2 == 0) else "NO"
  
  print(Parity)
