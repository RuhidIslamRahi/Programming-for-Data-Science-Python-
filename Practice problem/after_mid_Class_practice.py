# class 1
#Nested loop
#
for i in range(0,2):
    print("Printed by Outer loop: ")
    print(i)
    for j in range (50,52):
        print("Printed by Inner loop: ")
        print(j,end=" ")


#
for i in range(2):
    print("Printed by Outer loop: ")
    print(i)
    for j in range (50,52):
        print("Printed by Inner loop: ")
        print(j,end=" ")
    print(0)

#
for i in range(1,3):
    for j in range(1,3):
        print(i*j,end=" ")
    print() #New line

#
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()

#
rows = 5 
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#
rows = 5 
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

#
rows = 5 
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(5, end=" ")
    print()

#
rows = 5
for i in range(1, rows+1):
    for j in range(5,rows-i,-1):
        print(j, end=" ")
    print()




# class no 2

#
for i in range(1,7):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#
sum = 10
for i in range (1,4):
    sum = sum + 10
    for j in range (1,4):
        sum = sum + 20
        for k in range(1,4):
            sum = sum + 30
print(f"Total sum: {sum}") #---> Total sum: 1030

"""To calculate this sum manually within a fraction of a second, let's break down the loop logic and compute how many times each addition occurs, instead of simulating it step by step."""

sum = 10
for i in range (1, 4):          # i from 1 to 3 → 3 iterations
    sum = sum + 10              # adds 10 three times → 10 * 3 = 30
    for j in range (1, 4):      # j from 1 to 3 → 3 iterations per i → total 3 * 3 = 9
        sum = sum + 20          # adds 20 nine times → 20 * 9 = 180
        for k in range(1, 4):   # k from 1 to 3 → 3 iterations per j → total 3 * 3 * 3 = 27
            sum = sum + 30      # adds 30 twenty-seven times → 30 * 27 = 810


sum = 10
for i in range(1, 4):        # i loops 3 times (1,2,3)
    sum = sum + 10          # add 10 each time
    for j in range(1, 4):    # j loops 3 times
        sum = sum + 20      # add 20 each j
        for k in range(1, 4): # k loops 3 times
            sum = sum + 30  # add 30 each k




# class no 3

#
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(mat[0])
print(mat[2])
print(mat[0][0])
print(mat[1][0])
print(mat[2][0])
print(mat[2][-1])
print(mat[1][1])
print(mat[0][0]+mat[1][0]**2)

#
mat = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(mat)):
    for j in range(len(mat[1])):
        print(mat[i][j],end=" ")
    print()

#
# Question: Second coloum এর value squre করে sum
mat = [[1,2,3],[4,5,6],[7,8,9]]
sum = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if j==1:
            sum += mat[i][j] ** 2
    print(sum)

#

#
fruits = ["Apple","Orange","Banana","Coconut"]
name = ["Masud","Masum","Fahim","Ruhid","Rahi"]
laptop = ["Apple","Hp","Assus","Lenovo","Samsung"]

all_i = [fruits,name,laptop]

print(fruits )
print(name)
print(laptop)

print(all_i)

print(all_i[0])
print(all_i[1])
print(all_i[2])

print(all_i[0][0])
print(all_i[0][1])
print(all_i[0][2])
print(all_i[0][3])

print(all_i[1][0])
print(all_i[1][1])
print(all_i[1][2])
print(all_i[1][3])
print(all_i[1][4])

print(all_i[2][0])
print(all_i[2][1])
print(all_i[2][2])
print(all_i[2][3])
print(all_i[2][4])

for collection in all_i:
    # print(collection)
    for item in collection:
        print(item)
    print()

for collection in all_i:
    # print(collection)
    for item in collection:
        print(item)

for collection in all_i:
    # print(collection)
    for item in collection:
        print(item,end=" ")
    print()



# Dictionary & set
"""
Dictionary are used to store data values in key:value pairs
They are unordered, mutable(changeable) & don't allow duplicate keys
"""

"""
dict["name"], dict["cgpa"], dict["marks"]
dict["key"] = "value # 
"""

#
info = {
    "key" : "value",
    "name" : "Rahi",
    "subjects" : ["python", "java", "C"],#list store korlam
    "topics" : ("dict", "set"), # taple
    "learning" : "python",
    "marks" : 94.4,
    "is_adult" : True,
    12 : 233,
    20.32 : 243535.2
}

print(info)
print(type(info))
print(info["name"])
print(info["topics"])
print(info["subjects"])
print(info[12])

for key in info:
    print(key,info[key])

for key,value in info.item():
    print(key,end=" ")
    print(value)

for key in info.keys():
    print(key)

for key in info.values():
    print(value)



# name change kore onno valu add korbo / নতুন ভালু asign করতে চাইলে 

info["name"] = "Ruhid"
print(info)# name age cholo Rahi Akhon hoye gelo Ruhid 


