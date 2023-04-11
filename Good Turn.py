"""
Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once.
They consider a turn to be good if the sum of the numbers on their dice is greater than 6. 
Given that in a particular turn Chef and Chefina got X and Y on their respective dice, find whether the turn was good.
"""

def is_good_turn(x,y):
    if (x+y) > 6:
        return "YES" 
    else:
        return "NO"

L=[]       
t = int(input())

for i in range(t):
    x,y = map(int, input().split())
    result = is_good_turn(x,y)
    L.append(result)
    
for i in L:
    print(i)
