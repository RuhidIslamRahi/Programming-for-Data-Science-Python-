

"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1 
"""
rows = 5
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
rows = 5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

"""
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""
rows = 5
for i in range(0,rows):
    for j in range(0,i+1):
        print(rows-i,end=" ")
    print()


"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
rows = 5 
for i in range(0,rows):
    for j in range(0,i+1):
        print(rows,end=" ")
        rows -= 1
    print()
"""
*
* *
* * *
* * * *
* * * * *
"""
r = 5
for i in range(1,r+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

"""
* * * * *
* * * *
* * *
* *
*
"""
n = 5
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()




