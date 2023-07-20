'''
  Chef and some of his friends are planning to participate in a puzzle hunt event.
  The rules of the puzzle hunt state:
    -> "This hunt is intended for teams of 6 to 8 people."
  Chef's team has N people in total. 
  Are they eligible to participate?
'''

N = int(input())
PuzzleHunt = "YES" if N>=6 and N<=8 else "NO"
print(PuzzleHunt)
