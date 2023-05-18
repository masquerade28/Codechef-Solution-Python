'''
  In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:
    -> Top 10 participants receive rupees X each.
    -> Participants with rank 11 to 100 (both inclusive) receive rupees Y each.
  Find the total prize money over all the contestants.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = The Prize For Top 10 Rankers ; Y = The Prize For Ranks 11 to 100
  X,Y = map(int, input().split())
  
  # Top 10 Participants Receive Rupees X And Next 90 Participants Receive Rupees Y Each. So, Total Prize Money = 10*X + 90*Y
  print((10*X)+(90*Y))
