'''
  In a contest where N new users visited the contest,
    -> A users just saw the problems and didn’t make any submissions and hence won’t get any rating.
    -> B users who made a submission but could not solve any problem correctly. Thus, after the contest, they will get a rating in the range 800−1000.
    -> Everyone else could correctly solve at least 1 problem. Thus, they will get a rating strictly greater than 1000 after the contest.
  You need to output the number of new users in the contest who, after the contest, will get a rating and also the number of new users who will get a rating strictly greater than 1000.
'''

# Taking Input For N = New Users Who Visited The Contest; A = Who Just Saw the Problem And Didn't Make Any Submission; B = Who Made Submission But Couldn't Solve Any Problem Correctly
N,A,B = map(int, input().split())

# There were N new users. Among those N, A didn't make any submissions. This means that the other N−A users made submissions and will get a rating. 
# Among these N-A users, B couldn't solve any problem even though they submitted and tried. 
# So, they will get a rating less than equal to 1000. The other N-A−B users were able to solve at least 1 problem and hence will get a rating greater than 1000. 
print(N-A, N-(A+B))
