'''
  Harsh was recently gifted a book consisting of N pages. 
  Each page contains exactly M words printed on it. 
  As he was bored, he decided to count the number of words in the book.
  Help Harsh find the total number of words in the book.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For N = No. Of Pages ; M = No. Of Words On Each Page
  N,M = map(int, input().split())
  
  # Total No. Of Words = No. Of Words On Each Page * Total No. Of Pages
  print(N*M)
