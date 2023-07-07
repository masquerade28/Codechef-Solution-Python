'''
  Chef had collected N notes of Rs. 2000 to pay his total college fees. 
  However, the government banned Rs. 2000 notes.
  Chef wants to pay the same amount using Rs. 500 notes only. 
  Find the number of notes Chef needs.
'''

# Taking Input For N = No. Of Notes Of Rs.2000 That Chef Has Collected
N = int(input())

# Number Of Rs.500 Notes Needed = 4*N, because To Make 2000 We Need 4 Notes Of 500
print(4*N)
