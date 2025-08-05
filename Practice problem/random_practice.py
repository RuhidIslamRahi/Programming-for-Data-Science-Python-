my_list = ["Rahi",1,2,"Egg",99,"Dhaka","Uiu","Bogura","Uiu"]

print(len(my_list))
# 1 -->25
# 2 -- hridoy
# dah-- del
# 4 -- del
# las-- 2025

# my_list[1]=25
# print(my_list)
# my_list.insert(2,"Hridoy")
# print(my_list)
# my_list.remove("Dhaka")
# print(my_list)
# my_list.pop(4)
# print(my_list)


# lost_list = ["hridoy","rahi","mosque",99,5,"floor"]
# # while 
# index = 0
# while index < len(lost_list):
#     print(lost_list[index])
#     index+=1


# for i in range(0,6):
#     print(lost_list[i])


for i in range(0,101,2):
    print(i)


num = 1
sum = 0
while num < 101:
    # print(num)
    sum = sum + num
    num+=2
print(sum)






rows = int(input("Enter rows: "))
columns = int(input("Enter col: "))
symbol =input("Enter sym: ")
for i in range(rows):
    for y in range(columns):
        print(symbol,end=" ")
    print()




    

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