# dictionary তে নতুন key, value add করতে চাইলে 
info["laptop"] = "mac"
print(info)

# create a empty dictionary 
null_dict = {}
print(null_dict)
# null dictionary er modhe value add korte caile 
null_dict = {}
null_dict["name"] = "Islam"
print(null_dict)

# Nested Dictionary

student = {
    "name" : "rahi",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

# Dictionary Methods
"""
-> myDict.keys() #returns all keys
-> myDict.values() #returns all values
-> myDict.items() #return all (key, val) pairs as tuples
-> myDict.get("key") #returns the key according to value
-> myDict.update(newDict) #inserts the specified items to the dictionary
"""
print(student.keys())
print(list(student.keys()))
print(len(student)) 
print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])
print(pairs[1])

print(student["name"])
print(student.get("name"))

print(student["name2"]) #error
print(student.get("name2")) #no error -> None

student.update({"city" : "bogura"})
print(student)

new_dict = {"city" : "bogura",
            "age" : 22}
student.update(new_dict)
print(student)


# class task

word = {}
word[1] = "Red"
word[2] = "Blue"
word[3] = "Pink"
print(word)
print(len(word))
for value in word.values() :
    # print(value)
    if len(value) > 3:
        print(value)





# Set in Python
"""
Set is the collection of the unordered items.
Each element in the set must be unique & immutable.

nums = {1, 2, 3, 4}
sets = {1, 2, 2, 2}
repeated elements stored only once, so it resolved to {1,2}

null_set = set() #empty set syntax

"""




# Python Functions

"""
A function is a block of code that performs a specific task whenever it is called.
in bigger problems, where we have large amounts of code, it is advisable to create .
use existing functions that make the problem flow organized and neat.

"""

# how to use some of the build in function
print()
round()
max()
len()
type()
range()


# how to Create own custom function 
#
def greet():
    print("hi there")
    print("welcome abroad")


greet()


#
def calculateGmean(a, b): #calculateGmean হল নাম , a b হল argument
    mean = (a*b)/(a+b)
    print(mean)

a = 9
b = 8
calculateGmean(a,b)

c = 8
d = 7
calculateGmean(c,d)

#
def isGreater (a,b):
    if a>b:
        print("First number is greater ")
    else:
        print("second number is greater or equal")

# Arguments
def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome abroad")


greet("Ruhid", "Rahi")
greet("Mosh", "Hamedani")

# Types of Functions

def greet (name):
    print(f"Hi {name}")


# in programming we have two types of functions
# 1- perform a task
# 2- calculate and Return a value

def get_greeting (name):
    return f"Hi {name}"


message = get_greeting("Rahi")
# print(massage)
# or 
file = open("content.txt", "w")
file.write(message)

# keyword Arguments
def increment(number,by):
    return number + by


result = increment(2,1)
print(result)

# ok we can simplefy this code
def increment(number,by):
    return number + by

print(increment(2,1))

# default Arguments
def increment(number, by=1):
    return number + by

print(increment(2))
print(increment(2,5))

def increment(number, by=1, another): # i can't add another required perameter
# we can see red underline here

# - all the optional perameter(by=1) should come after the require perameter
# - correct
def increment(number, another, by=1): 


#   *args, wait, what?
def multiply (x, y):
    return x * y

multiply(2, 3)

# whatif we want a pass  
multiply(1, 3, 3, 7)
# than we need to repalce these 2 perameaters
#  need a single perameater
def multiply (*numbers): # this plural name here says indicate the collcetion of arguments
    print(numbers)
    # return x * y

multiply(2, 3, 4, 5)#run this code দেখ কি আসে 

# step 1 print kore dekho ki asteche
def multiply (*numbers):
    for number in numbers:
        print(number)

multiply(2,3,4,5)

# step 2 
def multiply (*numbers):
    total = 1 # difine a variable
    for number in numbers:
        # total = total * number
        total *= number 
    return total


# finally
print(multiply(2,3,4,5))





#   **args

def save_user (**user):
    print(user)

save_user(id=1, name="John", age=22) #dictionary

#
def save_user (**user):
    print(user["id"])

save_user(id=1, name="John", age=22)


#
def save_user (**user):
    print(user["name"])

save_user(id=1, name="John", age=22)

#  Scope
def greet(name):
    message = "a"


print(name)












# function practice from chatGpt
# Add two numbers
def add (a, b):
    return a + b

result = add(23,345)
print(result)

# write a function named square that takes a number and returns its square
def square(num):
    return num**2

result= square(4)
print(result)

# ✅ তোমার জন্য এখন তিনটি practice challenge (Easy → Medium):
#🧩 Challenge 1:
# Write a function named is_even that takes a number and returns True if it’s even, otherwise False.
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
result = is_even(5)
print(result)
# আরও ছোট ও সুন্দর
def is_even(num):
    return num%2==0

