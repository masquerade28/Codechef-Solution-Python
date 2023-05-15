'''
  DAIICT college students want to attend an IPL match.
  A total of N students from the college want to go while only M tickets are available for the match.
  Determine how many students won't be able to book tickets.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input N = No. Of Students ; M = No. Of Tickets Available
  N,M = map(int, input().split())
  
  # If No. Of Students Is Greater Than Tickets Available It Gives (N-M) i.e; No. Of Students Who Will Not Be Able To Book Tickets.
  # If No. Of Tickets Is Greater Than No. Of Students Than Every Student Will Be Able To Book Tickets. 
  Tickets = (N-M) if (N>=M) else 0
  
  print(Tickets)