# 🧩 Challenge 2:
# Write a function named greet_user that takes a name and prints:
# Hello, [name]! Welcome to Python.
def greet_user(name):
    return (f"Hello, [{name}]! Welcome to Python.")

greeter_name = greet_user("Rahi")
print(greeter_name)
"""
🧠 ছোট ২টা টিপ:
🔸 1. যদি তুমি শুধু print করতে চাও, তাহলে return এর দরকার নেই:

def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

greet_user("Rahi")
🔸 2. যদি তুমি message return করে পরে use করতে চাও, তখন return ব্যবহার করো (যেমন তুমি করেছো)।
তুমি চাইলে এই message file-এ লিখে রাখতে পারো, UI-তে দেখাতে পারো ইত্যাদি।

✅ Bottom line:
তুমি বুঝে লিখছো — সেটা সবচেয়ে বড় কথা!
👉 এবার চাইলে আমরা Challenge 3 (maximum of 2 numbers) করতে পারি!
"""

# 🧩 Challenge 3:
# Write a function maximum(a, b) that returns the greater of the two numbers.
def maximum(a,b):
    if a>b :
        return (f"{a} is the greater of the two numbers")
    elif b>a:
        return (f"{b} is the greater of the two numbers")
    else:
        return(f"the two numbers are equal")
    
maxi = maximum(23,324)
print(maxi)

# simple way
def maximum(a, b):
    return max(a, b)

print(maximum(23, 324))  # Output: 324


#
def sum_list(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

a = sum_list([1,3,3,4,45,4])
print(a)

# Function that counts even numbers from a list
def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count

result = count_even([2, 5, 8, 3, 4, 9])
print(result)  # Output: 3

# ✨ Bonus: আরও ছোট করে লিখতে চাইলে
def count_even(numbers):
    return len([num for num in numbers if num % 2 == 0])

result = count_even([2, 5, 8, 3, 4, 9])
print(result)  # Output: 3

# Write a function that takes a string and counts how many vowels are in it.
"""
✅ Input:
"Ruhid Islam Rahi"
✅ Output:
6
"""
def count_vowels(text):
    total_vowel_count = 0
    for letter in text:
        if letter.lower() in "aeiou":
   
            total_vowel_count += 1
    return total_vowel_count

result = count_vowels("Ruhid Islam Rahi")
print(result)
# more compact
def count_vowels(text):
    return sum(1 for letter in text if letter.lower() in "aeiou")

# 🧩 Challenge: Return All Vowels from a String in a List
"""
✅ Problem:
তুই এমন একটা function বানাবি যেটা:

একটি string ইনপুট হিসেবে নিবে

ওই string-এর সব vowel গুলো খুঁজে একটা list আকারে return করবে
Input:
"Data Science with Python"

Output:
['a', 'a', 'i', 'e', 'e', 'i', 'o']
"""
def extract_vowels(text):
    vowel = []
    for letter in text:
        if letter.lower() in "aeiou":
            vowel.append(letter)
    return vowel

        
inp = extract_vowels("Data Science with Python")
print(inp)  

# Count total words in a string using a function
"""
Input: "Python is easy to learn"
Output: 5
"""
def total_words(text):
    split_words = text.split()
    count = 0
    for word in split_words:
        count = count + 1
    return count

j = total_words("Python is easy to learn")
print(j)
# 🧠 Bonus Tip (shorter version):
def total_words(text):
    return len(text.split())

# 🧩 Challenge: Find the Longest Word from a Sentence
"""
Input: "Python is incredibly powerful"
Output: "incredibly"
"""
def long_word(text):
    split_words = text.split()
    longest= ""
    for word in split_words:
        if len(word) > len (longest):
            longest = word
    return longest

inp = long_word("Python is incredibly powerful")
print(inp)
#
def long_word(text):
    return max(text.split(), key=len)

# 🧩 Challenge: Count Word Frequency Using Dictionary
"""
🎯 Problem:
-- তুই এমন একটা function বানাবি, যেটা:

-- একটি sentence ইনপুট হিসেবে নিবে

প্রত্যেকটি word কতবার এসেছে — সেটা dictionary আকারে return করবে
Input:
"python is easy and python is powerful"
Output:
{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
"""
def word_count(text):
    split_word = text.split()
    count_dict = {}
    for word in split_word:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict

result = word_count("python is easy and python is powerful")
print(result)

# 🧩 Next Challenge: Find the Most Frequent Word
"""
Input: "python is easy and python is powerful"
Output: "python"
"""
def word_count(text):
    split_words = text.split()
    count_dict = {}
    for word in split_words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
        #{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
    max_word = ""
    max_count = 0
    for word, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_word = word
    return max_word

result = word_count("python is easy and python is powerful")
print(result)  # Output: python

def most_frequent_letter(text):
    count_dict = {}

    for char in text:
        if char != " ":
            char = char.lower()
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1

    max_letter = ""
    max_count = 0

    for letter, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_letter = letter

    return max_letter





  




            



